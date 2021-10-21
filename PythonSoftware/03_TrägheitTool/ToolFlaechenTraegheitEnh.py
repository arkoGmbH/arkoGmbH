# Information from: https://www.pythontutorial.net/tkinter/tkraise/
# Notebook: https://www.pythontutorial.net/tkinter/tkinter-notebook/
# ttk Style: https://stackoverflow.com/questions/54476511/setting-background-color-of-a-tkinter-ttk-frame
# Scrollbar: https://www.pythontutorial.net/tkinter/tkinter-scrollbar/
# Notebook docu: https://docs.python.org/3/library/tkinter.ttk.html#notebook
# Gutes tab handling Beispiel: https://www.homeandlearn.uk/python-database-form-tabs3.html
# ttk labels: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/ttk-Label.html
# Complete APP with popup and navigation: https://python-forum.io/thread-12435.html
# /Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/549_Funktionen_Berechnung/07_TrägheitsTool/PythonProject/env/bin/python


import tkinter as tk # gesamtes tk also tk
from tkinter import ttk # Es wird ttk importiert, sodas man nicht tk.ttk schreiben muss
import tkinter.font as tkFont


class Root(tk.Tk):
    def __init__(self):
        # Initialise with tk.TK __init__ method
        super(Root, self).__init__()
        self.title("Ultrastruct")
        self.minsize(800, 600)
        self.configure(background="white")
        
        # Add the dropdown menus
        self.createMenu()

        # Create user interface with tabs
        tabControl = ttk.Notebook(self)

        self.tab1 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text="Projekte")
        tk.Label(self.tab1, text= "Anal" ).place(x= 250, y= 20)
        Analyiseren = tk.Button(self.tab1, text="Analysieren", command=lambda: self.ToTab2()).place(x=520, y=320)
  
        self.tab2 = ttk.Frame(tabControl)
        tabControl.add(self.tab2, text="Fenster")
        tk.Label(self.tab2, text= "Please Select your choice" ).place(x= 250, y= 20)
        submit = tk.Button(self.tab2, text="Back to tab1", command=lambda: self.ToTab1()).place(x=520, y=320)
        # Create the 
        #self.BtnOnTab2()
  
        self.tab3 = ttk.Frame(tabControl)
        tabControl.add(self.tab3, text="Details")
        NewWindow = tk.Button(self.tab3, text="New", command=lambda: self.NewWindow()).place(x=520, y=320)


        # Fontdefinition
        fontbig = tkFont.Font(size=25)

        lblProj=ttk.Label(self.tab1, text ="Übersicht aller Projekte", font=fontbig)
        lblProj.grid(column = 0, row = 0,padx = 30,pady = 30)

        # Input field
        w = ttk.Entry(self.tab1,font=fontbig,width=10)
        w.insert(0,45)
        w.grid()


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

    # On tab change behaviour
    def on_tab_selected(event):
        #selected_tab = event.widget.select()
        #tab_text = event.widget.tab(selected_tab, "text")
        print(mfr.tab(mfr.select(), "text"))
  
        # Assigning a function to an event of a widget is called event binding.
        # When the event occurs, the assigned function is invoked automatically.
        # On tab selection behaviour
        # Example: widget.bind(event, handler, add=None)  in our case the event is <<NotebookTabChanged>> and the handler is the function on_tab_selected
        mfr.bind("<<NotebookTabChanged>>", on_tab_selected)

    def PrintTabName():
        '''Show a frame for the given page name'''
        # print( mfr.tab(tab2)['text']) tab2 name
        print(mfr.tab(mfr.select(), "text"))
        a=float(w.get())
        #w.insert(0,a)
        # New top level window

        # Toplevel widgets work as windows that are directly managed by the window manager.
        #  They do not necessarily have a parent widget on top of them.
        #new = tk.Toplevel()
        print('done')
        #NamedFrames['tab2'].tkraise()

    # go back to specific tab
    def ToTab2(self):
            #ttk.Notebook.select(self.tab7)
            self.tab_control.select(self.tab2)


# Istantiate the App
root = Root()
# Wait for actions
root.mainloop()


