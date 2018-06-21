%{
%}

#include yesno.tin
#include string.tin
#include def.tin

%start command

%token PAN_
%token REGIONS_

%%

#include yesno.trl

command : preserve 
 | preserve {yyclearin; YYACCEPT} STRING_
 ;

preserve : PAN_ yesno {ProcessCmdSet panzoom preserve $2 PreservePan}
 | REGIONS_ yesno {ProcessCmdSet marker preserve $2 MarkerPreserve}
 ;

%%

proc preserve::yyerror {msg} {
     variable yycnt
     variable yy_current_buffer
     variable index_

     ParserError $msg $yycnt $yy_current_buffer $index_
}
