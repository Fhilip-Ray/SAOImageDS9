#  Copyright (C) 1999-2018
#  Smithsonian Astrophysical Observatory, Cambridge, MA, USA
#  For conditions of distribution and use, see copyright notice in "copyright"

package provide DS9 1.0

proc PrefsDialogPlot {} {
    global dprefs

    set w $dprefs(tab)

    $dprefs(list) insert end [msgcat::mc {Plot}]
    lappend dprefs(tabs) [ttk::frame $w.plot]

    # Graph
    set f [ttk::labelframe $w.plot.graph -text [msgcat::mc {Graph}]]
    ttk::label $f.tbg -text [msgcat::mc {Background}]
    ColorMenuButton $f.bg pap graph,bg {}

    grid $f.tbg $f.bg -padx 2 -pady 2 -sticky w

    # Grid
    set f [ttk::labelframe $w.plot.grid -text [msgcat::mc {Grid}]]
    ttk::label $f.ttitle -text [msgcat::mc {Title}]
    FontMenuButton $f.title pap graph,title,family graph,title,size graph,title,weight graph,title,slant {}

    grid $f.ttitle $f.title -padx 2 -pady 2 -sticky w

    # Axis
    set f [ttk::labelframe $w.plot.axis -text [msgcat::mc {Axis}]]

    ttk::label $f.xtitle -text [msgcat::mc {X}]
    ttk::checkbutton $f.x -text [msgcat::mc {Grid}] -variable pap(axis,x,grid)
    ttk::radiobutton $f.xlinear -text [msgcat::mc {Linear}] \
	-variable pap(axis,x,log) -value 0
    ttk::radiobutton $f.xlog -text [msgcat::mc {Log}] \
	-variable pap(axis,x,log) -value 1

    ttk::label $f.ytitle -text [msgcat::mc {Y}]
    ttk::checkbutton $f.y -text [msgcat::mc {Grid}] -variable pap(axis,y,grid)
    ttk::radiobutton $f.ylinear -text [msgcat::mc {Linear}] \
	-variable pap(axis,y,log) -value 0
    ttk::radiobutton $f.ylog -text [msgcat::mc {Log}] \
	-variable pap(axis,y,log) -value 1

    ttk::label $f.ttextlab -text [msgcat::mc {Axis Title}]
    FontMenuButton $f.textlab pap axis,title,family axis,title,size axis,title,weight axis,title,slant {}
    ttk::label $f.tnumlab -text [msgcat::mc {Axis Numbers}]
    FontMenuButton $f.numlab pap axis,font,family axis,font,size axis,font,weight axis,font,slant {}

    grid $f.xtitle $f.x $f.xlinear $f.xlog -padx 2 -pady 2 -sticky w
    grid $f.ytitle $f.y $f.ylinear $f.ylog -padx 2 -pady 2 -sticky w
    grid $f.ttextlab $f.textlab  -padx 2 -pady 2 -sticky w
    grid $f.tnumlab $f.numlab -padx 2 -pady 2 -sticky w

    # Dataset
    set f [ttk::labelframe $w.plot.dataset -text [msgcat::mc {Dataset}]]

    #  Show
    ttk::checkbutton $f.show -text [msgcat::mc {Show}] -variable pap(show)
    grid $f.show -padx 2 -pady 2 -sticky w

    #  Shape
    ttk::label $f.shapetitle -text [msgcat::mc {Shape}]
    ttk::menubutton $f.shape -textvariable pap(shape,symbol) \
	-menu $f.shape.menu
    PlotLineShapeMenu $f.shape.menu pap(shape,symbol)
    ttk::checkbutton $f.shapefill -text [msgcat::mc {Fill}] \
	-variable pap(shape,fill)
    ColorMenuButton $f.shapecolor pap shape,color {}
    grid $f.shapetitle $f.shape $f.shapefill $f.shapecolor \
	-padx 2 -pady 2 -sticky w

    #  Smooth
    ttk::label $f.smoothtitle -text [msgcat::mc {Smooth}]
    ttk::menubutton $f.smooth -textvariable pap(smooth) \
	-menu $f.smooth.menu
    PlotLineSmoothMenu $f.smooth.menu pap(smooth)
    grid $f.smoothtitle $f.smooth -padx 2 -pady 2 -sticky w

    #  Color
    ttk::label $f.colortitle -text [msgcat::mc {Color}]
    ColorMenuButton $f.color pap color {}
    grid $f.colortitle $f.color -padx 2 -pady 2 -sticky w

    #  Width
    ttk::label $f.widthtitle -text [msgcat::mc {Width}]
    ttk::menubutton $f.width -textvariable pap(width) -menu $f.width.menu
    WidthDashMenu $f.width.menu pap width dash {} {}
    grid $f.widthtitle $f.width -padx 2 -pady 2 -sticky w

    #  Error
    ttk::label $f.errortitle -text [msgcat::mc {Error}]
    ttk::checkbutton $f.error -text [msgcat::mc {Show}] \
	-variable pap(error)
    ttk::checkbutton $f.errorcap -text [msgcat::mc {Cap}] \
	-variable pap(error,cap)
    ColorMenuButton $f.errorcolor pap error,color {}
    ttk::menubutton $f.errorwidth -textvariable pap(error,width) \
	-menu $f.errorwidth.menu
    WidthDashMenu $f.errorwidth.menu pap width dash {} {}
    grid $f.errortitle $f.error $f.errorcap $f.errorcolor $f.errorwidth \
	-padx 2 -pady 2 -sticky w

    pack $w.plot.graph $w.plot.grid $w.plot.axis $w.plot.dataset \
	-side top -fill both -expand true
}

proc ProcessPlotCmd {xarname iname buf fn} {
    upvar $xarname xar
    upvar $iname i

    global iap
    global parse
    set parse(buf) $buf
    set parse(fn) $fn
    set parse(tt) $iap(tt)

    set ref [lindex $iap(windows) end]
    global cvarname
    set cvarname $ref

    plot::YY_FLUSH_BUFFER
    plot::yy_scan_string [lrange $xar $i end]
    plot::yyparse
    incr i [expr $plot::yycnt-1]
}

proc PlotCmdCheck {} {
    global cvarname
    upvar #0 $cvarname cvar

    if {![info exists cvar(top)]} {
	Error "[msgcat::mc {Unable to find plot window}] $cvarname"
	return 0
    }
    if {![winfo exists $cvar(top)]} {
	Error "[msgcat::mc {Unable to find plot window}] $cvarname"
	return 0
    }
    return 1
}

proc PlotCmdRef {ref} {
    global iap
    global cvarname

    # look for reference in current list
    if {[lsearch $iap(windows) $ref] < 0} {
	Error "[msgcat::mc {Unable to find plot window}] $ref"
	return 0
    }

    set cvarname $ref
    return [PlotCmdCheck]
}

proc PlotCmdNew {name} {
    global parse

    if {$name != {}} {
	set parse(tt) $name
    }

    if {$parse(buf) != {}} {
	return
    } elseif {$parse(fn) != {}} {
	if {[file exists $parse(fn)]} {
	    set ch [open $parse(fn) r]
	    set parse(buf) [read $ch]
	    close $ch
	    return
	}
    }
    set parse(buf) {}
}

proc PlotCmdLine {title xaxis yaxis dim} {
    global parse
    PlotLine $parse(tt) {} $title $xaxis $yaxis $dim $parse(buf)
}

proc PlotCmdBar {title xaxis yaxis dim} {
    global parse
    PlotBar $parse(tt) {} $title $xaxis $yaxis $dim $parse(buf)
}

proc PlotCmdScatter {title xaxis yaxis dim} {
    global parse
    PlotScatter $parse(tt) {} $title $xaxis $yaxis $dim $parse(buf)
}

proc PlotCmdAnalysisPlotStdin {which} {
    global parse
    AnalysisPlotStdin $which $parse(tt) {} $parse(buf)
}

proc PlotCmdData {dim} {
    global parse
    global cvarname
    upvar #0 $cvarname cvar

    if {$parse(buf) == {}} {
	if {$parse(fn) != {}} {
	    if {[file exists $parse(fn)]} {
		set ch [open $parse(fn) r]
		set parse(buf) [read $ch]
		close $ch
	    }
	}
	if {$parse(buf) == {}} {
	    Error "[msgcat::mc {Unable to load plot data}] $fn"
	}
    }
    
    PlotRaise $cvarname
    PlotDataSet $cvarname $dim $parse(buf)
    $cvar(proc,updategraph) $cvarname
    PlotStats $cvarname
    PlotList $cvarname
}

proc PlotCmdLoad {fn dim} {
    global cvarname
    
    if {$fn != {}} {
	PlotLoadDataFile $cvarname $fn $dim
	FileLast apdatafbox $fn
    }
}

proc PlotCmdSave {fn} {
    global cvarname
    
    if {$fn != {}} {
	PlotSaveDataFile $cvarname $fn
	FileLast apdatafbox $fn
    }
}

proc PlotCmdLoadConfig {fn} {
    global cvarname
    
    if {$fn != {}} {
	PlotLoadConfigFile $cvarname $fn
	FileLast apconfigfbox $fn
    }
}

proc PlotCmdSaveConfig {fn} {
    global cvarname
    
    if {$fn != {}} {
	PlotSaveConfigFile $cvarname $fn
	FileLast apconfigfbox $fn
    }
}

proc PlotCmdUpdateGraph {which value} {
    global cvarname
    upvar #0 $cvarname cvar

    set cvar($which) $value
    $cvar(proc,updategraph) $cvarname
}

proc PlotCmdUpdateElement {which value} {
    global cvarname
    upvar #0 $cvarname cvar

    set cvar($which) $value
    $cvar(proc,updateelement) $cvarname
}

proc PlotCmdFontStyle {which value} {
    global cvarname
    upvar #0 $cvarname cvar

    switch $value {
	normal {
	    set cvar($which,weight) normal
	    set cvar($which,slant) roman
	}
	bold {
	    set cvar($which,weight) bold
	    set cvar($which,slant) roman
	}
	italic {
	    set cvar($which,weight) normal
	    set cvar($which,slant) italic
	}
    }

    $cvar(proc,updategraph) $cvarname
}

proc ProcessSendPlotCmd {proc id param {sock {}} {fn {}}} {
    global iap
    global parse
    set parse(proc) $proc
    set parse(id) $id

    set ref [lindex $iap(windows) end]
    global cvarname
    set cvarname $ref
    global parse

    plotsend::YY_FLUSH_BUFFER
    plotsend::yy_scan_string $param
    plotsend::yyparse
}
