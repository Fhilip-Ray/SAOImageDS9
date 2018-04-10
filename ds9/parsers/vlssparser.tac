%{
%}

#include yesno.tin
#include imgsvr.tin
#include numeric.tin
#include string.tin

%start command

%%

#include yesno.trl
#include imgsvr.trl
#include numeric.trl

command : vlss
 | vlss {yyclearin; YYACCEPT} STRING_
 ;

vlss : {IMGSVRApply dvlss 1}
 | OPEN_ {}
 | CLOSE_ {ARDestroy dvlss}
 | STRING_ {IMGSVRCmd dvlss name $1}
 | NAME_ STRING_ {IMGSVRCmd dvlss name $2}
 | SIZE_ numeric numeric sizeOpt {IMGSVRCmdSize dvlss $2 $3 $4}
 | SAVE_ yesno {IMGSVRCmd dvlss save $2}
 | FRAME_ frame {IMGSVRCmd dvlss mode $2}
 | UPDATE_ update

 | numeric numeric coordOpt {IMGSVRCmdCoord dvlss $1 $2 degrees}
 | SEXSTR_ SEXSTR_ coordOpt {IMGSVRCmdCoord dvlss $1 $2 sexagesimal}
 | COORD_ numeric numeric deg {IMGSVRCmdCoord dvlss $2 $3 $4}
 | COORD_ SEXSTR_ SEXSTR_ sex {IMGSVRCmdCoord dvlss $2 $3 $4}
 ;

update : FRAME_ {IMGSVRCmdUpdate dvlss}
 | CROSSHAIR_ {IMGSVRCmdCrosshair dvlss}
 ;

%%

proc vlss::yyerror {msg} {
     variable yycnt
     variable yy_current_buffer
     variable index_
     
     ParserError $msg $yycnt $yy_current_buffer $index_
}
