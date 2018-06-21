%{
%}

#include yesno.tin
#include string.tin
#include def.tin

%start command

%%

#include yesno.trl

command : iconify 
 | iconify {yyclearin; YYACCEPT} STRING_
 ;

iconify : yesno {IconifyCmd $1}
 ;

%%

proc iconify::yyerror {msg} {
     variable yycnt
     variable yy_current_buffer
     variable index_

     ParserError $msg $yycnt $yy_current_buffer $index_
}
