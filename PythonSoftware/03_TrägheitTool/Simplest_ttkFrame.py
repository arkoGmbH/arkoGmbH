# Information from: https://www.pythontutorial.net/tkinter/tkraise/
# Notebook: https://www.pythontutorial.net/tkinter/tkinter-notebook/
# ttk Style: https://stackoverflow.com/questions/54476511/setting-background-color-of-a-tkinter-ttk-frame
# Scrollbar: https://www.pythontutorial.net/tkinter/tkinter-scrollbar/
# Notebook docu: https://docs.python.org/3/library/tkinter.ttk.html#notebook
# Gutes tab handling Beispiel: https://www.homeandlearn.uk/python-database-form-tabs3.html
# ttk labels: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/ttk-Label.html


import tkinter as tk # gesamtes tk also tk
from tkinter import ttk # Es wird ttk importiert, sodas man nicht tk.ttk schreiben muss
import tkinter.font as tkFont

# Define a tk window
window = tk.Tk() 
window.title("Ultrastruct") 
window.config(bg='#FFFAFA')
window.geometry('1024x800')


# Menu items oben nach dem Apfel
menubar = tk.Menu(window) 
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

# Menu items hinzufügen
window.config(menu=menubar)

# Change the window grid to something more usefull?!
rows = 0
while rows<50:
    window.rowconfigure(rows,weight=1)
    window.columnconfigure(rows, weight=1)
    rows +=1

#creation of mainframe as notebook. Im notebook werden immer alle neue Frames als Tab hinzugefügt
mainframe = ttk.Notebook(window,width=50)

# On tab change behaviour
def on_tab_selected(event):
    #selected_tab = event.widget.select()
    #tab_text = event.widget.tab(selected_tab, "text")
    print(mfr.tab(mfr.select(), "text"))

# Define main frame
mfr = ttk.Notebook(window)

# create frame style
s= ttk.Style(mainframe)
# Default style
s.configure('new.TFrame', background='green')

tab1 = ttk.Frame(mfr)
tab2 = ttk.Frame(mfr)
tab3 = ttk.Frame(mfr)

#NamedFrames = {}

#NamedFrames['tab1'] = tab1
#NamedFrames['tab2'] = tab2

# Assigning a function to an event of a widget is called event binding.
# When the event occurs, the assigned function is invoked automatically.
# On tab selection behaviour
# Example: widget.bind(event, handler, add=None)  in our case the event is <<NotebookTabChanged>> and the handler is the function on_tab_selected
mfr.bind("<<NotebookTabChanged>>", on_tab_selected)

mfr.add(tab1, text ='Projekte')
mfr.add(tab2, text ='Fenster')
mfr.add(tab3, text ='Details')

# Fontdefinition
fontbig = tkFont.Font(size=25)

lblProj=ttk.Label(tab1, text ="Übersicht aller Projekte", font=fontbig)
lblProj.grid(column = 0, row = 0,padx = 30,pady = 30)

# Input field
w = ttk.Entry(tab1,font=fontbig,width=10)
w.insert(0,45)
w.grid()

def PrintTabName():
    '''Show a frame for the given page name'''
    # print( mfr.tab(tab2)['text']) tab2 name
    print(mfr.tab(mfr.select(), "text"))
    a=float(w.get())
    print(a)
    #w.insert(0,a)
    # New top level window

    # Toplevel widgets work as windows that are directly managed by the window manager.
    #  They do not necessarily have a parent widget on top of them.
    new = tk.Toplevel()
    tab2.tkraise()
    print('done')
    #NamedFrames['tab2'].tkraise()

# Button
bn1=ttk.Button(tab1,text='Analysieren',command=PrintTabName)
bn1.grid()

ttk.Label(tab2,
          text ="Übersicht aller Fenster").grid(column = 0,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)
# maninframe anzeigen
mfr.grid(row=1,column=2,columnspan=45,rowspan=43,sticky='NESW')




window.mainloop()

