import tkinter as tk # gesamtes tk also tk
from tkinter import ttk
import numpy as np
# In order to embed matplot lib into tk interface
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure



def demo():
    #root = tk.Tk()
    schedGraphics = tk
    root = schedGraphics.Tk()

    root.title("Ultrastruct")
    universal_height = 606

    nb = ttk.Notebook(root)

    # adding Frames as pages for the ttk.Notebook
    # first page, which would get widgets gridded into it
    page1 = ttk.Frame(nb, width= 300,height = universal_height)
    # second page
    page2 = ttk.Frame(nb,width = 300,height = universal_height)

    nb.add(page1, text='One')
    nb.add(page2, text='Two')

    nb.grid(column=0)

    day_label = schedGraphics.Label(page1, text="Day1:")
    day_label.pack()
    day_label.place(x=0, y=30)

    day_label = schedGraphics.Label(page2, text="Day2:")
    day_label.pack()
    day_label.place(x=0, y=30)



    canvas = schedGraphics.Canvas(root, width=900, height=universal_height)
    canvas.create_rectangle(50, 500, 300, 600, fill="red")
    canvas.grid(column=1, row=0)
 

    root.mainloop()

if __name__ == "__main__":
    demo()