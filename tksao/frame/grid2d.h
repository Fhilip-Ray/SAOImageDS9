// Copyright (C) 1999-2017
// Smithsonian Astrophysical Observatory, Cambridge, MA, USA
// For conditions of distribution and use, see copyright notice in "copyright"

#ifndef __grid2d_h__
#define __grid2d_h__

#include "grid.h"
#include "grid2dbase.h"
#include "coord.h"

class Grid2d : public Grid, public Grid2dBase {
 private:
  int matrixMap(void*, Matrix&, const char*);
  int doit(RenderMode);

 public:
  Grid2d(Widget*, Coord::CoordSystem, Coord::SkyFrame, 
	 Coord::SkyFormat, GridType, 
	 const char*, const char*);
  ~Grid2d();

  const char* option() {return GridBase::option();}

  void x11() {doit(X11);}
  void ps(int mode) {mode_=mode; doit(PS);}
#ifdef MAC_OSX_TK
  void macosx() {doit(MACOSX);}
#endif
#ifdef __WIN32
  void win32() {doit(GWIN32);}
#endif
};

#endif
