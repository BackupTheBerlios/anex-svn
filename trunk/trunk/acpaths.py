# -*- coding: utf-8 -*-
import cairo
import pangocairo
import pickle

acpaths = {}

def warpPath(cr,let):
    for path in let:
        path = path.replace("close path","close_path")
        plist = path.split(' ')
        typ, points = plist[0].strip(),plist[1:] 
        floatpoints = [float(point.strip()) for point in points]
        getattr(cr,typ)(*floatpoints)

def get_zod_paths():
    global acpaths

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32,400,400)
    cr = pangocairo.CairoContext(cairo.Context(surface))
    cr.set_source_rgb(1.0,1.0,1.0)
    cr.rectangle(0,0,400,400)
    cr.fill()
    cr.select_font_face('Victorian LET',cairo.FONT_SLANT_NORMAL,cairo.FONT_WEIGHT_NORMAL)
    font_size = 72.0
    cr.set_font_size(font_size)
    for s in ['A','C']:
        cr.text_path(s)
        acpaths[s] = cr.copy_path()
        acpaths[s] = acpaths[s].__str__()
        cr.new_path() # critical!
    
    f = open('ac.pk','w') 
    pickle.dump(acpaths,f)
    f.close()
    
    cr.set_source_rgb(0.72,0.58,0) 
    cr.set_source_rgb(0.74,0.42,0.85) 
    for i,s in enumerate(['A','C']):
        cr.save()
        cr.translate(20+50*i,200)
        warpPath(cr,acpaths[s].split('\n'))
        cr.fill()
        cr.restore()
    
    surface.write_to_png('ckntest.png') 

if __name__ == '__main__':
    get_zod_paths()
    #f = open('ckn.pk') 
    #obj = pickle.load(f) 
    #f.close()
    #print obj

#f = open('ckn/resources/ckn.pk') 
#acpaths = pickle.load(f) 
#f.close()
#
#        for i,s in enumerate(['C','K','N']):
#            cr.translate(*coords[i])
#            warpCKN(cr,acpaths[s].split('\n'))
#            cr.set_source_rgb(*cols[i]) 
#            cr.fill()
#
