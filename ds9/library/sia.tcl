#  Copyright (C) 1999-2018
#  Smithsonian Astrophysical Observatory, Cambridge, MA, USA
#  For conditions of distribution and use, see copyright notice in "copyright"

package provide DS9 1.0

proc SIADef {} {
    global sia
    global isia
    global psia
    global wcs

    set isia(sias) {}

    set isia(rformat) arcmin
    set isia(radius) 15

    set isia(minrows) 20
    set isia(mincols) 10

    set isia(mode) new
    set isia(save) 0

    set isia(def) { \
			{{2MASS (NASA/IPAC)} \
			     sia2mass \
			     {http://irsa.ipac.caltech.edu/cgi-bin/2MASS/IM/nph-im_sia}\
			     {} \
			} \
			{{AKARI (ISAS/JAXA)} \
			     siaakari \
			     {http://jvo.nao.ac.jp/skynode/do/siap/akari/fis_image_v1/1.0}\
			     {} \
			} \
			{{Astro-Wise} \
			     siaastrowise \
			     {http://vo.astro-wise.org/SIAP}\
			     {VERB=2&FORM=VOTable&PROJECT=ALL&INSTRUMENT=ALL&} \
			} \
			{{CADC} \
			     siacadc \
			     {http://www.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/sia/query}\
			     {} \
			} \
			{{Chandra (NASA/CXC)} \
			     siacxc \
			     {http://cda.harvard.edu/cxcsiap/queryImages}\
			     {} \
			} \
			{{Hubble Legacy Archive (STSCI)} \
			     siahla \
			     {http://hla.stsci.edu/cgi-bin/hlaSIAP.cgi}\
			     {} \
			} \
			{{MAST (STSCI)} \
			     siamast \
			     {http://archive.stsci.edu/siap/search.php}\
			     {} \
			} \
			{{SDSS DR12} \
			     siasdss \
			     {http://skyserver.sdss.org/SkyserverWS/dr12/SIAP/getSIAP}\
			     {} \
			} \
			{{SkyView (NASA/HEASARC)} \
			     siaskyview \
			     {http://skyview.gsfc.nasa.gov/cgi-bin/vo/sia.pl}\
			     {} \
			} \
			{{TGSSADR (GMRT)} \
			     siatgssadr \
			     {http://vo.astron.nl/tgssadr/q_fits/imgs/siap.xml}\
			     {} \
			 } \
		    }
}

proc SIAAnalysisMenu {mb} {
    global isia
    global ds9

    foreach ff $isia(def) {
	set title [lindex $ff 0]
	set vars [lindex $ff 1]
	set url [lindex $ff 2]
	set opts [lindex $ff 3]

	$mb add command -label $title \
	    -command [list SIADialog $vars $title $url $opts apply]
    }
}

proc SIAGetURLFinish {varname token} {
    upvar #0 $varname var
    global $varname

    global debug
    if {$debug(tcl,sia)} {
	puts stderr "SIAGetURLFinish $varname"
    }

    if {!($var(active))} {
	SIACancelled $varname
	return
    }

    upvar #0 $token t

    # Code
    set code [http::ncode $token]

    # Meta
    set meta $t(meta)

    # Log it
    HTTPLog $token

    # Result?
    switch -- $code {
	{} -
	200 -
	203 -
	404 -
	503 {
	    VOTParse $var(tbldb) $token
	    SIADone $varname
 	    SIALoadDone $varname
	}

	201 -
	300 -
	301 -
	302 -
	303 -
	305 -
	307 {
	    foreach {name value} $meta {
		if {[regexp -nocase ^location$ $name]} {
		    global debug
		    if {$debug(tcl,sia)} {
			puts stderr "SIAGetURLFinish redirect $code to $value"
		    }
		    # clean up and resubmit
		    http::cleanup $token
		    unset var(token)

		    SIALoad $varname $value $var(qq)
		}
	    }
	}

	default {
	    eval [list $var(proc,error) $varname "[msgcat::mc {Error code was returned}] $code"]
	}
    }
}

proc SIALoad {varname url query} {
    upvar #0 $varname var
    global $varname

    # clear previous db
    global $var(tbldb)
    if {[info exists $var(tbldb)]} {
	unset $var(tbldb)
    }

    global debug
    if {$debug(tcl,sia)} {
	puts stderr "SIALoad $varname $url?$query"
    }

    TBLGetURL $varname $url $query
    return
}

proc SIALoadDone {varname} {
    upvar #0 $varname var
    global $varname

    global debug
    if {$debug(tcl,sia)} {
	puts stderr "SIALoadDone $varname"
    }

    SIATable $varname
    SIADialogUpdate $varname
}

proc SIAOff {varname} {
    upvar #0 $varname var
    global $varname

    global $var(tbldb)
    if {[info exists $var(tbldb)]} {
	unset $var(tbldb)
    }
    set db $var(tbldb)
    set ${db}(Nrows) {}

    $var(tbl) selection clear all

    SIADialogUpdate $varname
}

proc SIATable {varname} {
    upvar #0 $varname var
    global $varname
    global $var(tbldb)
    global isia

    global debug
    if {$debug(tcl,sia)} {
	puts stderr "SIATable $varname"
    }

    if {![TBLValidDB $var(tbldb)]} {
	return
    }

    # clear the selection
    $var(tbl) selection clear all

    global $var(tbldb)
    $var(found) configure -textvariable ${var(tbldb)}(Nrows)

#    starbase_writefp $var(tbldb) stdout

    if {[starbase_nrows $var(tbldb)] == 0} {
	ARStatus $varname [msgcat::mc {No Items Found}]
	return
    }

    set nc [starbase_ncols $var(tbldb)]
    if { $nc > $isia(mincols)} {
	$var(tbl) configure -cols $nc
    } else {
	$var(tbl) configure -cols $isia(mincols)
    }

    # add header
    set nr [expr [starbase_nrows $var(tbldb)]+1]
    if {$nr > $isia(minrows)} {
	$var(tbl) configure -rows $nr
    } else {
	$var(tbl) configure -rows $isia(minrows)
    }
}

# Process Cmds

proc ProcessSIACmd {varname iname} {
    upvar $varname var
    upvar $iname i

    global isia
    # we need to be realized
    ProcessRealizeDS9

    set ref [lindex $isia(sias) end]
    global cvarname
    set cvarname $ref

    sia::YY_FLUSH_BUFFER
    sia::yy_scan_string [lrange $var $i end]
    sia::yyparse
    incr i [expr $sia::yycnt-1]
}

proc SIACmdCheck {} {
    global cvarname
    upvar #0 $cvarname cvar

    if {![info exists cvar(top)]} {
	Error "[msgcat::mc {Unable to find SIAP window}] $cvarname"
	return 0
    }
    if {![winfo exists $cvar(top)]} {
	Error "[msgcat:: mc {Unable to find SIAP window}] $cvarname"
	return 0
    }
    return 1
}

proc SIACmdRef {ref} {
    global isia
    global cvarname

    # look for reference in current list
    if {[lsearch $isia(sias) sia${ref}] < 0} {
	# see if its from our list of sias
	foreach mm $isia(def) {
	    set title [lindex $mm 0]
	    set vars [lindex $mm 1]
	    set url [lindex $mm 2]
	    set opts [lindex $mm 3]

	    if {$title != {-} && "sia${ref}" == $vars} {
		SIADialog $vars $title $url $opts sync
		set cvarname sia${ref}
	    }
	}
    }
}

proc ProcessSendSIACmd {proc id param sock fn} {
    global isia
    $proc $id "$isia(sias)\n"
}
