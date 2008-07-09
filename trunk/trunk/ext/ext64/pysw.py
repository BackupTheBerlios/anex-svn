# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.34
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _pysw
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


swe_julday = _pysw.swe_julday
swe_sidtime = _pysw.swe_sidtime
swe_revjul = _pysw.swe_revjul
swe_calc = _pysw.swe_calc
swe_calc_ut = _pysw.swe_calc_ut
swe_fixstar_ut = _pysw.swe_fixstar_ut
swe_houses = _pysw.swe_houses
swe_houses_armc = _pysw.swe_houses_armc
swe_close = _pysw.swe_close
swe_deltat = _pysw.swe_deltat
swe_set_ephe_path = _pysw.swe_set_ephe_path
def julday(y,m,d,h):
    if (y * 10000 + m * 100 + d) < 15821015:
        gregflag = 0
    else:
        gregflag = 1
    r = _pysw.swe_julday(y,m,d,h,gregflag)
    return r

def revjul(jd,gregflag=1):
    return _pysw.swe_revjul(jd,gregflag)

def calc(jd,pl,epheflag=4): 
    r = _pysw.swe_calc(jd+delta(jd),pl,epheflag) 
    return r[0], r[1][0], r[-1]

def calc_ut(jd,pl,epheflag=4): 
    r = _pysw.swe_calc(jd,pl,epheflag)
    return r[0], r[1][0], r[-1]

def calc_ut_with_speed(jd,pl,epheflag=4): 
    r = _pysw.swe_calc(jd,pl,epheflag|256)
    return r[0], r[1][0], r[1][3], r[-1]

def fixstar(star,jd,epheflag=4):
    r = _pysw.swe_fixstar_ut(star,jd,epheflag)
    return r 

def houses(jd,glt,glg):
    s,h = _pysw.swe_houses(jd,glt,glg,ord('K'))
    if s < 0 and glt < 66.53333336:
        print("error computing houses")
        return None
    return h

def local_houses(jd,glg,glt,epheflag):
    armc = glg
    if armc < 0:
        armc += 360 
    s,eps,e = calc(jd,-1,epheflag)
    s,h = _pysw.swe_houses_armc(armc,glt,eps,ord('K'))
    if s < 0:
        print("error computing local houses")
        return None
    return h

def delta(jd):
    return _pysw.swe_deltat(jd)

def planets(jd,epheflag,p=12):
    pl = []
    for i in range(p):
        if i == 10:
            continue
        s,l,e = calc(jd,i,epheflag)
        if s < 0:
            print("error: %s" % e)
            return None
        pl.append(l)
    return pl

setpath = _pysw.swe_set_ephe_path
sidtime = _pysw.swe_sidtime



