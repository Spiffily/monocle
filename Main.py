#!/bin/env python3
from os import * # Import bash run abilities
from os.path import expanduser
home = expanduser("~")

import gi # Import GTK Stuff
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

class HomeWindow(Gtk.ApplicationWindow):
    def __init__(self):
        # Construct window
        Gtk.Window.__init__(self, title="Monocle")
        # self.set_border_width(3)
        system("mkdir ~/.local/share/monocle")
        system("mkdir ~/.monocle")

        self.appdata = home+"/.local/share/monocle/"
        self.nbpath = home+"/.monocle/"

        # HomeWindow inherits the set_wmclass method from Gtk.ApplicationWindow
        self.set_wmclass("Monocle", "Monocle")

        self.head = Gtk.HeaderBar.new()
        self.head.set_title("Monocle")
        self.head.set_show_close_button(True)
        self.set_titlebar(self.head)

        # self.selectednb = nbpath+appstate.??[1]

    def init(self):
        self.sectionnb = Gtk.Notebook.new()
        self.sections = []

        #Notebook
        self.nblist = listdir(self.nbpath)
        if not self.nblist:
            self.nblist = self.nblist+["isempty"]
        else:
            self.selectednb = self.nblist[0]


        #Make Sections widgets
        self.seclist = listdir(self.nbpath+self.selectednb)
        print("Sections in selected notebook "+self.selectednb+":")
        print(self.seclist)
        if not self.seclist:
            self.seclist = self.seclist+["isemptynotebook"]
        else:
            for sec in self.seclist:
                # sec = Gtk.Notebook.new()
                name = sec
                secwid = SectionWidget(name, self.appdata, self.nbpath, self.selectednb)
                secwidname = secwid.init(name, self.appdata, self.nbpath, self.selectednb)
                self.sections = self.sections+[secwidname]

        #Set nb gtk.notebook widget up (top level nb widget)
        if "isemptynotebook" in self.seclist:
            emptnb = Gtk.Image.new()
            emptnb.set_from_file(self.appdata+"walls"+"/bionic.png")
            emptlab = Gtk.Label.new("No sections yet!")
            self.sectionnb.insert_page(emptnb, emptlab, -1)
        else:
            k=0                            # Add the pages to top level nb widget
            for sec in self.seclist:
                secwid = self.sections[k]
                seclab = Gtk.Label.new(sec)
                self.sectionnb.insert_page(secwid, seclab, -1)
                k=k+1
     

        self.add(self.sectionnb)

class SectionWidget():
    def __init__(self, name, appdata, nbpath, selectednb):
        self.name = name
        self.appdata = appdata
        self.nbpath = nbpath
        self.selectednb = selectednb
        self.pages = Gtk.Notebook.new()

        self.pglist = listdir(self.nbpath+self.selectednb+"/"+self.name)

    def init(self, name, appdata, nbpath, selectednb):
        print("Pages in section "+name+":")
        print(self.pglist)
        if not self.pglist:
            self.pglist = self.pglist+["isemptysection"]
            
            print("Empty Section")
            emptsec = Gtk.Image.new()
            emptsec.set_from_file(self.appdata+"walls"+"/bionic.png")
            emptlab = Gtk.Label.new("No pages here yet!")
            self.pages.insert_page(emptsec, emptlab, -1)
        else:
            for pg in self.pglist:
                pgwid = Gtk.Image.new()
                pgwid.set_from_file(self.appdata+"tuxmonocle.png")
                pglab = Gtk.Label.new(pg)
        
                self.pages.insert_page(pgwid, pglab, -1)

        self.pages.set_tab_pos(Gtk.PositionType.LEFT)        
        return self.pages
    
    # def 

win = HomeWindow()
win.init()

win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()