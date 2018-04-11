%{
%}

#include yesno.tin
#include numeric.tin
#include string.tin

%start command

%token CLOSE_
%token CONNECT_
%token DELAY_
%token DISCONNECT_
%token INTERNAL_
%token METHOD_
%token MIME_
%token OPEN_
%token SERVER_
%token XPA_

%%

#include yesno.trl
#include numeric.trl

command : vo 
 | vo {yyclearin; YYACCEPT} STRING_
 ;

vo : OPEN_ {VODialog}
 | CLOSE_ {VODestroy voi}
 | METHOD_ method {VOCmdSet method $2}
 | SERVER_ STRING_ {VOCmdSet server $2}
 | INTERNAL_ yesno {VOCmdSet hv $2}
 | DELAY_ INT_ {VOCmdSet delay $2}
 | CONNECT_ STRING_ {VOCmdConnect $2}
 | DISCONNECT_ STRING_ {VOCmdDisconnect $2}
 | STRING_ {VOCmdConnect $1}
 ;

method : XPA_ {set _ xpa}
 | MIME_ {set _ mime}
 ;

%%

proc vo::yyerror {msg} {
     variable yycnt
     variable yy_current_buffer
     variable index_

     ParserError $msg $yycnt $yy_current_buffer $index_
}
