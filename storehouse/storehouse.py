#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# storehouse.py - a simple inventory management software.
# (c) 2016 - Jesus Vedasto Olazo - jessie@jestoy.frihost.net


import Tkinter as tk
import ttk
import sys


__version__ = '1.0.0'

class MainWindow(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.geometry('300x200+100+100')
        self.parent.title(' - '.join(['StoreHouse', __version__]))
        self.parent.protocol('WM_DELETE_WINDOW', self.quitApp)
        self.createGui()
        self.show()

    def show(self):
        self.pack(expand=True, fill='both')

    def createGui(self):
        menubar = tk.Menu(self.parent)
        self.parent.config(menu=menubar)
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='Quit', command=self.quitApp)

    def quitApp(self):
        self.parent.destroy()


def main():
    app = tk.Tk()
    MainWindow(app)
    app.mainloop()

if __name__ == '__main__':
    main()

