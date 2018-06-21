%{
%}

#include yesno.tin
#include numeric.tin
#include string.tin
#include def.tin

%start command

%token CONTRAST_
%token SAMPLE_
%token LINE_

%%

#include yesno.trl
#include numeric.trl

command : zscale
 | zscale {yyclearin; YYACCEPT} STRING_
 ;

zscale : yesno {ProcessCmdSet scale mode zscale ChangeScaleMode}
 | CONTRAST_ numeric {ProcessCmdSet zscale contrast $2 ChangeZScale}
 | SAMPLE_ INT_ {ProcessCmdSet zscale sample $2 ChangeZScale}
 | LINE_ INT_ {ProcessCmdSet zscale line $2 ChangeZScale}
 ;

%%

proc zscale::yyerror {msg} {
     variable yycnt
     variable yy_current_buffer
     variable index_

     ParserError $msg $yycnt $yy_current_buffer $index_
}
