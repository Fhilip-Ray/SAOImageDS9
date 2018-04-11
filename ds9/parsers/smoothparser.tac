%{
%}

#include yesno.tin
#include numeric.tin
#include string.tin

%start command

%token ANGLE_
%token BOXCAR_
%token CLOSE_
%token ELLIPTIC_
%token FUNCTION_
%token GAUSSIAN_
%token LOCK_
%token MATCH_
%token OPEN_
%token RADIUS_
%token RADIUSMINOR_
%token SIGMA_
%token SIGMAMINOR_
%token TOPHAT_

%%

#include yesno.trl
#include numeric.trl

command : smooth 
 | smooth {yyclearin; YYACCEPT} STRING_
 ;


smooth : yesno {SmoothCmdSet view $1 SmoothUpdate}
 | OPEN_ {SmoothDialog}
 | CLOSE_ {SmoothDestroyDialog}
 | MATCH_ {MatchSmoothCurrent}
 | LOCK_ yesno {SmoothCmdSet lock $2 LockSmoothCurrent}
 | FUNCTION_ function {SmoothCmdSet function $2 SmoothUpdate}
 | RADIUS_ INT_ {SmoothCmdSet radius $2 SmoothUpdate}
 | RADIUSMINOR_ INT_ {SmoothCmdSet radius,minor $2 SmoothUpdate}
 | SIGMA_ numeric {SmoothCmdSet sigma $2 SmoothUpdate}
 | SIGMAMINOR_ numeric {SmoothCmdSet sigma,minor $2 SmoothUpdate}
 | ANGLE_ numeric {SmoothCmdSet angle $2 SmoothUpdate}
 ;

function : BOXCAR_ {set _ boxcar}
 | ELLIPTIC_ {set _ elliptic}
 | TOPHAT_ {set _ tophat}
 | GAUSSIAN_ {set _ gaussian}
 ;
 
%%

proc smooth::yyerror {msg} {
     variable yycnt
     variable yy_current_buffer
     variable index_

     ParserError $msg $yycnt $yy_current_buffer $index_
}
