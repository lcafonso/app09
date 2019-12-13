import os, sys
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

ALL = tk.N+tk.S+tk.W+tk.E

def Example(parent, list):
    w = Frame(parent,width=200, height=576)

    text = tk.Text(w, wrap="none")
    vsb = tk.Scrollbar(orient="vertical", command=text.yview)
    text.configure(yscrollcommand=vsb.set)
    vsb.pack(side="right", fill="y")
    text.pack(fill="both", expand=True)


    for i in list:
        idx = list.index(i)
        print(idx)

        img1 = Image.open('thumbs/'+i).convert('RGBA')
        useImg1 = ImageTk.PhotoImage(img1)
        Button(w, image=useImg1, width=64, height=64, command=callback).grid(row=0, column=idx , padx=4, pady=4, sticky=ALL)





def callback():
    print('press')


if __name__ == "__main__":
    root = tk.Tk()

    image_list = []
    image_list = next(os.walk('thumbs'))[2]

    Example(root,image_list)

    root.mainloop()