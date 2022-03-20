"""intro to dropdown menus"""

from tkinter import *


# change the label text
def show():
    label.config(text=f"You choose {clicked.get()}")


# set up the interface
root = Tk()
root.title("Dropdown menus")
root.geometry("300x90")

# Dropdown menu options
options = ["Cheese", "Beef", "Chicken", "Egg", "Lettuce", "Tomato", "Avocado"]

clicked = StringVar()

# Initial menu to 'clicked' button above
clicked.set("Choose filling...")

# Send dropdown menu to 'clicked' button above
choice = OptionMenu(root, clicked, *options)  # includes whole option list
choice.pack()

# Create button, to change label text
select_button = Button(root, text="click to confirm", command=show).pack()

# Create ;abel to hold the option chosen
label = Label(root, text="Choice will appear here")
label.pack()

root.mainloop()
