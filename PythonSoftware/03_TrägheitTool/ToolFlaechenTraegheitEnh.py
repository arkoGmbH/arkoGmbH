# Information from: https://www.pythontutorial.net/tkinter/tkraise/
# Notebook: https://www.pythontutorial.net/tkinter/tkinter-notebook/
# ttk Style: https://stackoverflow.com/questions/54476511/setting-background-color-of-a-tkinter-ttk-frame
# Scrollbar: https://www.pythontutorial.net/tkinter/tkinter-scrollbar/
# Notebook docu: https://docs.python.org/3/library/tkinter.ttk.html#notebook
# Gutes tab handling Beispiel: https://www.homeandlearn.uk/python-database-form-tabs3.html
# ttk labels: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/ttk-Label.html
# Complete APP with popup and navigation: https://python-forum.io/thread-12435.html
# /Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/549_Funktionen_Berechnung/07_TrägheitsTool/PythonProject/env/bin/python


#from _typeshed import Self
import tkinter as tk # gesamtes tk also tk
from tkinter import ttk # Es wird ttk importiert, sodas man nicht tk.ttk schreiben muss
import tkinter.font as tkFont
import os

# Maths and plotting
import numpy as np
import matplotlib.pyplot as plt

# In order to embed matplot lib into tk interface
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

# User defined libraries form the current file path
#   Current file path: os.path.realpath(__file__)
#   Current directory of file: os.path.abspath(os.path.dirname(__file__))
os.chdir(os.path.abspath(os.path.dirname(__file__)))
from SQLiteBasics import TableExists

# Set again the directory to the env
os.chdir("/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/549_Funktionen_Berechnung/07_TrägheitsTool/PythonProject/")




# Label collection class
class LblCln():
        def __init__(self):
            self.tabname=''         # tab name to which the field belongs
            self.Labelname=''       
            self.Labelcontent=''    
            self.PosX=''            # X-Position in pixels
            self.PosY=''            # Y-Position in pixels
        # Set a password
        def _setPassword(self, password):
            self._password = password
        # Example to se the variable password notice the _set and the _password:
        # u = User()
        # u.password = 'Sarantapodarousa'

# Input Field collection collection class
class InpCln():
        def __init__(self):
            self.tabname=''         # tab name to which the field belongs
            self.Fieldname=''       # Name and label of the Button
            self.Fieldcontent=''    # Tab name on which the button belongs
            self.PosX=''            # X-Position in pixels
            self.PosY=''            # Y-Position in pixels

# Button collection class
class BtnCln(tk.Button):
        def __init__(self):
            self.Buttoname='' # Name and label of the Button
            self.tabname=''   # Tab name on which the button belongs
            self.tkButton=''  # tk.Button Objekt
            self.command=''   # Command which the button will execute
            self.PosX=''      # X-Position in pixels
            self.PosY=''      # Y-Position in pixels


# Graphic collection class
class GraCln():
        def __init__(self):
            self.tabname=''     # Tab name on which the button belongs
            self.figureObj=''   # Figure Objekt
            self.canvasObj=''   # Canvas Objekt



# Initalisieren und Beispiel
T1B1=LblCln()
T1B1.password='onmpgfasd'


class Root(tk.Tk):
    def __init__(self):
        # Initialise with tk.TK __init__ method
        super(Root, self).__init__()
        self.title("Ultrastruct")
        self.minsize(800, 700)
        self.configure(background="white")
        
        # Add the dropdown menus
        self.createMenu()

        # Create user interface with tabs
        tabControl = ttk.Notebook(self)

        # Fontdefinition
        fontbig = tkFont.Font(size=25)
        fontbutton = tkFont.Font(size=20)
        fontsmall = tkFont.Font(size=12)

        # Standard button definition
        btnw=15
        btnh=3

        # tab0 (Home) ---------------------------
        self.tab0 = ttk.Frame(tabControl)
        tabControl.add(self.tab0, text="Tools")

        # tab1 labels
        ttk.Label(self.tab0, text ="Tools", font=fontbig).place(x= 0, y= 10)

         # tab0 buttons
        tk.Button(self.tab0, text="Flächenträgheit",width=btnw,height=btnh,font=fontbutton, command=lambda: self.ToTab2()).place(x=0, y=80)
        tk.Button(self.tab0, text="Schraubengruppe",width=btnw,height=btnh,font=fontbutton, command=lambda: self.ToTab2()).place(x=0, y=180)
        tk.Button(self.tab0, text="Knicken",width=btnw,height=btnh,font=fontbutton, command=lambda: self.ToTab2()).place(x=0, y=280)
        tk.Button(self.tab0, text="Fundament",width=btnw,height=btnh,font=fontbutton, command=lambda: self.ToTab2()).place(x=0, y=380)
        tk.Button(self.tab0, text="Elastischebettung",width=btnw,height=btnh,font=fontbutton, command=lambda: self.ToTab2()).place(x=0, y=480)

        tk.Button(self.tab0, text="Balkenbiegung",width=btnw,height=btnh,font=fontbutton, command=lambda: self.ToTab2()).place(x=250, y=80)
        tk.Button(self.tab0, text="Plattenbiegung",width=btnw,height=btnh,font=fontbutton, command=lambda: self.ToTab2()).place(x=250, y=180)
        tk.Button(self.tab0, text="Freiflächen",width=btnw,height=btnh,font=fontbutton, command=lambda: self.ToTab2()).place(x=250, y=280)


        # tab1 ---------------------------
        self.tab1 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text="Projekte")
        
         # tab1 Graphics
        fig = Figure(figsize=(3, 2), dpi=100)
        t = np.arange(0, 3, .01)
        x = np.array([0, 40, 40, 55, 45,20,0,0])
        y = np.array([0, 0, 30, 30,40, 40,40,0])
        #fig.add_subplot().plot(t, 2 * np.sin(2 * np.pi * t))
        fig.add_subplot().plot(x, y)
        canvas = FigureCanvasTkAgg(fig, master=self.tab1)  # A tk.DrawingArea.
        canvas.get_tk_widget().place(x= 0, y= 250) #grid(row=10,column=2)
        canvas.draw()


        # tab1 labels
        ttk.Label(self.tab1, text ="Projekte", font=fontbig).place(x= 0, y= 10)
        ttk.Label(self.tab1, text= "Breite [mm]", font=fontsmall ).place(x= 0, y= 50)

        # tab1 Input fields
        InputField = ttk.Entry(self.tab1,font=fontbig,width=5)
        InputField.place(x= 0, y= 70)
        InputField.insert(0,45)
        

        # tab1 buttons
        ttk.Button(self.tab1, text="Komponenten", command=lambda: self.ToTab2()).place(x=520, y=320)

        #tab2 ---------------------------
        self.tab2 = ttk.Frame(tabControl)
        tabControl.add(self.tab2, text="Material")
        # tab2 Graphics
        # empty
        #tab2 labels
        tk.Label(self.tab2, text= "Please Select your choice" ).place(x= 250, y= 20)
        # tab2 Input fields
        # empty
        #tab2 Buttons
        tk.Button(self.tab2, text="Back to tab1", command=lambda: self.ToTab1()).place(x=520, y=320)

        #tab3 ---------------------------
        self.tab3 = ttk.Frame(tabControl)
        tabControl.add(self.tab3, text="Details")
        # tab3 Graphics
        # empty
        # tab3 labels
        # empty
        # tab3 Input fields
        # empty
        # tab3 buttons
        # empty
        # tab3 further behaviour
        tk.Button(self.tab3, text="New", command=lambda: self.NewWindow()).place(x=520, y=320)

       

 


        # Show the final user interface
        tabControl.pack(expand=1, fill="both")
        self.tab_control = tabControl

    # Navigation
    def ToTab1(self):
        self.tab_control.select(self.tab1)

    def ToTab2(self):
        self.tab_control.select(self.tab2)

    def ToTab3(self):
        self.tab_control.select(self.tab3)

    def createMenu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        filemenu = tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label='File',menu=filemenu)
        filemenu.add_command(label='Open')
        filemenu.add_command(label='Clear')
        filemenu.add_command(label='Save As')
        filemenu.add_separator()
        filemenu.add_command(label='Exit')

        helpmenu = tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label='Help',menu=helpmenu)
        helpmenu.add_command(label='Precuations')
        helpmenu.add_command(label='Version Info')
        helpmenu.add_command(label='Technical Support')



    def NewWindow(self):
        newTop = tk.Toplevel(self.master)
        display = tk.Label(newTop, text="Review").pack()
        newTop.title("Review and Submit")
        newTop.focus_set()
        newTop.geometry("400x600")


    # go back to specific tab
    def ToTab2(self):
            #ttk.Notebook.select(self.tab7)
            self.tab_control.select(self.tab2)


# Check if table exists within the project database
DBName='Projects.db'
TableName='stocks'
exists=TableExists(DBName,TableName)


# Istantiate the App
App = Root()
# Wait for actions
App.mainloop()


