// Copyright (C) 1999-2016
// Smithsonian Astrophysical Observatory, Cambridge, MA, USA
// For conditions of distribution and use, see copyright notice in "copyright"

#ifndef __tkmacosx_h__
#define __tkmacosx_h__

#include <tcl.h>

#include <vector.h>

class TkMacosx {
 private:
  Tcl_Interp* interp;

  /*
  int showDialog;

  CGContextRef context;
  Matrix canvasToPage;

  OSStatus status;
  PMPageFormat pageFormat;
  PMPrintSettings printSettings;
  PMPrintSession printSession;

  int pmPrint(int, const char**);
  int pmPrintBegin(int, const char**);
  int pmPrintEnd();
  int pmPrintText(int, const char**);
  int pmPageSetup();
  */
 public:
  TkMacosx(Tcl_Interp*);
  ~TkMacosx();

  //  int pm(int, const char**);
  int locale(int, const char**);
  /*
  const Matrix& getCanvasToPage() {return canvasToPage;}

  void begin();
  void end();

  void color(float,float,float);
  void width(float);
  void dash(float*,int);
  void font(const char*, float);
  void clip(float, float, float, float);

  void newpath();
  void stroke();
  void fill();
  void arc(float, float, float, float, float);
  void curve(float, float, float, float, float, float, float, float);

  void drawText(float, float, float, const char*);
  void drawLines(float*, float*, int);
  void fillPolygon(float*, float*, int);
  void drawArc(float, float, float, float, float);
  
  void bitmapCreate(void*, int, int, float, float, float, float);
  */
};

extern TkMacosx* tkmacosx;

#endif
