
# livrarias especificas
import os
import sys
sys.path.insert(1, '/home/afonso/PycharmProjects/BeeGUI')
from ttkwidgets import CheckboxTreeview

from tkinter import *
import tkinter.ttk as ttk
import tkinter.filedialog as tkFileDialog
from  PIL import Image, ImageTk

ALL = N+S+W+E

class LeftPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = Frame(frame)

        # Create the toolbar as a frame

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.grid_rowconfigure(1, minsize=70)

        self.img1 = Image.open("icons/open-folder.png").convert('RGBA')
        self.useImg1 = ImageTk.PhotoImage(self.img1)

        self.path = os.path.dirname(__file__)

        #self.style = ttk.Style()
        #self.style.configure('Treeview', rowheight=40)
        self.tree =  CheckboxTreeview(self.frame)

        #self.tree.pack(expand=YES, fill=BOTH)
        self.tree.heading("#0", text="Ficheiros")

        self.dir = self.tree.insert('', 'end', text=self.path, open=True)
        self.Subs(self.path, self.dir)


        self.tree.grid(row=0, column=0, columnspan=2, padx=4, pady=4, sticky=ALL)

        Button(self.frame, image=self.useImg1, width=70, height=70, command=self.browse_button).grid(row=2, column=1, padx=4, pady=4, sticky=E)

        self.frame.pack(side=TOP, fill=BOTH)

    def Subs(self, path, parent):
        for p in os.listdir(path):
            abspath = os.path.join(path, p)
            parent_element = self.tree.insert(parent, 'end', text=p, open=True)
            if os.path.isdir(abspath):
                self.Subs(abspath, parent_element)

    def browse_button(self):
        self.path = tkFileDialog.askdirectory()


    def set_dir(self):
        sourcePath = str(self.path)
        os.chdir(sourcePath)