from tkinter import *
# import tkinter.ttk import *

from plotdata import regression_plot
from stats import stats_columns


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.b = Button(master, text="Blammo!", command=lambda: self.onClick())
        self.b.pack()

    def onClick(self):
        anotherWindow=Application(self.master)
        anotherWindow.pack()


root = Tk()
app = Application(master=root)
app.mainloop()
