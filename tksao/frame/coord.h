// Copyright (C) 1999-2017
// Smithsonian Astrophysical Observatory, Cambridge, MA, USA
// For conditions of distribution and use, see copyright notice in "copyright"

#ifndef __coord_h__
#define __coord_h__

#include <string.h>

#include <iostream>
#include <sstream>
#include <iomanip>
using namespace std;

class FitsImage;

class Coord {
 public:
  enum InternalSystem {WINDOW, CANVAS, WIDGET, USER, REF, 
		       PANNER, MAGNIFIER, PS};

  enum CoordSystem {DATA, IMAGE, PHYSICAL, AMPLIFIER, DETECTOR, WCS, 
		    WCSA, WCSB, WCSC, WCSD, WCSE, WCSF, WCSG, WCSH, WCSI,
		    WCSJ, WCSK, WCSL, WCSM, WCSN, WCSO, WCSP, WCSQ, WCSR,
		    WCSS, WCST, WCSU, WCSV, WCSW, WCSX, WCSY, WCSZ, WCS0};

  enum SkyFrame {FK4, FK4_NO_E, FK5, ICRS, GALACTIC, SUPERGALACTIC, 
		 ECLIPTIC, HELIOECLIPTIC};

  enum SkyFormat {DEGREES, SEXAGESIMAL};
  enum SkyDist {DEGREE, ARCMIN, ARCSEC};
  enum AngleFormat {DEG, RAD};
  enum Orientation {NORMAL, XX, YY, XY};

  public:
  void listCoordSystem(ostream&, CoordSystem, SkyFrame, FitsImage*);
  void listDistSystem(ostream&, CoordSystem, SkyDist, FitsImage*);
  void listProsCoordSystem(ostream&, CoordSystem, SkyFrame);

  void strToCoordSystem(const char*, CoordSystem, CoordSystem*, SkyFrame*);
  void strToSkyFormat(const char*, SkyFormat*);
  void strToSkyDist(const char*, SkyDist*);
  void strToDistSystem(const char*, CoordSystem, CoordSystem*, SkyDist*);
  void strToAngleFormat(const char*, AngleFormat*);

  const char* coordSystemStr(int ii);
  const char* skyFrameStr(int ii);
  const char* skyFormatStr(int ii);
  const char* skyDistStr(int ii);
};

extern Coord coord;

#endif
