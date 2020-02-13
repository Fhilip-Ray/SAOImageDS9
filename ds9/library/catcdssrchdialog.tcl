#  Copyright (C) 1999-2018
#  Smithsonian Astrophysical Observatory, Cambridge, MA, USA
#  For conditions of distribution and use, see copyright notice in "copyright"

package provide DS9 1.0

proc CATCDSSrchDialog {varname} {
    upvar #0 $varname var
    global $varname

    global ds9
    global pcat
    global icatcdssrch

    global debug
    if {$debug(tcl,cat)} {
	puts stderr "CATCDSSrchDialog $varname"
    }

    # main dialog
    set var(top) ".${varname}"
    set var(mb) ".${varname}mb"

    if {[winfo exists $var(top)]} {
	raise $var(top)
	return
    }

    # procs
    set var(proc,process) CATCDSSrchProcess
    set var(proc,load) CATCDSSrchLoad
    set var(proc,error) ARError

    # defaults
    set var(list,wave,param) $icatcdssrch(list,wave,param)
    set var(list,wave) $icatcdssrch(list,wave)
    set var(list,mission,param) $icatcdssrch(list,mission,param)
    set var(list,mission) $icatcdssrch(list,mission)
    set var(list,astro,param) $icatcdssrch(list,astro,param)
    set var(list,astro) $icatcdssrch(list,astro)

    # AR variables
    set var(status) {}
    set var(sync) 0

    # CATCDSSrch variables
    set var(catdb) ${varname}catdb
    set var(server) $pcat(server)

    set var(source) {}
    set var(words) {}
    set var(wave) {}
    set var(mission) {}
    set var(astro) {}

    # create the window
    set w $var(top)
    set mb $var(mb)

    Toplevel $w $mb 7 [msgcat::mc {Search for Catalogs}] \
	"CATCDSSrchDestroy $varname"

    # file
    $mb add cascade -label [msgcat::mc {File}] -menu $mb.file
    menu $mb.file
    $mb.file add command -label "[msgcat::mc {Open}]..." \
	-command "CATCDSSrchLoadFile $varname" -accelerator "${ds9(ctrl)}O"
    $mb.file add command -label "[msgcat::mc {Save}]..." \
	-command "CATCDSSrchSaveFile $varname" -accelerator "${ds9(ctrl)}S"
    $mb.file add separator
    $mb.file add command -label [msgcat::mc {Retrieve}] \
	-command "CATCDSSrchApply $varname"
    $mb.file add command -label [msgcat::mc {Cancel}] \
	-command "ARCancel $varname"
    $mb.file add separator
    $mb.file add command -label [msgcat::mc {Load}] \
	-command "CATCDSSrchCatalog $varname"
    $mb.file add command -label [msgcat::mc {Clear}] \
	-command "CATCDSSrchClear $varname"
    $mb.file add separator
    $mb.file add command -label [msgcat::mc {Close}] \
	-command "CATCDSSrchDestroy $varname" -accelerator "${ds9(ctrl)}W"

    # edit
    AREditMenu $varname

    # catalog server
    CATServerMenu $varname

    # Param
    set f [ttk::frame $w.param]

    ttk::frame $f.name 
    ttk::frame $f.words
    ttk::frame $f.srch 
    pack $f.name -side top -fill x -expand true
    pack $f.words -side top -fill x -expand true
    pack $f.srch -side bottom -fill both -expand true

    # param name
    ttk::label $f.name.title -text [msgcat::mc {Name or Designation}]
    ttk::entry $f.name.source -textvariable ${varname}(source)
    pack $f.name.title -side top -anchor w -padx 2 -pady 2
    pack $f.name.source -side top -anchor w -padx 2 -pady 2 -fill x -expand true

    # param keywords
    ttk::label $f.words.title \
	-text [msgcat::mc {Words matching title, description}]
    ttk::entry $f.words.key -textvariable ${varname}(words) -width 45
    pack $f.words.title -side top -anchor w -padx 2 -pady 2
    pack $f.words.key -side top -anchor w -padx 2 -pady 2 -fill x -expand true

    # param search
    ttk::frame $f.srch.wave
    ttk::frame $f.srch.mission
    ttk::frame $f.srch.astro
    pack $f.srch.wave $f.srch.mission $f.srch.astro \
	-side left -fill both -expand true -padx 2 -pady 2

    # param search wave
    ttk::frame $f.srch.wave.f
    ttk::label $f.srch.wave.title -text [msgcat::mc {Wavelength}]
    pack $f.srch.wave.title -side top -anchor w
    pack $f.srch.wave.f -side bottom -fill both -expand true \
	-anchor w -padx 2 -pady 2

    ttk::scrollbar $f.srch.wave.f.scroll \
	-command [list $f.srch.wave.f.list yview]
    set ${varname}(listbox,wave) [listbox $f.srch.wave.f.list \
				      -yscroll \
				      [list $f.srch.wave.f.scroll set] \
				      -setgrid true \
				      -selectmode browse \
				      -exportselection 0 \
				      -listvariable ${varname}(list,wave)]
    grid $f.srch.wave.f.list $f.srch.wave.f.scroll -sticky news
    grid rowconfigure $f.srch.wave.f 0 -weight 1
    grid columnconfigure $f.srch.wave.f 0 -weight 1

    # param search mission
    ttk::frame $f.srch.mission.f
    ttk::label $f.srch.mission.title -text [msgcat::mc {Mission}]
    pack $f.srch.mission.title -side top -anchor w
    pack $f.srch.mission.f -side bottom -fill both -expand true \
	-anchor w -padx 2 -pady 2

    ttk::scrollbar $f.srch.mission.f.scroll \
	-command [list $f.srch.mission.f.list yview]
    set ${varname}(listbox,mission) [listbox $f.srch.mission.f.list \
					 -yscroll \
					 [list $f.srch.mission.f.scroll set] \
					 -setgrid true \
					 -selectmode browse \
					 -exportselection 0 \
					 -listvariable ${varname}(list,mission)]
    grid $f.srch.mission.f.list $f.srch.mission.f.scroll \
	-sticky news
    grid rowconfigure $f.srch.mission.f 0 -weight 1
    grid columnconfigure $f.srch.mission.f 0 -weight 1

    # param search astro
    ttk::frame $f.srch.astro.f
    ttk::label $f.srch.astro.title -text [msgcat::mc {Astronomy}]
    pack $f.srch.astro.title -side top -anchor w
    pack $f.srch.astro.f -side bottom -fill both -expand true \
	-anchor w -padx 2 -pady 2

    ttk::scrollbar $f.srch.astro.f.scroll \
	-command [list $f.srch.astro.f.list yview]
    set ${varname}(listbox,astro) [listbox $f.srch.astro.f.list \
				       -yscroll \
				       [list $f.srch.astro.f.scroll set] \
				       -setgrid true \
				       -selectmode browse \
				       -exportselection 0 \
				       -listvariable ${varname}(list,astro)]
    grid $f.srch.astro.f.list $f.srch.astro.f.scroll -sticky news
    grid rowconfigure $f.srch.astro.f 0 -weight 1
    grid columnconfigure $f.srch.astro.f 0 -weight 1

    # Table
    set f [ttk::frame $w.tbl]

    set var(tbl) [table $f.t \
		      -state disabled \
		      -usecommand 0 \
		      -variable $var(catdb) \
		      -colorigin 1 \
		      -roworigin 0 \
		      -cols $icatcdssrch(mincols) \
		      -rows $icatcdssrch(minrows) \
		      -colstretchmode all \
		      -width -1 \
		      -height -1 \
		      -maxwidth 400 \
		      -maxheight 190 \
		      -titlerows 1 \
		      -xscrollcommand [list $f.xscroll set]\
		      -yscrollcommand [list $f.yscroll set]\
		      -selecttype row \
		      -selectmode extended \
		      -anchor w \
		      -font [font actual TkDefaultFont] \
		      -fg $ds9(gui,fg) -bg $ds9(gui,bg) \
		     ]

    ttk::scrollbar $f.yscroll -command [list $var(tbl) yview] \
	-orient vertical
    ttk::scrollbar $f.xscroll -command [list $var(tbl) xview] \
	-orient horizontal

    grid $var(tbl) $f.yscroll -sticky news
    grid $f.xscroll -stick news
    grid rowconfigure $f 0 -weight 1
    grid columnconfigure $f 0 -weight 1

    # Status
    set f [ttk::frame $w.status]

    ttk::label $f.title -text [msgcat::mc {Status}]
    ttk::label $f.item -textvariable ${varname}(status)
    pack $f.title $f.item -side left -anchor w -padx 2 -pady 2

    # Buttons
    set f [ttk::frame $w.buttons]

    set var(apply) [ttk::button $f.apply \
			-text [msgcat::mc {Retrieve}] \
			-command "CATCDSSrchApply $varname"]
    set var(cancel) [ttk::button $f.cancel \
			 -text [msgcat::mc {Cancel}] \
			 -command "ARCancel $varname" -state disabled]
    ttk::button $f.catalog -text [msgcat::mc {Load}] \
	-command "CATCDSSrchCatalog $varname"
    ttk::button $f.clear -text [msgcat::mc {Clear}] \
	-command "CATCDSSrchClear $varname"
    ttk::button $f.close -text [msgcat::mc {Close}] \
	-command "CATCDSSrchDestroy $varname"
    pack $f.apply $f.cancel $f.catalog $f.clear $f.close \
	-side left -expand true	-padx 2 -pady 4

    # Fini
    ttk::separator $w.sep -orient horizontal
    ttk::separator $w.stbl -orient horizontal
    ttk::separator $w.sstatus -orient horizontal
    pack $w.buttons $w.sstatus $w.status $w.stbl -side bottom -fill x
    pack $w.param $w.sep -side top -fill x
    pack $w.tbl -side top -fill both -expand true

    ARStatus $varname {}

    # initialize
    $var(listbox,wave) selection set 0
    $var(listbox,mission) selection set 0
    $var(listbox,astro) selection set 0
    $w.param.name.source select range 0 end

    bind $w <<Open>> [list CATCDSSrchLoadFile $varname]
    bind $w <<Save>> [list CATCDSSrchSaveFile $varname]
    bind $w <<Close>> [list CATCDSSrchDestroy $varname]
}

proc CATCDSSrchApply {varname} {
    upvar #0 $varname var
    global $varname

    global icatcdssrch

    global debug
    if {$debug(tcl,cat)} {
	puts stderr "CATCDSSrchApply $varname"
    }

    set id [$var(listbox,wave) curselection]
    if {$id > 0} {
	set var(wave) [lindex $var(list,wave) $id]
    } else {
	set var(wave) {}
    }
    set id [$var(listbox,mission) curselection]
    if {$id > 0} {
	set var(mission) [lindex $var(list,mission) $id]
    } else {
	set var(mission) {}
    }
    set id [$var(listbox,astro) curselection]
    if {$id > 0} {
	set var(astro) [lindex $var(list,astro) $id]
    } else {
	set var(astro) {}
    }

    ARApply $varname
    ARStatus $varname [msgcat::mc {Contacting Server}]
    CATCDSSrch $varname
}

proc CATCDSSrch {varname} {
    upvar #0 $varname var
    global $varname
    global pcat

    global debug
    if {$debug(tcl,cat)} {
	puts stderr "CATCDSSrch $varname"
    }

    #url
    set site [CATCDSURL $var(server)]
    set cgidir {viz-bin}
    set script {votable}
    set url "http://$site/$cgidir/$script"
    
    # defaults
    set query {-meta}
    append query "&[http::formatQuery -out.max 1000]"
    append query "&[http::formatQuery -out.form VOTable]"

    if {$var(source) != {}} {
	append query "&[http::formatQuery -source $var(source)]"
    }
    if {$var(words) !={}} {
	append query "&[http::formatQuery -words $var(words)]"
    }
    if {$var(wave) !={}} {
	append query "&[http::formatQuery $var(list,wave,param) $var(wave)]"
    }
    if {$var(mission) !={}} {
	append query "&[http::formatQuery $var(list,mission,param) $var(mission)]"
    }
    if {$var(astro) !={}} {
	append query "&[http::formatQuery $var(list,astro,param) $var(astro)]"
    }

    CATCDSSrchLoad $varname $url $query
}

proc CATCDSSrchDestroy {varname} {
    upvar #0 $varname var
    global $varname
    global $var(catdb)

    global debug
    if {$debug(tcl,cat)} {
	puts stderr "CATCDSSrchDestroy $varname"
    }

    if {[info exists $var(catdb)]} {
	unset $var(catdb)
    }

    ARDestroy $varname
}
