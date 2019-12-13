
# livrarias especificas

try:
    from Tkinter import *
except ImportError:
    from tkinter import *


class BottonPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

        try:
            self.imageEx = PhotoImage(file='images/image.gif')
            Label(self.frame, image=self.imageEx).pack(side=TOP, fill=BOTH)


        except:
            print("Image not found")