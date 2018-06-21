%{
%}

#include font.tin
#include string.tin
#include def.tin

%start plotsend

%token AUTO_
%token AXIS_
%token AXESNUMBERS_
%token AXESTITLE_
%token BARMODE_
%token CAP_
%token COLOR_
%token DASH_
%token DATASET_
%token ERROR_
%token ERRORBAR_
%token FAMILY_
%token FILL_
%token FILLCOLOR_
%token FLIP_
%token FORMAT_
%token GRID_
%token LABELS_
%token LEGEND_
%token LEGENDTITLE_
%token LIST_
%token LOG_
%token MAX_
%token MIN_
%token MODE_
%token NUMBERS_
%token NAME_
%token POSITION_
%token RELIEF_
%token SELECT_
%token SHAPE_
%token SHOW_
%token SIZE_
%token SLANT_
%token SMOOTH_
%token STATS_
%token STATISTICS_
%token STYLE_
%token TITLE_
%token WEIGHT_
%token WIDTH_
%token XAXIS_
%token YAXIS_

%%

plotsend : {ProcessSendCmdGet iap windows}
 | {if {![PlotCmdCheck]} {plot::YYABORT}} plotCmd
 | STRING_ {if {![PlotCmdRef $1]} {plot::YYABORT}} plotCmd
 ;

xy : 'x' {set _ x}
 | 'X' {set _ x}
 | 'y' {set _ y}
 | 'Y' {set _ y}
 ;

# backward compatibility
xyaxis : XAXIS_ {set _ x}
 | YAXIS_ {set _ y}
 ;

plotCmd : STATS_ {ProcessSendCmdCVAR PlotStatsGenerate}
 # backward compatibility
 | STATISTICS_ {ProcessSendCmdCVAR PlotStatsGenerate}
 | LIST_ {ProcessSendCmdCVAR PlotListGenerate}
 | MODE_ {ProcessSendCmdCVARGet mode}
 | AXIS_ axis
 | LEGEND_ legend
 | FONT_ fontt
 | TITLE_ title
 | BARMODE_ {ProcessSendCmdCVARGet bar,mode}
 | SHOW_ {ProcessSendCmdCVARYesNo show}
 | COLOR_ {ProcessSendCmdCVARGet color}
 | FILL_ {ProcessSendCmdCVARGet fill}
 | FILLCOLOR_ {ProcessSendCmdCVARGet fill,color}
 | ERROR_ errorr
 # backward compatibility
 | ERRORBAR_ errorr
 | NAME_ {ProcessSendCmdCVARGet name}
 | SHAPE_ shape
 | RELIEF_ {ProcessSendCmdCVARGet bar,relief}
 | SMOOTH_ {ProcessSendCmdCVARGet smooth}
 | WIDTH_ {ProcessSendCmdCVARGet width}
 | DASH_ {ProcessSendCmdCVARYesNo dash}
 | SELECT_ {ProcessSendCmdCVARGet data,current}
 # backward compatibility
 | DATASET_ {ProcessSendCmdCVARGet data,current}
 ;
 
axis : xy GRID_ {ProcessSendCmdCVARYesNo "axis,$1,grid"}
 | xy LOG_ {ProcessSendCmdCVARYesNo "axis,$1,log"}
 | xy FLIP_ {ProcessSendCmdCVARYesNo "axis,$1,flip"}
 | xy AUTO_ {ProcessSendCmdCVARYesNo "axis,$1,auto"}
 | xy MIN_ {ProcessSendCmdCVARGet "axis,$1,min"}
 | xy MAX_ {ProcessSendCmdCVARGet "axis,$1,max"}
 | xy FORMAT_ {ProcessSendCmdCVARGet "axis,$1,format"}
 ;

legend : {ProcessSendCmdCVARYesNo legend}
 | POSITION_ {ProcessSendCmdCVARGet legend,position}
 ;
 
fontt : fontType FONT_ {ProcessSendCmdCVARGet "$1,family"}
# backward compatibility
 | fontType FAMILY_ {ProcessSendCmdCVARGet "$1,family"}
 | fontType FONTSIZE_ {ProcessSendCmdCVARGet "$1,size"}
 | fontType FONTWEIGHT_ {ProcessSendCmdCVARGet "$1,weight"}
 | fontType FONTSLANT_ {ProcessSendCmdCVARGet "$1,slant"}
# backward compatibility
 | fontType FONTSTYLE_ {ProcessSendCmdCVARGet "$1,weight"}
 | fontType SIZE_ {ProcessSendCmdCVARGet "$1,size"}
 | fontType WEIGHT_ {ProcessSendCmdCVARGet "$1,weight"}
 | fontType SLANT_ {ProcessSendCmdCVARGet "$1,slant"}
 | fontType STYLE_ {ProcessSendCmdCVARGet "$1,weight"}
 ;

fontType : TITLE_ {set _ graph,title}
 | LABELS_ {set _ axis,title}
 # backward compatibility
 | AXESTITLE_ {set _ axis,title}
 | NUMBERS_ {set _ axis,font}
 # backward compatibility
 | AXESNUMBERS_ {set _ axis,font}
 | LEGEND_ {set _ legend,font}
 | LEGENDTITLE_ {set _ legend,title}
 ;

title : {ProcessSendCmdCVARGet graph,title}
 | xy {ProcessSendCmdCVARGet "axis,$1,title"}
 | xyaxis {ProcessSendCmdCVARGet "axis,$1,title"}
 | LEGEND_ {ProcessSendCmdCVARGet legend,title}
 ;

errorr : {ProcessSendCmdCVARYesNo error}
 | CAP_ {ProcessSendCmdCVARYesNo error,cap}
 | COLOR_ {ProcessSendCmdCVARGet error,color}
 | WIDTH_ {ProcessSendCmdCVARGet error,width}
 ;

shape : {ProcessSendCmdCVARGet shape,symbol}
 | FILL_ {ProcessSendCmdCVARYesNo shape,fill}
 | COLOR_ {ProcessSendCmdCVARGet shape,color}
 ;

%%

proc plotsend::yyerror {msg} {
     variable yycnt
     variable yy_current_buffer
     variable index_

     ParserError $msg $yycnt $yy_current_buffer $index_
}
