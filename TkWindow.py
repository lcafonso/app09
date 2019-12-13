# livrarias especificas


try:
    import Tkinter as tk
    #import ttk
    from Tkinter import *

except ImportError:
    import tkinter as tk
    #import tkinter.ttk as ttk
    from tkinter import *

from LeftPanel import *
from TopPanel import *
from CenterPanel import *
from RightPanel import *
from BottonPanel import *

__title__ = "TkWindow"
__version__ = "1.0.0"
__author__ = "LAfonso"

ALL = tk.N+tk.S+tk.W+tk.E

#class da janela principal
class TkWindow:
    def __init__(self):
        self.root = tk.Tk()
        # Dimensionando a janela principal
        w = 1900
        h = 1080
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = int((sw - w) / 2)
        y = int((sh - h) / 2)
        # Construindo a janela
        self.root.wm_title("Window Title")
        self.root.config(background="#FFFFFF")
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # Grid 5x3
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        # Frame esquerda
        self.leftFrame = Frame(self.root, highlightbackground="gray", highlightcolor="white", highlightthickness=1)
        self.leftFrame.grid(row=0, column=0, rowspan=2, columnspan=2, padx=2, pady=2, sticky=ALL)
        Label(self.leftFrame, text="Ficheiros", bg="gray68", fg="white").pack(fill=X)

        # Frame centro cima
        self.topFrame = Frame(self.root, highlightbackground="gray", highlightcolor="white", highlightthickness=1)
        self.topFrame.grid(row=0, column=2, columnspan=2, padx=2, pady=2, sticky=ALL)
        Label(self.topFrame, text="Origem", bg="gray68", fg="white").pack(fill=X)

        # Frame centro baixo
        self.centerFrame = Frame(self.root, highlightbackground="gray", highlightcolor="white", highlightthickness=1)
        self.centerFrame.grid(row=1, column=2, columnspan=2,padx=2, pady=2, sticky=ALL)
        Label(self.centerFrame, text="Destino", bg="gray68", fg="white").pack(fill=X)

        # Frame direita
        self.rightFrame = Frame(self.root, highlightbackground="gray", highlightcolor="white", highlightthickness=1)
        self.rightFrame.grid(row=0, column=4, padx=2,rowspan=2, pady=2, sticky=ALL)
        Label(self.rightFrame, text="Tools", bg="gray68", fg="white").pack(fill=X)

        # Frame embaixo
        self.bottonFrame = Frame(self.root, highlightbackground="gray", highlightcolor="white", highlightthickness=1)
        self.bottonFrame.grid(row=2, column=0, columnspan=5, padx=2, pady=2, sticky=ALL)
        Label(self.bottonFrame, text="Selecionados", bg="gray68", fg="white").pack(fill=X)

        self.leftPanel = LeftPanel(self.root, self.leftFrame)
        self.topPanel = TopPanel(self.root, self.topFrame)
        self.centerPanel = CenterPanel(self.root, self.centerFrame)
        self.rightPanel = RightPanel(self.root, self.rightFrame)
        self.bottomPanel = BottonPanel(self.root, self.bottonFrame)

    def start(self):
        self.root.mainloop()