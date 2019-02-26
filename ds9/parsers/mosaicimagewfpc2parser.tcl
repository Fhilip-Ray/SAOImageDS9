package provide DS9 1.0

######
# Begin autogenerated taccle (version 1.3) routines.
# Although taccle itself is protected by the GNU Public License (GPL)
# all user-supplied functions are protected by their respective
# author's license.  See http://mini.net/tcl/taccle for other details.
######

namespace eval mosaicimagewfpc2 {
    variable yylval {}
    variable table
    variable rules
    variable token {}
    variable yycnt 0
    variable yyerr 0
    variable save_state 0

    namespace export yylex
}

proc mosaicimagewfpc2::YYABORT {} {
    return -code return 1
}

proc mosaicimagewfpc2::YYACCEPT {} {
    return -code return 0
}

proc mosaicimagewfpc2::YYERROR {} {
    variable yyerr
    set yyerr 1
}

proc mosaicimagewfpc2::yyclearin {} {
    variable token
    variable yycnt
    set token {}
    incr yycnt -1
}

proc mosaicimagewfpc2::yyerror {s} {
    puts stderr $s
}

proc mosaicimagewfpc2::setupvalues {stack pointer numsyms} {
    upvar 1 1 y
    set y {}
    for {set i 1} {$i <= $numsyms} {incr i} {
        upvar 1 $i y
        set y [lindex $stack $pointer]
        incr pointer
    }
}

proc mosaicimagewfpc2::unsetupvalues {numsyms} {
    for {set i 1} {$i <= $numsyms} {incr i} {
        upvar 1 $i y
        unset y
    }
}

array set mosaicimagewfpc2::table {
  6:0 reduce
  3:0,target 0
  0:257 reduce
  1:257 reduce
  0:258 shift
  5:0,target 2
  2:257 reduce
  0:260 goto
  0:259 shift
  0:261 goto
  1:257,target 6
  0:258,target 1
  0:262 goto
  5:257 shift
  0:0,target 4
  0:261,target 4
  2:0,target 5
  5:257,target 6
  4:0,target 1
  0:0 reduce
  6:0,target 3
  1:0 reduce
  0:257,target 4
  2:0 reduce
  3:0 accept
  2:257,target 5
  0:259,target 2
  0:260,target 3
  4:0 reduce
  1:0,target 6
  5:0 reduce
  0:262,target 5
}

array set mosaicimagewfpc2::rules {
  0,l 263
  1,l 260
  2,l 261
  3,l 261
  4,l 262
  5,l 262
  6,l 262
}

array set mosaicimagewfpc2::rules {
  5,dc 1
  0,dc 1
  2,dc 1
  4,dc 0
  6,dc 1
  1,dc 1
  3,dc 2
}

array set mosaicimagewfpc2::rules {
  5,line 26
  2,line 21
  4,line 25
  6,line 27
  1,line 18
  3,line 22
}

array set mosaicimagewfpc2::lr1_table {
  0 {{0 0 0} {1 0 0} {2 0 0} {3 0 0} {4 {0 257} 0} {5 {0 257} 0} {6 {0 257} 0}}
  1 {{6 {0 257} 1}}
  2 {{5 {0 257} 1}}
  3 {{0 0 1}}
  4 {{1 0 1}}
  0,trans {{258 1} {259 2} {260 3} {261 4} {262 5}}
  5 {{2 0 1} {3 0 1}}
  1,trans {}
  2,trans {}
  6 {{3 0 2}}
  3,trans {}
  4,trans {}
  5,trans {{257 6}}
  6,trans {}
}

array set mosaicimagewfpc2::token_id_table {
  262,title {}
  0,t 0
  0 {$}
  263,title {}
  error,t 0
  error error
  258,line 11
  261,line 20
  error,line 15
  257 STRING_
  257,t 0
  263,line 28
  258 MASK_
  258,t 0
  260,t 1
  260 command
  error,title {}
  259 NEW_
  259,t 0
  261,t 1
  261 mosaicimagewfpc2
  262,t 1
  262 opts
  257,line 7
  263,t 1
  263 start'
  260,line 17
  257,title string
  259,line 12
  258,title MASK
  262,line 24
  260,title {}
  259,title NEW
  261,title {}
}

proc mosaicimagewfpc2::yyparse {} {
    variable yylval
    variable table
    variable rules
    variable token
    variable yycnt
    variable lr1_table
    variable token_id_table
    variable yyerr
    variable save_state

    set yycnt 0
    set state_stack {0}
    set value_stack {{}}
    set token ""
    set accepted 0
    set yyerr 0
    set save_state 0

    while {$accepted == 0} {
        set state [lindex $state_stack end]
        if {$token == ""} {
            set yylval ""
            set token [yylex]
            set buflval $yylval
	    if {$token>0} {
	        incr yycnt
            }
        }
        if {![info exists table($state:$token)] || $yyerr} {
	    if {!$yyerr} {
	        set save_state $state
	    }
            # pop off states until error token accepted
            while {[llength $state_stack] > 0 && \
                       ![info exists table($state:error)]} {
                set state_stack [lrange $state_stack 0 end-1]
                set value_stack [lrange $value_stack 0 \
                                       [expr {[llength $state_stack] - 1}]]
                set state [lindex $state_stack end]
            }
            if {[llength $state_stack] == 0} {
 
	        set rr { }
                if {[info exists lr1_table($save_state,trans)] && [llength $lr1_table($save_state,trans)] >= 1} {
                    foreach trans $lr1_table($save_state,trans) {
                        foreach {tok_id nextstate} $trans {
			    set ss $token_id_table($tok_id,title)
			    if {$ss != {}} {
			        append rr "$ss, "
                            }
                        }
                    }
                }
		set rr [string trimleft $rr { }]
		set rr [string trimright $rr {, }]
                yyerror "parse error, expecting: $rr"


                return 1
            }
            lappend state_stack [set state $table($state:error,target)]
            lappend value_stack {}
            # consume tokens until it finds an acceptable one
            while {![info exists table($state:$token)]} {
                if {$token == 0} {
                    yyerror "end of file while recovering from error"
                    return 1
                }
                set yylval {}
                set token [yylex]
                set buflval $yylval
            }
            continue
        }
        switch -- $table($state:$token) {
            shift {
                lappend state_stack $table($state:$token,target)
                lappend value_stack $buflval
                set token ""
            }
            reduce {
                set rule $table($state:$token,target)
                set ll $rules($rule,l)
                if {[info exists rules($rule,e)]} {
                    set dc $rules($rule,e)
                } else {
                    set dc $rules($rule,dc)
                }
                set stackpointer [expr {[llength $state_stack]-$dc}]
                setupvalues $value_stack $stackpointer $dc
                set _ $1
                set yylval [lindex $value_stack end]
                switch -- $rule {
                    2 { MosaicImageWFPC2CmdLoad {} $1 }
                    3 { MosaicImageWFPC2CmdLoad $2 $1 }
                    5 { CreateFrame; set _ {} }
                    6 { set _ mask }
                }
                unsetupvalues $dc
                # pop off tokens from the stack if normal rule
                if {![info exists rules($rule,e)]} {
                    incr stackpointer -1
                    set state_stack [lrange $state_stack 0 $stackpointer]
                    set value_stack [lrange $value_stack 0 $stackpointer]
                }
                # now do the goto transition
                lappend state_stack $table([lindex $state_stack end]:$ll,target)
                lappend value_stack $_
            }
            accept {
                set accepted 1
            }
            goto -
            default {
                puts stderr "Internal parser error: illegal command $table($state:$token)"
                return 2
            }
        }
    }
    return 0
}

######
# end autogenerated taccle functions
######

proc mosaicimagewfpc2::yyerror {msg} {
     variable yycnt
     variable yy_current_buffer
     variable index_

     ParserError $msg $yycnt $yy_current_buffer $index_
}