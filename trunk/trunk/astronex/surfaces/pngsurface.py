# -*- coding: utf-8 -*-
import os
import sys
import gtk
import cairo
import pangocairo
import pango
from .. drawing.dispatcher import DrawMixin
from .. utils import parsestrtime
from .. boss import boss
curr = boss.get_state()
opts = None
minim = None
MAGICK_SCALE = 0.002

suffixes = boss.suffixes

class DrawPng(object):
    @staticmethod
    def clicked(boss):
        global opts,minim
        opts = boss.opts

        dialog = gtk.FileChooserDialog(_("Guardar..."),
                                    None,
                                    gtk.FILE_CHOOSER_ACTION_SAVE,
                                    (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                        gtk.STOCK_SAVE, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)

        filter = gtk.FileFilter()
        filter.set_name(_("Imagen Png"))
        filter.add_mime_type("image/png")
        filter.add_pattern("*.png")
        dialog.add_filter(filter)
        name = curr.curr_chart.first + "_" + suffixes[curr.curr_op]
        dialog.set_current_name(name+".png")
        if sys.platform == 'win32':
            import winshell
            dialog.set_current_folder(winshell.my_documents())
        else: 
            dialog.set_current_folder(os.path.expanduser("~"))
        dialog.set_do_overwrite_confirmation(True)

        filename = None
        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            filename = dialog.get_filename()
        elif response == gtk.RESPONSE_CANCEL:
            pass
        dialog.destroy()

        if filename is None or filename == '': return

        w = int(opts.hsize)
        h = int(opts.vsize)
        if curr.curr_op in ['compo_one','compo_two']:
            w = 800
            h = 1100
        minim = min(w,h)
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32,w,h)
        cr = pangocairo.CairoContext(cairo.Context(surface))
        cr.set_source_rgb(1.0,1.0,1.0)
        cr.rectangle(0,0,w,h)
        cr.fill()
        cr.set_line_join(cairo.LINE_JOIN_ROUND) 
        cr.set_line_width(float(opts.base))
        dr = DrawMixin(opts,DrawPng())
        dr.dispatch_pres(cr,w,h)
        if opts.labels == 'true' or curr.curr_op in ['compo_one','compo_tow']:
            draw_label(cr,w,h)
        surface.write_to_png(filename) 
        if sys.platform == 'win32':
            os.startfile(filename) 
        else: 
            os.system("%s '%s' &" % (opts.pngviewer,filename))


def draw_label(cr,w,h): 
    cr.identity_matrix() 
    clickops = ['click_hh','click_nn','click_bridge','click_nh','click_rr',
            'click_ss','click_rs','click_sn','ascent_star','wundersensi_star',
            'polar_star','paarwabe_plot','crown_comp',
            'dyn_cuad2','click_hn','subject_click'] 
    sheetopts = ['dat_nat', 'dat_nod', 'dat_house', 'prog_nat', 'prog_nod', 
            'prog_local', 'prog_soul' ]

    if curr.curr_op in clickops or (curr.clickmode == 'click' and curr.opmode != 'simple'): 
        d_name(cr,w,h,kind='click')
    elif curr.curr_op in ['compo_one','compo_two']:
        compo_name(cr,w,h)
    elif curr.curr_op not in sheetopts:
        d_name(cr,w,h)

def compo_name(cr,w,h):
    layout = cr.create_layout()
    font = pango.FontDescription(opts.font)
    font.set_size(int(7*pango.SCALE*minim*0.9*MAGICK_SCALE))
    layout.set_font_description(font)
    h *= 0.995
    mastcol = (0.8,0,0.1)
    clickcol = (0,0,0.4)    
    mastname = "%s %s" % (curr.curr_chart.first,curr.curr_chart.last)
    clickname = "%s %s" % (curr.curr_click.first,curr.curr_click.last)
    cr.set_source_rgb(*mastcol)
    layout.set_alignment(pango.ALIGN_RIGHT) 
    layout.set_text(clickname)
    ink,logical = layout.get_extents()
    xpos = logical[2]/pango.SCALE
    ypos = logical[3]/pango.SCALE
    cr.move_to(w-xpos-30,h-ypos)
    cr.show_layout(layout)
    cr.set_source_rgb(*clickcol)
    layout.set_alignment(pango.ALIGN_LEFT) 
    layout.set_text(mastname) 
    ypos = logical[3]/pango.SCALE
    cr.move_to(30,h-ypos)
    cr.show_layout(layout)

def d_name(cr,w,h,kind='radix'):
    layout = cr.create_layout()
    font = pango.FontDescription(opts.font)
    font.set_size(int(7*pango.SCALE*minim*MAGICK_SCALE))
    layout.set_font_description(font)
    h *= 0.995
    
    mastcol = (0,0,0.4)
    clickcol = (0.8,0,0.1)
    mastname = "%s %s" % (curr.curr_chart.first,curr.curr_chart.last)
    clickname = "%s %s" % (curr.curr_click.first,curr.curr_click.last)
    
    if kind == "click":
        mastcol, clickcol = clickcol, mastcol
        mastname, clickname = clickname, mastname
        date,time = parsestrtime(curr.curr_click.date)
        date = date + " " + time.split(" ")[0]
        geodat = curr.format_longitud(kind='click') + " " + curr.format_latitud(kind='click')
        loc = curr.curr_click.city + " (" + t(curr.curr_chart.country)[0] + ") "
        text = "\n" + date + "\n"  + loc + geodat
    else:
        date,time = parsestrtime(curr.curr_chart.date)
        date = date + " " + time.split(" ")[0]
        geodat = curr.format_longitud() + " " + curr.format_latitud()
        loc = curr.curr_chart.city + " (" + t(curr.curr_chart.country)[0] + ") "
        text = "\n" + date + "\n"  + loc + geodat

    cr.set_source_rgb(*mastcol)
    
    layout.set_alignment(pango.ALIGN_RIGHT) 
    layout.set_text(mastname+text)
    ink,logical = layout.get_extents()
    xpos = logical[2]/pango.SCALE
    ypos = logical[3]/pango.SCALE
    cr.move_to(w-xpos-5,h-ypos)
    cr.show_layout(layout)

    if kind == 'click':
        cr.set_source_rgb(*clickcol)
        layout.set_alignment(pango.ALIGN_LEFT) 
        date,time = parsestrtime(curr.curr_chart.date)
        date = date + " " + time.split(" ")[0]
        geodat = curr.format_longitud() + " " + curr.format_latitud()
        loc = curr.curr_chart.city + " (" + t(curr.curr_chart.country)[0] + ") "
        text = "\n" + date + "\n"  + loc + geodat
        layout.set_text(clickname+text)
        
        ypos = logical[3]/pango.SCALE
        cr.move_to(0+5,h-ypos)
        cr.show_layout(layout)
