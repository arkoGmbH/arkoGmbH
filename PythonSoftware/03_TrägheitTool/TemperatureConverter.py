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
        self['text'] = 'Temperature selection options' # Titel der Radiobuttons (des CotntrolFrames)
        # Similar to a dictionary. It assignes to the key 'text' the title
        
        self.selected_value = tk.IntVar() # Instantiates a 'tkinter.IntVar' class objekt and stores it in the Radiobuttons (same for both)

        # Radiobutton F to C (Perform change_fram ob push)
        ttk.Radiobutton(self,text='F to C',value=0,variable=self.selected_value, command=self.change_frame).grid(column=0, row=0, padx=5, pady=5)

         # Radiobutton C to F (Perform change_fram ob push)
        ttk.Radiobutton(self,text='C to F',value=1,variable=self.selected_value,command=self.change_frame).grid(column=1, row=0, padx=5, pady=5)

        #Wert der ausgewählten buttons erreicht man unter self.selected_value.get() herausgegeben wird der Wert "value"


        # The "variable" in the Radiobutton helps to update all the related items and is therefore identical for both radio buttons
        # One special quality of a control variable is that it can be shared by a number of different widgets,
        # and the control variable can remember all the widgets that are currently sharing it. 
        # This means, in particular, that if your program stores a value v into a control variable c with its c.set(v) 
        # method, any widgets that are linked to that control variable are automatically updated on the screen.

        # Radiobuttons auf im GUI platzieren
        self.grid(column=0, row=1, padx=5, pady=50, sticky='ew')


        # Control Frames initalisation ( es werden bei de Frames gebildet)
        self.frames = {}

        # Create a 
        unit_from='Fahrenheit'
        self.frames[0] = ConverterFrame(container,unit_from,TemperatureConverter.fahrenheit_to_celsius)

        unit_from='Celsius'
        self.frames[1] = ConverterFrame(container,unit_from,TemperatureConverter.celsius_to_fahrenheit)

        # Untermethode die die Frames anhand von self.selected_value.get() ändert
        self.change_frame()

        # Container --> he value must be a boolean. If true, it means that this window will be used as a container in which some other application will be embedded (for example, a Tk toplevel can be embedded using the -use option). The window will support the appropriate window manager protocols for things like geometry requests. The window should not have any children of its own in this application. This option may not be changed with the configure widget command. Note that -borderwidth, -padx and -pady are ignored when configured as a container since a container has no border.

    # Funktion that is used to change the frame according to the frame number
    def change_frame(self):
        # Assging to the new frame object the selected frame number ( which is store in the Variable of the Radiobutton)
        frame = self.frames[self.selected_value.get()]
        
        #type(frame)
        #reset() method to clear the entry widget and the result label when the frame is switched from one to another
        frame.reset()

        # Raise this widget in the stacking order.
        frame.tkraise()
#-----------Ende Radiobuttons-------------------------------------------------------------------------------------------


#------- Frame mit den Resultaten der Analyse ----------------------------------------------
class ConverterFrame(ttk.Frame):   # ttk.Frame class is inherited
    # Upon class instantiation the following happens
    def __init__(self, container, unit_from, converter): #"__init__" is a reseved method (also Funktion) in python classes. It is known as a constructor in object oriented concepts.
        super().__init__(container) #super() gives you access to methods in a superclass from the subclass that inherits from it.
        # super() alone returns a temporary object of the superclass that then allows you to call that superclass’s methods.
        # a common use case is building classes that extend the functionality of previously built classes.

        #Use the unit_from argument to show the label for the temperature.
        self.unit_from = unit_from # wird später aufgeruffen

        #Call the self.convert callback in the convert() method to convert a temperature from one unit to another.
        self.converter = converter
        
        # field options um die Ausrichtung im Pad nach dem konvertieren hinzuzufügen
        options = {'padx': 0, 'pady': 40} # Weil es bei verschiedenen Funktionen ein parameter ist benötigt man **
        #padx, pady − How many pixels to pad widget, horizontally and vertically, outside v's borders.

        # temperature label
        self.temperature_label = ttk.Label(self, text=self.unit_from)
        self.temperature_label.grid(column=0, row=0, sticky='w',  **options)

        # temperature input field
        self.temperature = tk.StringVar()
        self.temperature_entry = ttk.Entry(self, textvariable=self.temperature)
        self.temperature_entry.grid(column=1, row=5, sticky='w', **options)
        self.temperature_entry.focus()
        #The focus command is used to manage the Tk input focus. At any given time, one window on each display is designated as the focus window; any key press or key release events for the display are sent to that window.

        # convert button
        self.convert_button = ttk.Button(self, text='Convert')
        self.convert_button.grid(column=2, row=5, sticky='w', **options)  #Nur Falls genügend padding da ist kann geschoben werden 
        self.convert_button.configure(command=self.convert)

        # result label
        self.result_label = ttk.Label(self)
        self.result_label.grid(row=1, columnspan=3, **options)

        # add padding to the frame and show it
        self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

    # Method to convert temperature value by the use of converter method and to set the field with resutls
    def convert(self, event=None):
        """  Handle button click event
        """
        try:
            input_value = float(self.temperature.get())
            result = self.converter(input_value)
            self.result_label.config(text=result)
        except ValueError as error:
            showerror(title='Error', message=error)

    # Method to reset the tmperature entry and restult labels
    def reset(self):
        self.temperature_entry.delete(0, "end")
        self.result_label.text = ''


#Functions (def) in Python can't have the same keyword argument specified multiple times, so the keys in each dictionary used with ** must be distinct or an exception will be raised.

#------ End Results frame -----------------------------------------------------------------------------------

# Class named App 
class App(tk.Tk): # inherits tk.Tk class properties
    def __init__(self):
        super().__init__() # performs __init___ of superclass tk.Tk
        self.title('Temperature Converter')
        # Grösse der App definieren
        self.geometry('600x600')
        # resizable() method is used to allow Tkinter root window to change it’s size according to the users need as well we can prohibit resizing of the Tkinter window.
        self.resizable(True, True)


#---------- Run App -----------------------------------------------------
# The __name__ variable (two underscores before and after) is a special Python variable. It gets its value depending on how we execute the containing script
# Wenn man das script mit play lauffen läst dann ist __name__ == "__main__" sonst wäre es der Name des scripts
if __name__ == "__main__":
    app = App()
    # Construct a Ttk "Label frame" with parent master. Standardoptions: class, cursor, style, takefocus
    ControlFrame(app)
    # keep the app in the loop in order to allow user interaction
    app.mainloop()

# To show all mehtods in a class use dir(class)