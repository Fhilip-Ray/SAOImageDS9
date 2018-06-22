%{
%}
#include def.tin

#include string.tin

%start catsend

%token HEADER_

%%

catsend : {if {![CatalogCmdCheck]} {catsend::YYABORT}} catsendCmd
 | STRING_ {if {![CatalogSendCmdRef cat${1}]} {catsend::YYABORT}} catsendCmd
 ;

catsendCmd : {ProcessSendCmdGet icat cats}
 | HEADER_ {CatalogSendCmdHeader}
 ; 

%%

proc catsend::yyerror {msg} {
     variable yycnt
     variable yy_current_buffer
     variable index_

     ParserError $msg $yycnt $yy_current_buffer $index_
}
