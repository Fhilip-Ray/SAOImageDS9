#  Copyright (C) 1999-2018
#  Smithsonian Astrophysical Observatory, Cambridge, MA, USA
#  For conditions of distribution and use, see copyright notice in "copyright"

package provide DS9 1.0

# used by backup
proc PlotScatterTool {} {
    global iap

    PlotScatter $iap(tt) [msgcat::mc {Scatter Plot Tool}] {} {} {} 2 {}
}

proc PlotScatter {tt wtt title xaxis yaxis dim data} {
    global iap

    # make the window name unique
    set ii [lsearch $iap(windows) $tt]
    if {$ii>=0} {
	incr iap(unique)
	append tt $iap(unique)
    }

    # set the window title if none
    if {$wtt == {}} {
	set wtt $tt
    }

    set varname $tt
    upvar #0 $varname var
    global $varname

    PlotScatterDialog $varname $wtt
    PlotTitle $varname $title $xaxis $yaxis
    PlotAddDataSet $varname $dim $data
    PlotStats $varname
    PlotList $varname

    global ds9
    switch $ds9(wm) {
	x11 {
	    update idletasks
	    wm geometry $var(top) \
		"[winfo width $var(top)]x[winfo height $var(top)]"
	}
	aqua -
	win32 {}
    }
}

proc PlotScatterDialog {varname wtt} {
    upvar #0 $varname var
    global $varname

    set var(proc,addgraph) PlotScatterAddGraph
    set var(proc,updateelement) PlotScatterUpdateElement
    set var(proc,highlite) PlotScatterHighliteElement
    set var(proc,button) PlotScatterButton

    PlotDialog $varname $wtt
    PlotAddGraph $varname
}


proc PlotScatterMenus {varname} {
    upvar #0 $varname var
    global $varname

    # Data
    menu $var(mb).datascatter
    $var(mb).datascatter add checkbutton -label [msgcat::mc {Show}] \
	-variable ${varname}(graph,ds,show) \
	-command [list PlotScatterUpdateElement $varname]
    $var(mb).datascatter add separator
    $var(mb).datascatter add cascade -label [msgcat::mc {Shape}] \
	-menu $var(mb).datascatter.shape
    $var(mb).datascatter add cascade -label [msgcat::mc {Error}] \
	-menu $var(mb).datascatter.error
    $var(mb).datascatter add separator
    $var(mb).datascatter add command -label "[msgcat::mc {Name}]..." \
	-command [list DatasetNameDialog $varname]

    # Shape
    PlotShapeMenu $varname datascatter

    # Error
    PlotErrorMenu $varname datascatter
}


proc PlotScatterAddGraph {varname} {
    upvar #0 $varname var
    global $varname

    set var(graph,type) scatter
    blt::graph $var(graph) -width 600 -height 500 -highlightthickness 0
}

proc PlotScatterUpdateElement {varname} {
    upvar #0 $varname var
    global $varname

    PlotSaveState $varname

    set cc $var(graph,current)
    if {[llength $var($cc,dss)] == 0} {
 	return
    }
    
    if {$var(graph,ds,shape,symbol) == "none"} {
	set var(graph,ds,shape,symbol) circle
    }

    if {$var(graph,ds,shape,fill)} {
	set clr $var(graph,ds,shape,color)
    } else {
	set clr {}
    }

    if {$var(graph,ds,error)} {
	set show both
    } else {
	set show none
    }

    if {$var(graph,ds,error,cap)} {
	set cap [expr $var(graph,ds,error,width)+3]
    } else {
	set cap 0
    }

    set nn $var(graph,ds,current)
    $var(graph) element configure ${nn} \
	-label $var(graph,ds,name) -hide [expr !$var(graph,ds,show)] \
	-symbol $var(graph,ds,shape,symbol) -fill $clr -scalesymbols no \
	-outline $var(graph,ds,shape,color) \
	-linewidth 0 -pixels 5 \
	-showerrorbars $show -errorbarcolor $var(graph,ds,error,color) \
	-errorbarwidth $var(graph,ds,error,width) -errorbarcap $cap

    $var(graph) pen configure active -color blue \
	-symbol $var(graph,ds,shape,symbol) \
	-linewidth 0 -pixels 5 \
	-showerrorbars $show -errorbarcolor $var(graph,ds,error,color) \
	-errorbarwidth $var(graph,ds,error,width) -errorbarcap $cap
}

proc PlotScatterButton {varname x y} {
    upvar #0 $varname var
    global $varname

    set cc $var(graph,current)

    if {[llength $var($cc,dss)] == 0} {
	return
    }

    if {$var(callback) == {}} {
	return
    }

    set rr [$var(graph) element closest $x $y]
    set elem [lindex $rr 1]
    set row [lindex $rr 3]

    if {$elem != {}} {
	if {$row != {}} {
	    $var(graph) element deactivate $elem
	    $var(graph) element activate $elem $row
	    # rows start at 1
	    eval "$var(callback) [expr $row+1]"
	} else {
	    $var(graph) element deactivate $elem
	    eval "$var(callback) {}"
	}
    }
}

proc PlotScatterHighliteElement {varname rowlist} {
    upvar #0 $varname var
    global $varname

    set cc $var(graph,current)
    set nn $var(graph,ds,current)

    if {[llength $var($cc,dss)] == 0} {
	return
    }

    if {$var(graph,ds,show)} {
	$var(graph) element deactivate $nn
	if {$rowlist != {}} {
	    # can have multiple rows
	    eval "$var(graph) element activate $nn $rowlist"
	}
    }
}
