%{
%}

#include base.tin
#include coords.tin
#include yesno.tin

%start command

%token CLOSE_
%token COORD_
%token CROSSHAIR_
%token CURRENT_
%token FRAME_
%token NAME_
%token NEW_
%token OPEN_
%token UPDATE_
%token SAVE_
%token SIZE_
%token SURVEY_

%%

#include base.trl
#include coords.trl
#include yesno.trl

command : 2mass
 | 2mass {yyclearin; YYACCEPT} STRING_
 ;

deg : {set _ degrees}
 | DEGREES_ {set _ degrees}
 ;

sex : {set _ sexagesimal}
 | SEXAGESIMAL_ {set _ sexagesimal}
 ;

2mass : {IMGSVRApply dtwomass 1}
 | OPEN_ {}
 | CLOSE_ {ARDestroy dtwomass}
 | STRING_ {global dtwomass; set dtwomass(name) $1; IMGSVRApply dtwomass 1}
 | NAME_ STRING_ {global dtwomass; set dtwomass(name) $2; IMGSVRApply dtwomass 1}
 | COORD_ numeric numeric deg {global dtwomass; set dtwomass(x) $2; set dtwomass(y) $3; set dtwomass(skyformat) $4; set dtwomass(skyformat,msg) $4; IMGSVRApply dtwomass 1}
 | COORD_ SEXSTR_ SEXSTR_ sex {global dtwomass; set dtwomass(x) $2; set dtwomass(y) $3; set dtwomass(skyformat) $4; set dtwomass(skyformat,msg) $4; IMGSVRApply dtwomass 1}
 | SIZE_ numeric numeric skyformat {global dtwomass; set dtwomass(width) $2; set dtwomass(height) $3; set dtwomass(rformat) $4; set dtwomass(rformat,msg) $4}
 | SAVE_ yesno {global dtwomass; set dtwomass(save) $2}
 | FRAME_ frame {global dtwomass; set dtwomass(mode) $2}
 | UPDATE_ FRAME_ {IMGSVRUpdate dtwomass; IMGSVRApply dtwomass 1}
 | UPDATE_ CROSSHAIR_ {IMGSVRCrosshair dtwomass; IMGSVRApply dtwomass 1}
 | SURVEY_ survey {global dtwomass; set dtwomass(survey) $2}
 ;

frame : NEW_ {set _ new}
 | CURRENT_ {set _ current}
 ;

survey : 'j' {set _ $1}
 | 'h' {set _ $1}
 | 'k' {set _ $1}
 ;
