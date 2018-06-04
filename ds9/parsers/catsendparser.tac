%{
%}

#include string.tin

%token HEADER_

%start catsend

%%

catsend : {if {![CatalogCmdCheck]} {cat::YYABORT}} catsendCmd
 | STRING_ {if {![CatalogSendCmdRef cat${1}]} {plot::YYABORT}} catsendCmd
 ;

catsendCmd : {ProcessSendCmdGet icat cats}
 | HEADER_ {global cvarname; ProcessSendCmdResult {.txt} [CATGetHeader $cvarname]}
 ; 

%%

proc catsend::yyerror {msg} {
     variable yycnt
     variable yy_current_buffer
     variable index_

     ParserError $msg $yycnt $yy_current_buffer $index_
}
