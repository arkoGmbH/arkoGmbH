# Information from: https://www.pythontutorial.net/tkinter/tkraise/
import tkinter as tk # gesamtes tk also tk
from tkinter import ttk # Es wird ttk importiert, sodas man nicht tk.ttk schreiben muss
#from tkinter.messagebox import showerror

# widget.grid(column=0, row=0, sticky='w',  **options)

#---- Mathematische transformationen mit dem Teperaturconverter ---------------------------
# Konvertierung der Temperatur (Option mit format oder nicht)
# A static method is also a method that is bound to the class and not the object of the class
# They do not require a class instance creation. So, they are not dependent on the state of the object.
class TemperatureConverter:
    @staticmethod
    def fahrenheit_to_celsius(f, format=True):
        result = (f - 32) * 5/9
        if format:
            return f'{f} Fahrenheit = {result:.2f} Celsius'
        return result

    @staticmethod
    def celsius_to_fahrenheit(c, format=True):
        result = c * 9/5 + 32
        if format:
            return f'{c} Celsius = {result:.2f} Fahrenheit'
        return result
#--------- End mathematische Transformationen mit converter ---------------------------

#------ Radiobuttons Frame --------------------------------------------------------------------------
class ControlFrame(ttk.LabelFrame):
    #The LabelFrame widget (part of ttk), like the Frame widget, is a spatial container—a rectangular area that can contain other widgets.
    # However, unlike the Frame widget, the LabelFrame widget allows you to display a label as part of the border around the area (der text ist Teil vom border).
    
    # Definieren was passiert wei instanzierung
    def __init__(self, container):
        super().__init__(container) # super allows you to call the superclass methods, in this case the __init__ method of ttk.LabelFrame
        # Since a LabelFrame needs a container, you need to add an argument to its __init__() method and call the __init__() method of the ttk.LabelFrame
        self['text'] = 'Tool auswählen' # Titel der Radiobuttons (des CotntrolFrames)
        # Similar to a dictionary. It assignes to the key 'text' the title
        
        self.selected_value = tk.IntVar() # Instantiates a 'tkinter.IntVar' class objekt and stores it in the Radiobuttons (same for both)

        # Radiobutton F to C (Perform change_fram ob push)
        ttk.Radiobutton(self,text='Windlasttool',value=1,variable=self.selected_value, command=self.change_frame).grid(column=0, row=0, padx=5, pady=5)

         # Radiobutton C to F (Perform change_fram ob push)
        ttk.Radiobutton(self,text='Holmtool',value=2,variable=self.selected_value,command=self.change_frame).grid(column=1, row=0, padx=5, pady=5)

        #Wert der ausgewählten buttons erreicht man unter self.selected_value.get() herausgegeben wird der Wert "value"


        # The "variable" in the Radiobutton helps to update all the related items and is therefore identical for both radio buttons
        # One special quality of a control variable is that it can be shared by a number of different widgets,
        # and the control variable can remember all the widgets that are currently sharing it. 
        # This means, in particular, that if your program stores a value v into a control variable c with its c.set(v) 
        # method, any widgets that are linked to that control variable are automatically updated on the screen.

        # Radiobuttons auf im GUI platzieren
        self.grid(column=0, row=1, padx=5, pady=50, sticky='ew')

        # Initialize style
        s = ttk.Style()
        # Create style used by default for all Frames
        s.configure('TFrame', background='green')
        # Control Frames initalisation ( es werden bei de Frames gebildet)
        self.frames = {}

        # Create a 
        colour_from='Rot'
        self.frames[0] = CreateColourFrame(container,colour_from)
        self.frames[1] = CreateColourFrame(container,colour_from)

        colour_from='Blau'
        self.frames[2] = CreateColourFrame(container,colour_from)

        # Untermethode die die Frames anhand von self.selected_value.get() ändert
        self.change_frame()


    # Funktion that is used to change the frame according to the frame number
    def change_frame(self):
        # Assging to the new frame object the selected frame number ( which is store in the Variable of the Radiobutton)
        frame = self.frames[self.selected_value.get()]
        # Raise this widget in the stacking order.
        frame.tkraise()
#-----------Ende Radiobuttons-------------------------------------------------------------------------------------------


#------- Frame mit den Resultaten der Analyse ----------------------------------------------
class CreateColourFrame(ttk.Frame):   # ttk.Frame class is inherited
    # Upon class instantiation the following happens
    def __init__(self, container, colour_from): #"__init__" is a reseved method (also Funktion) in python classes. It is known as a constructor in object oriented concepts.
        super().__init__(container) #super() gives you access to methods in a superclass from the subclass that inherits from it.
        # super() alone returns a temporary object of the superclass that then allows you to call that superclass’s methods.
        # a common use case is building classes that extend the functionality of previously built classes.

        #Use the colour_from argument to show the label for the temperature.
        self.colour_from = colour_from # wird später aufgeruffen
        if colour_from =='Blau' :
            print('hallo')
            #self.configure(background='blue')
        elif colour_from =='Rot' :
            print('hallo')
            #self.configure(background='red')
        
        # field options um die Ausrichtung im Pad nach dem konvertieren hinzuzufügen
        options = {'padx': 0, 'pady': 40} # Weil es bei verschiedenen Funktionen ein parameter ist benötigt man **
        #padx, pady − How many pixels to pad widget, horizontally and vertically, outside v's borders.

        # temperature label
        self.Colourlabel = ttk.Label(self, text=self.colour_from)
        # Show the colour label
        self.Colourlabel.grid(column=0, row=0, sticky='w',  **options)



# Class named App 
class App(tk.Tk): # inherits tk.Tk class properties
    def __init__(self):
        super().__init__() # performs __init___ of superclass tk.Tk
        self.title('Simple double frame change')
        # Grösse der App definieren
        self.geometry('600x800')
        # resizable() method is used to allow Tkinter root window to change it’s size according to the users need as well we can prohibit resizing of the Tkinter window.
        self.resizable(True, True)


#---------- Run App -----------------------------------------------------

if __name__ == "__main__":
    app = App()
    ControlFrame(app)
    app.mainloop()
