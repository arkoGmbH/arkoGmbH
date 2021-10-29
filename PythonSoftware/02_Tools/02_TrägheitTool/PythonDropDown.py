# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry( "200x200" )

# Change the label text
def InsertToLabel():
	label.config( text = DPValue.get() )

# Dropdown menu options
options = [
	"Monday",
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday",
	"Saturday",
	"Sunday"
]

# datatype of menu text
DPValue = StringVar()

# initial menu text
DPValue.set( "Monday" )

# Create Dropdown menu
drop = OptionMenu( root , DPValue , *options )
drop.pack()

# Create button, it will change label text
button = Button( root , text = "click Me" , command = InsertToLabel ).pack()

# Create Label
label = Label( root , text = " " )
label.pack()

# Execute tkinter
root.mainloop()
