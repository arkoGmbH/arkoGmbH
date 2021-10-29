import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt


# In order to embed matplot lib into tk interface
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


#window = tk.Tk()
#window.title("Ultrastruct")
#window.geometry('1000x1000')
# Add ultrastuct logo
# LogoImage= tk.PhotoImage(file=r"/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/549_Funktionen_Berechnung/07_TrägheitsTool/PythonProject/UltrastructLogo.png")
# Logo=tk.Label(window, image=LogoImage)

#---- Add the Chart to the FUI ------------------------------------------------------
root = tk.Tk()
root.wm_title("Ultrastruct")
# Adjust size
root.geometry( "1000x1000" )

# Abstände der einzelnen Elemte
options = {'sticky':'W','padx': 0, 'pady': 1} # Weil es bei verschiedenen Funktionen ein parameter ist benötigt man **

fig = Figure(figsize=(6, 4), dpi=100)
t = np.arange(0, 3, .01)
t1 = np.array([0,40,40,0,0])
t2 = np.array([0,0,40,40,0])
#fig.add_subplot().plot(t, 2 * np.sin(2 * np.pi * t))
fig.add_subplot().plot(t1, t2)
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()



# Insert drop down value into filed
def InsertSomewhere():
    #DPlbl.config( text = DPValue.get() )
    Ys0Field.delete(0,tk.END)
    Ys0Field.insert( 0,DPValue.get() )
    return

# pack_toolbar=False will make it easier to use a layout manager later on.
#toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
#toolbar.update()

canvas.mpl_connect(
    "key_press_event", lambda event: print(f"you pressed {event.key}"))
canvas.mpl_connect("key_press_event", key_press_handler)

#toolbar.pack(side=tk.BOTTOM, fill=tk.X)
#canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
canvas.get_tk_widget().grid(row=13, column=0,columnspan = 10, rowspan = 5)



def InsertValue():
    #lbl.configure(text="Close Window")
    temp="Babaa"+HField.get()
    HField.insert(0, temp)     #insert new data in a  field
    #Hlbl.configure(text=temp) to change the text in a label
    print(HField.get())
    #window.destroy()


# Titel Label
DPlbl= tk.Label( root , text = "Profildefinition", font=("Arial", 25) )
DPlbl.grid(row=0, column=0, **options)

# Bei Höhe einfügen
btn = tk.Button(master=root, text="Werte ermitteln",    width=11, height=3, bg="blue", fg="black", command=InsertValue)
#btn.pack(side=tk.TOP)
btn.grid(row=5, column=3, **options)


#Höhe
Hlbl= tk.Label(master=root,text='Höhe [mm]')
Hlbl.grid(row=5, column=0, **options)
HField = tk.Entry(master=root,width=10)
HField.grid(row=5, column=1, **options)

#Breite
Blbl= tk.Label(master=root,text="Breite [mm]",)
Blbl.grid(row=6, column=0, **options)
BField = tk.Entry(master=root,width=10)
BField.grid(row=6, column=1, **options)

#Xs0
Xs0lbl= tk.Label(master=root,text="Xs0 [mm]",)
Xs0lbl.grid(row=7, column=0, **options)
Xs0Field = tk.Entry(master=root,width=10)
Xs0Field.grid(row=7, column=1, **options)

#Ys0
Ys0lbl= tk.Label(master=root,text="Ys0 [mm]",)
Ys0lbl.grid(row=8, column=0, **options)
Ys0Field = tk.Entry(master=root,width=10)
Ys0Field.grid(row=8, column=1, **options)




# Dropdown menu options
DPoptions = [
    "S235JR",
    "1.4301",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]
# Material dropdown 
# datatype of menu text
DPValue = tk.StringVar()  
# initial menu text
DPValue.set( "S235JR" )

# Create Dropdown menu
DP = tk.OptionMenu( root , DPValue , *DPoptions )
DP.grid(row=28, column=0, **options)

# Button to insert DP value into field
CB_Inp = tk.Button( root ,width=11, height=3, text = "Übernehmen", command = InsertSomewhere )
CB_Inp.grid(row=28, column=1, **options)


tk.mainloop()


#entry = tk.Entry(fg="Black", bg="white", width=50)
#  .pack() verwenden um das Objekt anzuzeigen
#lbl.pack() # Tkinter sizes the window as small as it can while still fully encompassing the widget. Now execute the following:
#button.pack()
#entry.pack()

#name = entry.get()
#entry.insert(0, "Real ")

#window.destroy() In order to close the window when finished

#Source
#https://likegeeks.com/python-gui-examples-tkinter-tutorial/
#https://docs.python.org/3/library/tk.html