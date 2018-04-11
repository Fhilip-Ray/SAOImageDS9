%{
%}

#include yesno.tin
#include coords.tin
#include numeric.tin
#include string.tin

%start command

%token ALIGN_
%token APPEND_
%token CLOSE_
%token OPEN_
%token REPLACE_
%token RESET_
%token SKY_
%token SKYFORMAT_
%token SYSTEM_

%%

#include yesno.trl
#include coords.trl
#include numeric.trl

command : wcs 
 | wcs {yyclearin; YYACCEPT} STRING_
 ;

wcs : OPEN_ {WCSDialog}
 | CLOSE_ {WCSDestroyDialog}
 | wcssys {WCSCmdSet system $1 UpdateWCS}
 | SYSTEM_ wcssys {WCSCmdSet system $2 UpdateWCS}
 | skyframe {WCSCmdSet sky $1 UpdateWCS}
 | SKY_ skyframe {WCSCmdSet sky $2 UpdateWCS}
 | skyformat {WCSCmdSet skyformat $1 UpdateWCS}
 | SKYFORMAT_ skyformat {WCSCmdSet skyformat $2 UpdateWCS}
 | ALIGN_ yesno {CurrentCmdSet align $2 AlignWCSFrame}
 | RESET_ {WCSCmdReset 1}
 | RESET_ INT_ {WCSCmdReset $2}
 | REPLACE_ replace
 | APPEND_ append
 ;

replace : {WCSCmdLoad replace 1}
 | INT_ {WCSCmdLoad replace $1}
 | STRING_ {WCSCmdLoadFn replace 1 $1}
 | INT_ STRING_ {WCSCmdLoadFn replace $1 $2}
 ;
 
append : {WCSCmdLoad append 1}
 | INT_ {WCSCmdLoad append $1}
 | STRING_ {WCSCmdLoadFn append 1 $1}
 | INT_ STRING_ {WCSCmdLoadFn append $1 $2}
 ;

%%

proc wcs::yyerror {msg} {
     variable yycnt
     variable yy_current_buffer
     variable index_

     ParserError $msg $yycnt $yy_current_buffer $index_
}
