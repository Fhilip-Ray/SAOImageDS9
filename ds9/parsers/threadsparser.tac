%{
%}

#include numeric.tin
#include string.tin

%start command

%%

#include numeric.trl

command : threads 
 | threads {yyclearin; YYACCEPT} STRING_
 ;

threads : INT_ {ProcessCmdSet ds9 threads $1 ChangeThreads}
 ;

%%

proc threads::yyerror {msg} {
     variable yycnt
     variable yy_current_buffer
     variable index_

     ParserError $msg $yycnt $yy_current_buffer $index_
}
