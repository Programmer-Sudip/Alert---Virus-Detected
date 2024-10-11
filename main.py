# Import neccesary libraries
from tkinter import*
from tkinter import messagebox

# setup Tkinter window
root =Tk()
root.geometry("200x200")

# Function for Displaying warning message
# This will be called once the button is clicked
# messagebox.showwarning("Warning Name", "Text to be displayed")
def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

# Adding Button widget to window
button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)

# Entering main event loop
root.mainloop()