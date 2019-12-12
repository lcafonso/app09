
# livrarias especificas

try:
    import Tkinter as tk
    from Tkinter import *
except ImportError:
    import tkinter as tk
    from tkinter import *

ALL = tk.N+tk.S+tk.W+tk.E

class TopPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

        try:
            self.imageEx = PhotoImage(file='images/image.gif')
            Label(self.frame, image=self.imageEx).pack()

        except:
            print("Image not found")