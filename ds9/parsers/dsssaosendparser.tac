%{
%}

#include imgsvr.tin
#include string.tin

%start dsssaosend

%%

dsssaosend : {ProcessSendCmdGet dsao name}
 | NAME_ {ProcessSendCmdGet dsao name}
 | SAVE_ {ProcessSendCmdYesNo dsao save}
 | FRAME_ {ProcessSendCmdGet dsao mode}
 | SURVEY_ {ProcessSendCmdGet dsao survey}
 | SIZE_ {ProcessSendCmdGet3 dsao width height rformat}
 | COORD_ {ProcessSendCmdGet3 dsao x y skyformat}
 ;
 
%%

proc dsssaosend::yyerror {msg} {
     variable yycnt
     variable yy_current_buffer
     variable index_
     
     ParserError $msg $yycnt $yy_current_buffer $index_
}
