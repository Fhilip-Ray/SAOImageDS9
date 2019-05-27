#  Copyright (C) 1999-2018
#  Smithsonian Astrophysical Observatory, Cambridge, MA, USA
#  For conditions of distribution and use, see copyright notice in "copyright"

package provide DS9 1.0

# used by backup
proc PlotBarTool {} {
    global iap

    PlotBar $iap(tt) [msgcat::mc {Bar Plot Tool}] {} {} {} 2 {}
}

proc PlotBar {tt wtt title xaxis yaxis dim data} {
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

    PlotBarDialog $varname $wtt $title $xaxis $yaxis
    
    PlotDataSet $varname $dim $data
    $var(proc,updategraph) $varname
    PlotStats $varname
    PlotList $varname
}

proc PlotBarDialog {varname wtt title xaxis yaxis} {
    upvar #0 $varname var
    global $varname

    set var(proc,addgraph) PlotBarAddGraph
    set var(proc,updategraph) PlotBarUpdateGraph
    set var(proc,updateelement) PlotBarUpdateElement
    set var(proc,highlite) PlotBarHighliteElement
    set var(proc,button) PlotBarButton

    PlotDialog $varname $wtt $title $xaxis $yaxis
    PlotAddGraph $varname

    set tt $var(graph,total)
    set cc $var(graph,current)

    # Graph
    $var(mb).graph add separator
    $var(mb).graph add cascade -label "[msgcat::mc {Mode}]..." \
	-menu $var(mb).graph.mode

    # Graph Mode
    menu $var(mb).graph.mode
    $var(mb).graph.mode add radiobutton -label [msgcat::mc {Normal}] \
	-variable ${varname}(bar,mode) -value normal \
	-command [list $var(proc,updategraph) $varname]
    $var(mb).graph.mode add radiobutton -label [msgcat::mc {Stacked}] \
	-variable ${varname}(bar,mode) -value stacked \
	-command [list $var(proc,updategraph) $varname]
    $var(mb).graph.mode add radiobutton -label [msgcat::mc {Aligned}] \
	-variable ${varname}(bar,mode) -value aligned \
	-command [list $var(proc,updategraph) $varname]
    $var(mb).graph.mode add radiobutton -label [msgcat::mc {Overlap}] \
	-variable ${varname}(bar,mode) -value overlap \
	-command [list $var(proc,updategraph) $varname]

    # Data
    $var(mb).data add checkbutton -label [msgcat::mc {Show}] \
	-variable ${varname}(graph$cc,show) \
	-command [list PlotBarUpdateElement $varname]
    $var(mb).data add separator
    $var(mb).data add cascade -label [msgcat::mc {Color}] \
	-menu $var(mb).data.color
    $var(mb).data add cascade -label [msgcat::mc {Relief}] \
	-menu $var(mb).data.relief
    $var(mb).data add cascade -label [msgcat::mc {Error}] \
	-menu $var(mb).data.error
    $var(mb).data add separator
    $var(mb).data add command -label "[msgcat::mc {Name}]..." \
	-command [list DatasetNameDialog $varname]

    PlotColorMenu $var(mb).data.color $varname color \
	[list PlotBarUpdateElement $varname]

    # Relief
    menu $var(mb).data.relief
    $var(mb).data.relief add radiobutton -label [msgcat::mc {Flat}] \
	-variable ${varname}(bar,relief) -value flat \
	-command [list PlotBarUpdateElement $varname]
    $var(mb).data.relief add radiobutton -label [msgcat::mc {Sunken}] \
	-variable ${varname}(bar,relief) -value sunken \
	-command [list PlotBarUpdateElement $varname]
    $var(mb).data.relief add radiobutton -label [msgcat::mc {Raised}] \
	-variable ${varname}(bar,relief) -value raised \
	-command [list PlotBarUpdateElement $varname]
    $var(mb).data.relief add radiobutton -label [msgcat::mc {Solid}] \
	-variable ${varname}(bar,relief) -value solid \
	-command [list PlotBarUpdateElement $varname]
    $var(mb).data.relief add radiobutton -label [msgcat::mc {Groove}] \
	-variable ${varname}(bar,relief) -value groove \
	-command [list PlotBarUpdateElement $varname]

    # Error
    menu $var(mb).data.error
    $var(mb).data.error add checkbutton -label [msgcat::mc {Show}] \
	-variable ${varname}(error) \
	-command [list PlotBarUpdateElement $varname]
    $var(mb).data.error add checkbutton -label [msgcat::mc {Cap}] \
	-variable ${varname}(error,cap) \
	-command [list PlotBarUpdateElement $varname]
    $var(mb).data.error add separator
    $var(mb).data.error add cascade -label [msgcat::mc {Color}] \
	-menu $var(mb).data.error.color
    $var(mb).data.error add cascade -label [msgcat::mc {Width}] \
	-menu $var(mb).data.error.width

    PlotColorMenu $var(mb).data.error.color $varname error,color \
	[list PlotBarUpdateElement $varname]
    WidthDashMenu $var(mb).data.error.width $varname error,width {} \
	[list PlotBarUpdateElement $varname] {}
}

proc PlotBarAddGraph {varname} {
    upvar #0 $varname var
    global $varname

    set cc $var(graph,current)

    set var(type$cc) bar
    set var(graph$cc) [blt::barchart $var(canvas).gr$cc \
			   -width 600 \
			   -height 500 \
			   -highlightthickness 0 \
			  ]

    $var(graph$cc) xaxis configure -grid no -stepsize 0
    $var(graph$cc) yaxis configure -grid yes
}

proc PlotBarUpdateGraph {varname} {
    upvar #0 $varname var
    global $varname

    PlotUpdateGraph $varname

    set tt $var(graph,total)
    set cc $var(graph,current)

    for {set ii 1} {$ii<=$tt} {incr ii} {
	$var(graph$ii) configure -barmode $var(bar,mode)
    }
}

proc PlotBarUpdateElement {varname} {
    upvar #0 $varname var
    global $varname

    set tt $var(graph,total)
    set cc $var(graph,current)

    # warning: uses current vars
    if {$var(graph$cc,data,total) == 0} {
 	return
    }
    
    set nn $var(graph$cc,data,current)
    PlotGetVar $varname $nn

    if {$var(error)} {
	set show both
    } else {
	set show none
    }

    if {$var(error,cap)} {
	set cap [expr $var(error,width)+3]
    } else {
	set cap 0
    }

    $var(graph$cc) element configure "d-${nn}" \
	-label $var(graph$cc,name) -hide [expr !$var(graph$cc,show)] \
	-relief $var(bar,relief) -color $var(color) \
	-showerrorbars $show -errorbarcolor $var(error,color) \
	-errorbarwidth $var(error,width) -errorbarcap $cap
}

proc PlotBarButton {varname x y} {
    upvar #0 $varname var
    global $varname
}

proc PlotBarHighliteElement {varname rowlist} {
    upvar #0 $varname var
    global $varname
}
