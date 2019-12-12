
# livrarias especificas
import sys

try:
    import Tkinter as tk
    from Tkinter import *
    import Image, ImageTk
except ImportError:
    import tkinter as tk
    from tkinter import *
    from  PIL import Image, ImageTk

ALL = tk.N+tk.S+tk.W+tk.E

class RightPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame


        # Create the toolbar as a frame
        self.toolbar = Frame(self.frame, borderwidth=2)




        self.img1 = Image.open("icons/off.png")
        self.useImg1 = ImageTk.PhotoImage(self.img1)
        self.img2 = Image.open('icons/off.png')
        self.useImg2 = ImageTk.PhotoImage(self.img2)
        self.img3 = Image.open('icons/off.png')
        self.useImg3 = ImageTk.PhotoImage(self.img3)
        self.img4 = Image.open('icons/off.png')
        self.useImg4 = ImageTk.PhotoImage(self.img4)

        self.toolbar.columnconfigure(0, weight=1)
        self.toolbar.columnconfigure(1, weight=1)
        self.toolbar.rowconfigure(0, weight=2)
        self.toolbar.rowconfigure(1, weight=2)

        Button(self.toolbar, image=self.useImg1, width=64, height=64, command=self.callback1).grid(row=0, column=0, padx=4, pady=4, sticky=ALL)
        Button(self.toolbar, image=self.useImg2, width=64, height=64, command=self.callback2).grid(row=0, column=1, padx=4, pady=4, sticky=ALL)
        Button(self.toolbar, image=self.useImg3, width=64, height=64, command=self.callback3).grid(row=1, column=0, padx=4, pady=4, sticky=ALL)
        Button(self.toolbar, image=self.useImg4, width=64, height=64, command=self.callback4).grid(row=1, column=1, padx=4, pady=4, sticky=ALL)


        self.toolbar.pack(side=TOP, fill=BOTH)




    def callback1(self):
        print("A button was pressed 1")

    def callback2(self):
        print("A button was pressed 2")

    def callback3(self):
        print("A button was pressed 3")

    def callback4(self):
        self.root.quit()
