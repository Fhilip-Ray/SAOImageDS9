// Copyright (C) 1999-2016
// Smithsonian Astrophysical Observatory, Cambridge, MA, USA
// For conditions of distribution and use, see copyright notice in "copyright"

#ifndef __grid_h__
#define __grid_h__

#include "coord.h"

class Grid {
 public:
  enum GridType {ANALYSIS,PUBLICATION};

 protected:
  GridType type_;
  Coord::CoordSystem system_;
  Coord::SkyFrame sky_;
  Coord::SkyFormat skyFormat_;
  char* vars_;

 public:
  Grid(Coord::CoordSystem, Coord::SkyFrame, Coord::SkyFormat, 
       GridType, const char*);
  virtual ~Grid();

  virtual const char* option() =0;

  virtual void x11() =0;
  virtual void ps(int) =0;
#ifdef MAC_OSX_TK
  virtual void macosx() =0;
#endif
#ifdef __WIN32
  virtual void win32() =0;
#endif

  GridType type() {return type_;}
  Coord::CoordSystem system() {return system_;}
  Coord::SkyFrame sky() {return sky_;}
  Coord::SkyFormat skyFormat() {return skyFormat_;}
  const char* vars() {return vars_;}
};

#endif
