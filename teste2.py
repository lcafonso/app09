from Tkinter import *
from ttk import *
import os, sys
from PIL import ImageTk, Image

class VerticalScrolledFrame(Frame):
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                       anchor=NW)

        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)




class SampleApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        b = Button(self, text="Open a new window", command=self.open_new)
        b.pack()

    def open_new(self):
        top = Toplevel()
        self.frame = VerticalScrolledFrame(top)
        self.frame.pack()

        def Print():
            print "print function"

        #button = Button(self.frame, text="Compare",command = Print)
        #button.pack(side=LEFT)
        image_list = []
        image_list = next(os.walk('thumbs'))[2]

        size = 64, 64
        buttons = []
        for i in image_list:
            idx = image_list.index(i)
            img1 = Image.open('thumbs/' + i).convert('RGBA')
            img1.thumbnail(size, Image.ANTIALIAS)
            useImg1 = ImageTk.PhotoImage(img1)
            buttons.append(Button(self.frame, image=useImg1))
            buttons[idx].pack()





if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()