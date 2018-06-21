%{
%}

#include int.tin
#include string.tin
#include def.tin

%start command

%%

command : height 
 | height {yyclearin; YYACCEPT} STRING_
 ;

height : INT_ {ProcessCmdSet canvas height $1 UpdateView}
 ;

%%

proc height::yyerror {msg} {
     variable yycnt
     variable yy_current_buffer
     variable index_

     ParserError $msg $yycnt $yy_current_buffer $index_
}
