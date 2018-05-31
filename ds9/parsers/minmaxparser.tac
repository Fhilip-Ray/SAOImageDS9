%{
%}

#include numeric.tin
#include string.tin

%start command

%token AUTO_
%token DATAMIN_
%token IRAFMIN_
%token INTERVAL_
%token MODE_
%token SAMPLE_
%token SCAN_

%%

#include numeric.trl

command : minmax 
 | minmax {yyclearin; YYACCEPT} STRING_
 ;

minmax : {ProcessCmdSet scale mode minmax ChangeScaleMode}
 | mode {ProcessCmdSet minmax mode $1 ChangeMinMax}
 | MODE_ mode {ProcessCmdSet minmax mode $2 ChangeMinMax}
 | INTERVAL_ INT_ {ProcessCmdSet minmax sample $2 ChangeMinMax}
 ;

mode : SCAN_ {set _ scan}
 | SAMPLE_ {set _ sample}
 | DATAMIN_ {set _ datamin}
 | IRAFMIN_ {set _ irafmin}
# backward compatibility
 | AUTO_ {set _ scan}
 ;

%%

proc minmax::yyerror {msg} {
     variable yycnt
     variable yy_current_buffer
     variable index_

     ParserError $msg $yycnt $yy_current_buffer $index_
}
