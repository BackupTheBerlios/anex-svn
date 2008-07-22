# -*- coding: utf-8 -*-

import os
import gtk, gobject
import cairo, pango
from .. extensions.path import path

boss = None

class IniEditor(gtk.Window):
    def __init__(self,parent):
        global boss
        boss = parent.boss
        gtk.Window.__init__(self)
        self.set_type_hint(gtk.gdk.WINDOW_TYPE_HINT_DIALOG)
        self.set_transient_for(parent)
        self.set_destroy_with_parent(True)
        self.set_resizable(True)
        self.set_title(_("Editor cfg.ini"))

        vbox = gtk.VBox()
        vbox.set_border_width(6)
        sw = gtk.ScrolledWindow()
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        textview = gtk.TextView()
        textview.modify_bg(gtk.STATE_NORMAL,gtk.gdk.color_parse("#000")) 
        textbuffer = textview.get_buffer()
        sw.add(textview)
        vbox.pack_start(sw)

        cfgfile = path.joinpath(boss.opts.home_dir,'cfg.ini')
        infile = open(cfgfile, "r")

        if infile:
            string = infile.read()
            infile.close()
            textbuffer.set_text(string)
            print string


        self.add(vbox)        
        self.set_default_size(480,520)
        self.connect('destroy', self.cb_exit)
        self.show_all()


    def cb_exit(self,e):
        self.destroy() 
        return False
