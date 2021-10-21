# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/
# https://www.youtube.com/watch?v=oV68QJJUXTU&list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk&t=431s

import tkinter as tk
# Macht alles etwas schöner 
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)

# Starting page class 
class Apl(tk.Tk):
    # Initialisierungsfunktion
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #tk.Tk.iconbitmap(self, default="LogoTest.jpg")
        # Titel hinzufügen
        tk.Tk.wm_title(self, "Ultrastruct")
        # Logo
        tk.Tk.wm_iconbitmap(self,"LogoTest.bmp")
        # Frame erstellen
        ContFrame = tk.Frame(self)
        ContFrame.pack(side="top", fill="both", expand = True)
        self.geometry('600x400')
        self.resizable(False, False)
        
        #we used columnconfigure and rowconfigure to indicate the columns and rows we'd like to expand if there is extra space available in the window
        ContFrame.grid_rowconfigure(0, weight=1)
        ContFrame.grid_columnconfigure(0, weight=1)

        #Initialise the frame with an empty dictionary?
        self.frames = {}

        # Create the frames for the three pages
        for F in (StartPage, PageOne, PageTwo):
            frame = F(ContFrame, self) #F is everytime a class that has one frame (in this case container)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)


    def show_frame(self, cont):
        frame = self.frames[cont]
        #frame.tkraise() wird verwendet um zwischen den frames zu wechseln
        frame.tkraise()




# Starting page class        
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button = tk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()
        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

# Page one class
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

# Page two class
class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()

# Applikation starten      
app = Apl()
# Im loop bleiben um interaktionen zu erlauben 
app.mainloop()