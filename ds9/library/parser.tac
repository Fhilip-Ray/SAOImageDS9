%{
global file
set file(type) fits
set file(mode) {}
set file(layer) {}
set file(mosaic) wcs
set file(load) 0
%}

%token INT_
%token REAL_
%token STRING_
%token SEXSTR_
%token HMSSTR_
%token DMSSTR_

%token 2MASSCMD_
%token 3DCMD_
%token ALIGNCMD_
%token ASINHCMD_
%token BINCMD_
%token BGCMD_
%token BLOCKCMD_
%token BLUECMD_
%token BLINKCMD_
%token CDCMD_
%token CONSOLECMD_
%token CROPCMD_
%token CROSSHAIRCMD_
%token CUBECMD_
%token CURSORCMD_
%token GREENCMD_
%token FITSCMD_
%token FRAMECMD_
%token HEIGHTCMD_
%token HELPCMD_
%token HISTEQUCMD_
%token ICONIFYCMD_
%token IRAFALIGNCMD_
%token LINEARCMD_
%token LOGCMD_
%token LOWERCMD_
%token MINMAXCMD_
%token MODECMD_
%token NANCMD_
%token ORIENTCMD_
%token PANCMD_
%token PREFSCMD_
%token PIXELTABLECMD_
%token PRIVATECMD_
%token POWCMD_
%token QUITCMD_
%token RAISECMD_
%token REDCMD_
%token RGBCMD_
%token SCALECMD_
%token SINGLECMD_
%token SINHCMD_
%token SLEEPCMD_
%token SOURCECMD_
%token SQUAREDCMD_
%token SQRTCMD_
%token THEMECMD_
%token THREADSCMD_
%token TILECMD_
%token WIDTHCMD_
%token ZMAXCMD_
%token ZOOMCMD_
%token ZSCALECMD_

%token 123_
%token 132_
%token 213_
%token 231_
%token 312_
%token 321_

%token 3D_
%token ABOUT_
%token AIP_
%token ALL_
%token AMPLIFIER_
%token ARCMIN_
%token ARCSEC_
%token ASINH_
%token AUTO_
%token AUTOMATIC_
%token AVERAGE_
%token AXES_
%token AXIS_
%token AZIMUTH_
%token B1950_
%token BACK_
%token BACKGROUND_
%token BGCOLOR_
%token BIN_
%token BLOCK_
%token BLUE_
%token BORDER_
%token BUFFERSIZE_
%token CATALOG_
%token CENTER_
%token CHANNEL_
%token CLEAR_
%token CLOSE_
%token COLOR_
%token COLORBAR_
%token COLORMAP_
%token COLS_
%token COLUMN_
%token COLSZ_
%token COMPASS_
%token CONTRAST_
%token COORD_
%token CROP_
%token CROSSHAIR_
%token CURRENT_
%token DATAMIN_
%token DATASEC_
%token DEGREES_
%token DEPTH_
%token DETECTOR_
%token DELETE_
%token DIRECTION_
%token ECLIPTIC_
%token ELEVATION_
%token EXAMINE_
%token EXP_
%token FACTOR_
%token FALSE_
%token FILTER_
%token FIRST_
%token FIT_
%token FK4_
%token FK5_
%token FORWARD_
%token FRAME_
%token FRAMENO_
%token FUNCTION_
%token GALATIC_
%token GAP_
%token GLOBAL_
%token GREEN_
%token GRID_
%token HIDE_
%token HIGHLITE_
%token HISTEQU_
%token ICRS_
%token IMAGE_
%token IN_
%token INTERVAL_
%token IRAF_
%token IRAFALIGN_
%token IRAFMIN_
%token J2000_
%token LAST_
%token LAYOUT_
%token LIMITS_
%token LINE_
%token LINEAR_
%token LOCAL_
%token LOCK_
%token LOG_
%token MANUAL_
%token MATCH_
%token MECUBE_
%token METHOD_
%token MINMAX_
%token MIP_
%token MODE_
%token MOSAIC_
%token MOSAICIMAGE_
%token MOVE_
%token MULTIFRAME_
%token NAME_
%token NANCOLOR_
%token NEW_
%token NEXT_
%token NO_
%token NONE_
%token OFF_
%token ON_
%token OPEN_
%token ORDER_
%token OUT_
%token PAN_
%token PLAY_
%token POINTER_
%token POW_
%token PREV_
%token PHYSICAL_
%token RED_
%token REFRESH_
%token REGION_
%token RESET_
%token RGB_
%token RGBCUBE_
%token RGBIMAGE_
%token ROTATE_
%token ROW_
%token SAMPLE_
%token SAVE_
%token SCALE_
%token SCALELIMITS_
%token SCAN_
%token SCOPE_
%token SEXAGESIMAL_
%token SHOW_
%token SINH_
%token SIZE_
%token SLICE_
%token SMOOTH_
%token SQUARED_
%token SQRT_
%token STOP_
%token SUM_
%token SURVEY_
%token SYSTEM_
%token THREADS_
%token TO_
%token TRUE_
%token UPDATE_
%token USER_
%token VIEW_
%token WCS_
%token WCSA_
%token WCSB_
%token WCSC_
%token WCSD_
%token WCSE_
%token WCSF_
%token WCSG_
%token WCSH_
%token WCSI_
%token WCSJ_
%token WCSK_
%token WCSL_
%token WCSM_
%token WCSN_
%token WCSO_
%token WCSP_
%token WCSQ_
%token WCSR_
%token WCSS_
%token WCST_
%token WCSU_
%token WCSV_
%token WCSW_
%token WCSX_
%token WCSY_
%token WCSZ_
%token WFPC2_
%token X_
%token XY_
%token Y_
%token YES_
%token ZMAX_
%token ZOOM_
%token ZSCALE_

%%

commands : commands command
 | command
 ;

command : 2MASSCMD_ {2MASSDialog} 2mass
 | 3DCMD_ {3DDialog} 3d
 | ALIGNCMD_ align
 | ASINHCMD_ {global scale; set scale(type) asinh; ChangeScale}
 | BINCMD_ bin
 | BGCMD_ STRING_ {global pds9; set pds9(bg) $2; PrefsBgColor}
 | BLINKCMD_ blink
 | BLOCKCMD_ {ProcessRealizeDS9} block
 | BLUECMD_ {global current; set current(rgb) blue; RGBChannel}
 | CDCMD_ cd
 | CONSOLECMD_ {global ds9; OpenConsole; InitError $ds9(msg,src)}
 | CROPCMD_ {ProcessRealizeDS9} crop
 | CROSSHAIRCMD_ crosshair
 | CUBECMD_ {CubeDialog} cube
 | CURSORCMD_ INT_ INT_ {CursorCmd $2 $3}
 | FITSCMD_ fits
 | FRAMECMD_ frame
 | GREENCMD_ {global current; set current(rgb) green; RGBChannel}
 | HEIGHTCMD_ INT_ {global canvas; RealizeDS9; set canvas(height) $2; UpdateView}
 | HELPCMD_ {HelpCommand}
 | HISTEQUCMD_ {global scale; set scale(type) histequ; ChangeScale}
 # backward compatibility
 | ICONIFYCMD_ iconify
 | IRAFALIGNCMD_ yesno {global pds9; set pds9(iraf) $2; PrefsIRAFAlign}
 | LINEARCMD_ {global scale; set scale(type) linear; ChangeScale}
 | LOGCMD_ {global scale; set scale(type) log; ChangeScale}
 | LOWERCMD_ {global ds9; lower $ds9(top)}
 | MINMAXCMD_ minmax
 | MODECMD_ mode
 | NANCMD_ STRING_ {global pds9; set pds9(nan) $2; PrefsNanColor}
 | ORIENTCMD_ orient
 | PANCMD_ pan
 | PIXELTABLECMD_ pixelTable
 | PREFSCMD_ prefs
 # backward compatibility
 | PRIVATECMD_ 
 | POWCMD_ {global scale; set scale(type) pow; ChangeScale}
 | QUITCMD_ {QuitDS9}
 | RAISECMD_ {global ds9; raise $ds9(top)}
 | REDCMD_ {global current; set current(rgb) red; RGBChannel}
 | RGBCMD_ {RGBDialog} rgb
 | SINGLECMD_ {global current; ProcessRealizeDS9; set current(display) single; DisplayMode}
 | SINHCMD_ {global scale; set scale(type) sinh; ChangeScale}
 | SLEEPCMD_ {UpdateDS9; RealizeDS9} sleep
 | SOURCECMD_ STRING_ {SourceFileCmd $2}
 | SQUAREDCMD_ {global scale; set scale(type) squared; ChangeScale}
 | SQRTCMD_ {global scale; set scale(type) sqrt; ChangeScale}
 | SCALECMD_ scale
 # backward compatibility
 | THEMECMD_
 | THREADSCMD_ INT_ {global ds9; set ds9(threads) $2; ChangeThreads}
 | TILECMD_ tile
 | WIDTHCMD_ INT_ {global canvas; RealizeDS9; set canvas(width) $2; UpdateView}
 | ZMAXCMD_ {global scale; set scale(mode) zmax; ChangeScaleMode}
 | ZOOMCMD_ {ProcessRealizeDS9} zoom
 | ZSCALECMD_ zscale
 | STRING_ {CommandLineFileName $1}
 ;

numeric	: REAL_ {set _ $1}
 | INT_ {set _ $1}
 ;

yes : YES_ {set _ 1}
 | TRUE_ {set _ 1}
 | ON_ {set _ 1}
 | '1' {set _ 1}
 ;

no : NO_ {set _ 0}
 | FALSE_ {set _ 0}
 | OFF_ {set _ 0}
# | '0' {set _ 0}
 ;

yesno : YES_ {set _ 1}
 | TRUE_ {set _ 1}
 | ON_ {set _ 1}
# | '1' {set _ 1}
 | NO_ {set _ 0}
 | FALSE_ {set _ 0}
 | OFF_ {set _ 0}
# | '0' {set _ 0}
 ;

skyframe : FK4_ {set _ fk4}
 | B1950_ {set _ fk4}
 | FK5_ {set _ fk5}
 | J2000_ {set _ fk5}
 | ICRS_ {set _ icrs}
 | GALATIC_ {set _ galactic}
 | ECLIPTIC_ {set _ ecliptic}
 ;

sysdist : DEGREES_ {set _ degrees}
 | ARCMIN_ {set _ arcmin}
 | ARCSEC_ {set _ arcsec}
 ;

optSex : {set _ sexagesimal}
 | SEXAGESIMAL_ {set _ sexagesimal}
 ;

optDeg : {set _ degrees}
 | DEGREES_ {set _ degrees}
 ;

coordsys : IMAGE_ {set _ image}
 | PHYSICAL_ {set _ physical}
 | AMPLIFIER_ {set _ amplifier}
 | DETECTOR_ {set _ detector}
 | wcssys {set _ $1}
 ;

wcssys : WCS_ {set _ wcs}
 | WCSA_ {set _ wcsa}
 | WCSB_ {set _ wcsb}
 | WCSC_ {set _ wcsc}
 | WCSD_ {set _ wcsd}
 | WCSE_ {set _ wcse}
 | WCSF_ {set _ wcsf}
 | WCSG_ {set _ wcsg}
 | WCSH_ {set _ wcsh}
 | WCSI_ {set _ wcsi}
 | WCSJ_ {set _ wcsj}
 | WCSK_ {set _ wcsk}
 | WCSL_ {set _ wcsl}
 | WCSM_ {set _ wcsm}
 | WCSN_ {set _ wcsn}
 | WCSO_ {set _ wcso}
 | WCSP_ {set _ wcsp}
 | WCSQ_ {set _ wcsq}
 | WCSR_ {set _ wcsr}
 | WCSS_ {set _ wcss}
 | WCST_ {set _ wcst}
 | WCSU_ {set _ wcsu}
 | WCSV_ {set _ wcsv}
 | WCSW_ {set _ wcsw}
 | WCSX_ {set _ wcsx}
 | WCSY_ {set _ wcsy}
 | WCSZ_ {set _ wcsz}
 ;

mosaicImageType : mosaicType {set _ $1}
 | WFPC2_ {set _ wfpc2}
 ;

mosaicType : IRAF_ {set _ iraf}
 | WCS_ {set _ wcs}
 | WCSA_ {set _ wcsa}
 | WCSB_ {set _ wcsb}
 | WCSC_ {set _ wcsc}
 | WCSD_ {set _ wcsd}
 | WCSE_ {set _ wcse}
 | WCSF_ {set _ wcsf}
 | WCSG_ {set _ wcsg}
 | WCSH_ {set _ wcsh}
 | WCSI_ {set _ wcsi}
 | WCSJ_ {set _ wcsj}
 | WCSK_ {set _ wcsk}
 | WCSL_ {set _ wcsl}
 | WCSM_ {set _ wcsm}
 | WCSN_ {set _ wcsn}
 | WCSO_ {set _ wcso}
 | WCSP_ {set _ wcsp}
 | WCSQ_ {set _ wcsq}
 | WCSR_ {set _ wcsr}
 | WCSS_ {set _ wcss}
 | WCST_ {set _ wcst}
 | WCSU_ {set _ wcsu}
 | WCSV_ {set _ wcsv}
 | WCSW_ {set _ wcsw}
 | WCSX_ {set _ wcsx}
 | WCSY_ {set _ wcsy}
 | WCSZ_ {set _ wcsz}
 ;

2mass : {IMGSVRApply dtwomass 1}
 | STRING_ {global dtwomass; set dtwomass(name) $1; IMGSVRApply dtwomass 1}
 | NAME_ STRING_ {global dtwomass; set dtwomass(name) $2; IMGSVRApply dtwomass 1}
 | COORD_ 2massCoord {IMGSVRApply dtwomass 1}
 | SIZE_ 2massSize
 | SAVE_ yesno {global dtwomass; set dtwomass(save) $2}
 | FRAME_ 2massFrame {global dtwomass; set dtwomass(mode) $2}
 | UPDATE_ FRAME_ {IMGSVRUpdate dtwomass; IMGSVRApply dtwomass 1}
 | UPDATE_ CROSSHAIR_ {IMGSVRCrosshair dtwomass; IMGSVRApply dtwomass 1}
 | SURVEY_ 2massSurvey {global dtwomass; set dtwomass(survey) $2}
 | OPEN_ {}
 | CLOSE_ {ARDestroy dtwomass}
 ;

2massCoord : SEXSTR_ SEXSTR_ optSex {
  global dtwomass
  set dtwomass(x) $1
  set dtwomass(y) $2
  set dtwomass(skyformat) $3
  set dtwomass(skyformat,msg) $3
 }
 | numeric numeric optDeg {
  global dtwomass
  set dtwomass(x) $1
  set dtwomass(y) $2
  set dtwomass(skyformat) $3
  set dtwomass(skyformat,msg) $3
 }
 ;

2massFrame : NEW_ {set _ new}
 | CURRENT_ {set _ current}
 ;

2massSize : numeric numeric {
   global dtwomass
   set dtwomass(width) $1
   set dtwomass(height) $2
 }
 | numeric numeric sysdist {
   global dtwomass
   set dtwomass(width) $1
   set dtwomass(height) $2
   set dtwomass(rformat) $3
   set dtwomass(rformat,msg) $3
 }
 ;

2massSurvey : 'j' {set _ $1}
 | 'h' {set _ $1}
 | 'k' {set _ $1}
 ;

3d : {Create3DFrame}
 | VIEW_ numeric numeric {global threed; set threed(az) $2; set threed(el) $3; 3DViewPoint}
 | AZIMUTH_ numeric {global threed; set threed(az) $2; 3DViewPoint}
 | ELEVATION_ numeric {global threed; set threed(el) $2; 3DViewPoint}
 | SCALE_ numeric {global threed; set threed(scale) $2; 3DScale}
 | METHOD_ 3dMethod {global threed; set threed(method) $2; 3DRenderMethod}
 | BACKGROUND_ 3dBackground {global threed; set threed(background) $2; 3DBackground}
 | BORDER_ 3dBorder
 | HIGHLITE_ 3dHighlite
 | COMPASS_ 3dCompass
 | OPEN_ {}
 | CLOSE_ {3DDestroyDialog}
 ;

3dMethod : MIP_ {set _ mip}
 | AIP_ {set _ aip}
 ;

3dBackground : NONE_ {set _ none}
 | AZIMUTH_ {set _ azimuth}
 | ELEVATION_ {set _ elevation}
 ;

3dHighlite : yesno {global threed; set threed(highlite) $1; 3DHighlite}
 | COLOR_ STRING_ {global threed; set threed(highlite,color) $2; 3DHighliteColor}
 ;

3dBorder : yesno {global threed; set threed(border) $1; 3DBorder}
 | COLOR_ STRING_ {global threed; set threed(border,color) $2; 3DBorderColor}
 ;

3dCompass : yesno {global threed; set threed(compass) $1; 3DCompass}
 | COLOR_ STRING_ {global threed; set threed(compass,color) $2; 3DCompassColor}
 ;

align : {global current; set current(align) 1; AlignWCSFrame}
 | yesno {global current; set current(align) $1; AlignWCSFrame}
 ;

blink : {global current; set current(display) blink; DisplayMode}
 | yes {global current; set current(display) blink; DisplayMode}
 | no {global current; set current(display) single; DisplayMode}
 | INTERVAL_ numeric {global blink; set blink(interval) [expr int($2*1000)]; DisplayMode}
 ;

bin : CLOSE_ {BinDestroyDialog}
 | OPEN_ {BinDialog}
 | MATCH_ {MatchBinCurrent}
 | LOCK_ binLock
 | ABOUT_ binAbout
 | BUFFERSIZE_ INT_ {global bin; set bin(buffersize) $2; ChangeBinBufferSize}
 | COLS_ STRING_ STRING_ {BinCols \"$2\" \"$3\" \"\"}
 | COLSZ_ STRING_ STRING_ STRING_ {BinCols \"$2\" \"$3\" \"$4\"}
 | FACTOR_ binFactor
 | DEPTH_ INT_ {global bin; set bin(depth) $1; ChangeBinDepth}
 | FILTER_ STRING_ {BinFilter $2}
 | FUNCTION_ binFunction {global bin; set bin(function) $1; ChangeBinFunction}
 | IN_ {Bin .5 .5}
 | OUT_ {Bin 2 2}
 | TO_ binTo
 ;

binLock : {global bin; set bin(lock) 1; LockBinCurrent}
 | yesno {global bin; set bin(lock) $1; LockBinCurrent}
 ;

binAbout : numeric numeric {BinAbout $1 $2}
 | CENTER_ {BinAboutCenter}
 ;

binFactor : numeric {global bin; set bin(factor) " $1 $1 "; ChangeBinFactor}
 | numeric numeric {global bin; set bin(factor) " $1 $2 "; ChangeBinFactor}
 ;

binFunction: AVERAGE_ {set _ average}
 | SUM_ {set _ sum}
 ;

binTo: binFactor
 | FIT_ {BinToFit}
 ;

block : INT_ {Block $1 $1}
 | INT_ INT_ {Block $1 $2}
 | OPEN_ {BlockDialog}
 | CLOSE_ {BlockDestroyDialog}
 | MATCH_ {MatchBlockCurrent}
 | LOCK_ blockLock
 | IN_ {Block .5 .5}
 | OUT_ {Block 2 2}
 | TO_ blockTo
 ;

blockLock : {global block; set block(lock) 1; LockBlockCurrent}
 | yesno {global block; set block(lock) $1; LockBlockCurrent}
 ;

blockTo : INT_ {global block; set block(factor) " $1 $1 "; ChangeBlock}
 | INT_ INT_ {global block; set block(factor) " $1 $2 "; ChangeBlock}
 | FIT_ {BlockToFit}
 ; 

cd : STRING_ {cd $2}
 | '.' {cd .}
 | '/' {cd /}
 ;

crop : numeric numeric numeric numeric {global current; $current(frame) crop center $1 $2 image fk5 $3 $4 image degrees}
 | numeric numeric numeric numeric coordsys {global current; $current(frame) crop center $1 $2 $5 fk5 $3 $4 $5 degrees}
 | numeric numeric numeric numeric coordsys skyframe {global current; $current(frame) crop center $1 $2 $5 $6 $3 $4 $5 degrees}
 | numeric numeric numeric numeric coordsys skyframe sysdist {global current; $current(frame) crop center $1 $2 $5 $6 $3 $4 $5 $7}
 | numeric numeric numeric numeric skyframe {global current; $current(frame) crop center $1 $2 wcs $5 $3 $4 wcs degrees}
 | numeric numeric numeric numeric skyframe sysdist {global current; $current(frame) crop center $1 $2 wcs $5 $3 $4 wcs $6}
 | SEXSTR_ SEXSTR_ numeric numeric coordsys {global current; $current(frame) crop center $1 $2 $5 fk5 $3 $4 $5 degrees}
 | SEXSTR_ SEXSTR_ numeric numeric coordsys skyframe {global current; $current(frame) crop center $1 $2 $5 $6 $3 $4 $5 degrees}
 | SEXSTR_ SEXSTR_ numeric numeric coordsys skyframe sysdist {global current; $current(frame) crop center $1 $2 $5 $6 $3 $4 $5 $7}
 | SEXSTR_ SEXSTR_ numeric numeric skyframe {global current; $current(frame) crop center $1 $2 wcs $5 $3 $4 wcs degrees}
 | SEXSTR_ SEXSTR_ numeric numeric skyframe sysdist {global current; $current(frame) crop center $1 $2 wcs $5 $3 $4 wcs $6}

 | OPEN_ {CropDialog}
 | CLOSE_ {CropDestroyDialog}
 | MATCH_ coordsys {MatchCropCurrent $2}
 | LOCK_ coordsys {global crop; set crop(lock) $2; LockCropCurrent}
 | LOCK_ NONE_ {global crop; set crop(lock) none; LockCropCurrent}
 | RESET_ {CropReset}
 | 3D_ numeric numeric {global current; $current(frame) crop 3d $2 $3 image}
 | 3D_ numeric numeric coordsys {global current; $current(frame) crop 3d $2 $3 $4}
 ;

crosshair : numeric numeric {CrosshairTo $1 $2 image fk5}
 | numeric numeric coordsys {CrosshairTo $1 $2 $3 fk5}
 | numeric numeric coordsys skyframe {CrosshairTo $1 $2 $3 $4}
 | numeric numeric skyframe {CrosshairTo $1 $2 wcs $3}
 | SEXSTR_ SEXSTR_ coordsys {CrosshairTo $1 $2 $3 fk5}
 | SEXSTR_ SEXSTR_ coordsys skyframe {CrosshairTo $1 $2 $3 $4}
 | SEXSTR_ SEXSTR_ skyframe {CrosshairTo $1 $2 $3 fk5}
 | MATCH_ coordsys {global crosshair; MatchCrosshairCurrent $2}
 | LOCK_ coordsys {global crosshair; set crosshair(lock) $2; LockCrosshairCurrent}
 | LOCK_ NONE_ {global crosshair; set crosshair(lock) none; LockCrosshairCurrent}
 ;

cube : cubeSlice
 | OPEN_ {}
 | CLOSE_ {CubeDestroyDialog}
 | MATCH_ cubeMatch
 | LOCK_ cubeLock
 | PLAY_ {CubePlay}
 | STOP_ {CubeStop}
 | NEXT_ {CubeNext}
 | PREV_ {CubePrev}
 | FIRST_ {CubeFirst}
 | LAST_ {CubeLast}
 | INTERVAL_ numeric {global blink; set blink(interval) [expr int($2*1000)]}
 | AXIS_ INT_ {global cube; set cube(axis) [expr $2-1]}
 | AXES_ cubeAxes
 | ORDER_ cubeAxes
 ;

cubeSlice : INT_ {global dcube; global cube; set dcube(wcs,2) $1; set cube(system) image; set cube(axis) 2; CubeApply 2}
 | numeric coordsys {global dcube; global cube; set dcube(wcs,2) $1; set cube(system) $2; set cube(axis) 2; CubeApply 2}
 | numeric coordsys INT_ {global dcube; global cube; set aa [expr $3-1]; set dcube(wcs,$aa) $1; set cube(system) $2; set cube(axis) $aa; CubeApply $aa}
 ;

cubeMatch : {MatchCubeCurrent image}
 | coordsys {MatchCubeCurrent $1}
 ;

cubeLock : {global cube; set cube(lock) image; LockCubeCurrent}
 | yes {global cube; set cube(lock) image; LockCubeCurrent}
 | no {global cube; set cube(lock) none; LockCubeCurrent}
 | coordsys {global cube; set cube(lock) $1; LockCubeCurrent}
 | NONE_ {global cube; set cube(lock) none; LockCubeCurrent}
 ;

cubeAxes : cubeAxesOrder {global cube; set cube(axes) $1; CubeAxes}
 | LOCK_ cubeAxesLock
 ;

cubeAxesOrder : 123_ {set _ 123}
 | 132_ {set _ 132}
 | 213_ {set _ 213}
 | 231_ {set _ 231}
 | 312_ {set _ 312}
 | 321_ {set _ 321}
 ;

cubeAxesLock : {global cube; set cube(lock,axes) 1; LockAxesCurrent}
 | yesno {global cube; set cube(lock,axes) $1; LockAxesCurrent}
 ;

fits : {global file; set file(type) fits}
 | MOSAIC_ mosaicType {global file; set file(type) mosaic; set file(mosaic) $2}
 | MOSAICIMAGE_ mosaicImageType {global file; set file(type) mosaicimage; set file(mosaic) $2}
 | MECUBE_ {global file; set file(type) mecube}
 | MULTIFRAME_ {global file; set file(type) multiframe}
 | RGBCUBE_ {global file; set file(type) rgbcube}
 | RGBIMAGE_ {global file; set file(type) rgbimage}
 ;

frame : INT_ {CreateGotoFrame $1 base}
 | MATCH_ coordsys {MatchFrameCurrent $2}
 | LOCK_ frameLock
 | CENTER_ frameCenter
 | CLEAR_ frameClear
 | DELETE_ frameDelete
 | NEW_ frameNew
 | RESET_ frameReset
 | REFRESH_ frameRefresh
 | HIDE_ frameHide
 | SHOW_ frameShow
 | MOVE_ frameMove
 | FIRST_ {FirstFrame}
 | PREV_ {PrevFrame}
 | NEXT_ {NextFrame}
 | LAST_ {LastFrame}
 | FRAMENO_ INT_ {CreateGotoFrame $2 base}
 ;

frameLock : coordsys {global panzoom; set panzoom(lock) $1; LockFrameCurrent}
 | NONE_ {global panzoom; set panzoom(lock) none; LockFrameCurrent}
 ;

frameCenter: {CenterCurrentFrame}
 | ALL_ {CenterAllFrame}
 | INT_ {CenterFrame Frame$1}
 ;

frameClear: {ClearCurrentFrame}
 | ALL_ {ClearAllFrame}
 | INT_ {ClearFrame Frame$1}
 ;

frameDelete: {DeleteCurrentFrame}
 | ALL_ {DeleteAllFrames}
 | INT_ {DeleteSingleFrame Frame$1}
 ;

frameNew: {CreateFrame}
 | RGB_ {CreateRGBFrame}
 | 3D_ {Create3DFrame}
 ;

frameReset: {ResetCurrentFrame}
 | ALL_ {ResetAllFrame}
 | INT_ {ResetFrame Frame$1}
 ;

frameRefresh: {UpdateCurrentFrame}
 | ALL_ {UpdateAllFrame}
 | INT_ {UpdateFrame Frame$1}
 ;

frameHide: {global active; global current; set active($current(frame)) 0; UpdateActiveFrames}
 | ALL_ {ActiveFrameNone}
 | INT_ {global active; set active(Frame$1) 0; UpdateActiveFrames}
 ;

frameShow: {}
 | ALL_ {ActiveFrameAll}
 | INT_ {global active; set active(Frame$1) 1; UpdateActiveFrames}
 ;

frameMove : FIRST_ {MoveFirstFrame}
 | BACK_ {MovePrevFrame}
 | FORWARD_ {MoveNextFrame}
 | LAST_ {MoveLastFrame}
 ;

iconify : {global ds9; wm iconify $ds9(top)}
 | yes {global ds9; wm iconify $ds9(top)}
 | no {global ds9; wm deiconify $ds9(top)}
 ;

minmax : {global scale; set scale(mode) minmax; ChangeScaleMode}
 # backward compatibility
 | AUTO_ {global minmax; set minmax(mode) scan; ChangeMinMax}
 | SCAN_ {global minmax; set minmax(mode) scan; ChangeMinMax}
 | SAMPLE_ {global minmax; set minmax(mode) sample; ChangeMinMax}
 | DATAMIN_ {global minmax; set minmax(mode) datamin; ChangeMinMax}
 | IRAFMIN_ {global minmax; set minmax(mode) irafmin; ChangeMinMax}
 | MODE_ minmaxMode {global minmax; set minmax(mode) $2; ChangeMinMax}
 | INTERVAL_ INT_ {global minmax; set minmax(sample) $2; ChangeMinMax}
 ;

minmaxMode : SCAN_ {set _ scan}
 | SAMPLE_ {set _ sample}
 | DATAMIN_ {set _ datamin}
 | IRAFMIN_ {set _ irafmin}
 ;

mode : NONE_ {global current; set current(mode) none; ChangeMode}
 # backward compatibility
 | POINTER_ {global current; set current(mode) none; ChangeMode}
 | REGION_ {global current; set current(mode) region; ChangeMode}
 | CROSSHAIR_ {global current; set current(mode) crosshair; ChangeMode}
 | COLORBAR_ {global current; set current(mode) colorbar; ChangeMode}
 | PAN_ {global current; set current(mode) pan; ChangeMode}
 | ZOOM_ {global current; set current(mode) zoom; ChangeMode}
 | ROTATE_ {global current; set current(mode) rotate; ChangeMode}
 | CROP_ {global current; set current(mode) rotate; ChangeMode}
 | CATALOG_ {global current; set current(mode) catalog; ChangeMode}
 | EXAMINE_ {global current; set current(mode) examine; ChangeMode}
 ;

orient : orientation {global current; set current(orient) $1; ChangeOrient}
 | OPEN_ {PanZoomDialog}
 | CLOSE_ {PanZoomDestroyDialog}
 ;

orientation : NONE_ {set _ none}
 | X_ {set _ x}
 | Y_ {set _ y}
 | XY_ {set _ xy}
 ;

pan : {}
 | OPEN_ {PanZoomDialog}
 | CLOSE_ {PanZoomDestroyDialog}
 | TO_ panTo
 ;

panTo : {}
 ;

pixelTable : {PixelTableDialog}
 | yes {PixelTableDialog}
 | OPEN_ {PixelTableDialog}
 | no {PixelTableDestroyDialog}
 | CLOSE_ {PixelTableDestroyDialog}
 ;

prefs : CLEAR_ {ClearPrefs}
 # backward compatibility
 | BGCOLOR_ STRING_ {global pds9; set pds9(bg) $2; PrefsBgColor}
 # backward compatibility
 | NANCOLOR_ STRING_ {global pds9; set pds9(nan) $2; PrefsNanColor}
 # backward compatibility
 | THREADS_ INT_ {global pds9; set ds9(threads) $2; ChangeThreads}
 | IRAFALIGN_ yesno {global pds9; set pds9(iraf) $2; PrefsIRAFAlign}
 ;

rgb : {CreateRGBFrame}
 | OPEN_ {}
 | CLOSE_ {RGBDestroyDialog}
 | RED_ {global current; set current(rgb) red; RGBChannel}
 | GREEN_ {global current; set current(rgb) green; RGBChannel}
 | BLUE_ {global current; set current(rgb) blue; RGBChannel}
 | CHANNEL_ rgbChannel {global current; set current(rgb) $2; RGBChannel}
 | LOCK_ rgbLock
 | SYSTEM_ coordsys {global rgb; set rgb(system) $2; RGBSystem}
 | VIEW_ rgbView
 ;

rgbChannel : RED_ {set _ red}
 | GREEN_ {set _ green}
 | BLUE_ {set _ blue}
 ;

rgbLock : WCS_ rgbLockWCS
 | CROP_ rgbLockCrop
 | SLICE_ rgbLockSlice
 | BIN_ rgbLockBin
 | AXES_ rgbLockAxes
 | ORDER_ rgbLockAxes
 | SCALE_ rgbLockScale
 | LIMITS_ rgbLockScalelimits
 | SCALELIMITS_ rgbLockScalelimits
 | COLOR_ rgbLockColorbar
 | COLORMAP_ rgbLockColorbar
 | COLORBAR_ rgbLockColorbar
 | BLOCK_ rgbLockBlock
 | SMOOTH_ rgbLockSmooth
 ;

rgbLockWCS: {global rgb; set rgb(lock,wcs) 1;}
 | yesno {global rgb; set rgb(lock,wcs) $1;}
 ;

rgbLockCrop: {global rgb; set rgb(lock,crop) 1;}
 | yesno {global rgb; set rgb(lock,crop) $1;}
 ;

rgbLockSlice: {global rgb; set rgb(lock,slice) 1;}
 | yesno {global rgb; set rgb(lock,slice) $1;}
 ;

rgbLockBin: {global rgb; set rgb(lock,bin) 1;}
 | yesno {global rgb; set rgb(lock,bin) $1;}
 ;

rgbLockAxes: {global rgb; set rgb(lock,axes) 1;}
 | yesno {global rgb; set rgb(lock,axes) $1;}
 ;

rgbLockScale: {global rgb; set rgb(lock,scale) 1;}
 | yesno {global rgb; set rgb(lock,scale) $1;}
 ;

rgbLockScalelimits: {global rgb; set rgb(lock,scalelimits) 1;}
 | yesno {global rgb; set rgb(lock,scalelimits) $1;}
 ;

rgbLockColorbar: {global rgb; set rgb(lock,colorbar) 1;}
 | yesno {global rgb; set rgb(lock,colorbar) $1;}
 ;

rgbLockBlock: {global rgb; set rgb(lock,block) 1;}
 | yesno {global rgb; set rgb(lock,block) $1;}
 ;

rgbLockSmooth: {global rgb; set rgb(lock,smooth) 1;}
 | yesno {global rgb; set rgb(lock,smooth) $1;}
 ;

rgbView : RED_ yesno {global rgb; set rgb(red) $2; RGBView}
 | GREEN_ yesno {global rgb; set rgb(green) $2; RGBView}
 | BLUE_ yesno {global rgb; set rgb(blue) $2; RGBView}
 ;

scale : scaleScales {global scale; set scale(type) $1; ChangeScale}
 | LOG_ scaleLog
 | DATASEC_ yesno
 | LIMITS_ scaleLimits
 | SCALELIMITS_ scaleLimits
 | MINMAX_ {global scale; set scale(mode) minmax; ChangeScaleMode}
 | ZSCALE_ {global scale; set scale(mode) zscale; ChangeScaleMode}
 | ZMAX_ {global scale; set scale(mode) zmax; ChangeScaleMode}
 | USER_ {global scale; set scale(mode) user; ChangeScaleMode}
 | MODE_ scaleMode {global scale; set scale(mode) $2; ChangeScaleMode}
 | MODE_ numeric {global scale; set scale(mode) $2; ChangeScaleMode}
 | LOCAL_ {global scale; set scale(scope) local; ChangeScaleScope}
 | GLOBAL_ {global scale; set scale(scope) global; ChangeScaleScope}
 | SCOPE_ scaleScope {global scale; set scale(scope) $2; ChangeScaleScope}
 | MATCH_ {MatchScaleCurrent} 
 | MATCH_ LIMITS_ {MatchScaleLimitsCurrent}
 | MATCH_ SCALELIMITS_ {MatchScaleLimitsCurrent}
 | LOCK_ {global scale; set scale(lock) 1; LockScaleCurrent} 
 | LOCK_ yesno {global scale; set scale(lock) $2; LockScaleCurrent}
 | LOCK_ LIMITS_ {global scale; set scale(lock,limits) 1; LockScaleLimitsCurrent} 
 | LOCK_ LIMITS_ scaleLockLimits
 | LOCK_ SCALELIMITS_ {global scale; set scale(lock,limits) 1; LockScaleLimitsCurrent} 
 | LOCK_ SCALELIMITS_ scaleLockLimits
 | OPEN_ {ScaleDialog}
 | CLOSE_ {ScaleDestroyDialog}
 ;

scaleScales : LINEAR_ {set _ linear}
 | POW_ {set _ pow}
 | SQRT_ {set _ sqrt}
 | SQUARED_ {set _ squared}
 | ASINH_ {set _ asinh}
 | SINH_ {set _ sinh}
 | HISTEQU_ {set _ histequ}
 ;

scaleLog : {global scale; set scale(type) log; ChangeScale}
 | EXP_ numeric {global scale; set scale(log) $2; ChangeScale}
 ;

scaleLimits: numeric numeric {global scale; set scale(min) $1; set scale(max) $2; ChangeScaleLimit}
 ;
	     
scaleLockLimits : yesno {global scale; set scale(lock,limits) $1; LockScaleLimitsCurrent}
 ;

scaleMode : MINMAX_ {set _ minmax}
 | ZSCALE_ {set _ zscale}
 | ZMAX_ {set _ zmax}
 ;

scaleScope : LOCAL_ {set _ local}
 | GLOBAL_ {set _ global}
 ;

sleep : {after 1000}
 | numeric {after [expr int($1*1000)]}
 ;

tile: {global current; set current(display) tile; DisplayMode}
 | yes {global current; set current(display) tile; DisplayMode}
 | no {global current; set current(display) single; DisplayMode}
 | MODE_ tileMode {global tile; set tile(mode) $2; DisplayMode}
 | GRID_ tileGrid
 | COLUMN_ {global tile; set tile(mode) column; DisplayMode}
 | ROW_ {global tile; set tile(mode) row; DisplayMode}
 ;

tileMode : GRID_ {set _ grid}
 | COLUMN_ {set _ column}
 | ROW_ {set _ row}
 ;

tileGrid : {global tile; set tile(mode) grid; DisplayMode}
 | MODE_ tileGridMode {global tile; set tile(grid,mode) $2; DisplayMode}
 | DIRECTION_ tileGridDir {global tile; set tile(grid,dir) $2; DisplayMode}
 | LAYOUT_ INT_ INT_ {global tile; set tile(grid,col) $2; set tile(grid,row) $3; set tile(grid,mode) manual; DisplayMode}
 | GAP_ INT_ {global tile; set tile(grid,gap) $2; DisplayMode}
 ;

tileGridMode : AUTOMATIC_ {set _ automatic}
 | MANUAL_ {set _ manual}
 ;

tileGridDir : X_ {set _ x}
 | Y_ {set _ y}
 ;

zoom : numeric {Zoom $1 $1}
 | numeric numeric {Zoom $1 $2}
 | OPEN_ {PanZoomDialog}
 | CLOSE_ {PanZoomDestroyDialog}
 | IN_ {Zoom 2 2}
 | OUT_ {Zoom .5 .5}
 | TO_ zoomTo
 ;

zoomTo: FIT_ {ZoomToFit}
 | numeric {global zoom; set current(zoom) " $1 $1 "; ChangeZoom}
 | numeric numeric {global zoom; set current(zoom) " $1 $2 "; ChangeZoom}
 ;

zscale : {global scale; set scale(mode) zscale; ChangeScaleMode}
 | CONTRAST_ numeric {global zscale; set zscale(contrast) $2; ChangeZScale}
 | SAMPLE_ INT_ {global zscale; set zscale(sample) $2; ChangeZScale}
 | LINE_ INT_ {global zscale; set zscale(line) $2; ChangeZScale}
 ;

%%

proc yyerror {s} {
     puts stderr "parse error:"
     puts stderr "$::yy_buffer"
     puts stderr [format "%*s" $::yy_index ^]
}

proc yydone {} {
     puts stderr "z: $file(load)"
     global file
     if {$file(load) != 0} {
	FinishLoadPost
     }
}