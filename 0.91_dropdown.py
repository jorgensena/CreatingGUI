"""exercise with dropdown menus"""

from tkinter import *
root = Tk()


class Option:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        fillings.append(self)


# change the label text
def generate_options():
    choices = []
    for filling in fillings:
        choices.append(f"{filling.name} ${filling.price:.2f}")
    return choices


def exit_program():
    root.destroy()


# set up the interface
root.title("Sandwich fillings")
root.geometry("300x90")
fillings = []

# Dropdown menu options
Option("Cheese", 2.5)
Option("Beef", 3.5)
Option("Chicken", 3)
Option("Egg", 1.5)
Option("Lettuce", 1)


label_text = StringVar()
option_choices = generate_options()

# Initial menu text - dropdown comes from here
label_text.set("Choose filling...")

# Send dropdown menu to 'clicked' button above
option = OptionMenu(root, label_text, *option_choices).pack()

# Create ;abel to hold the option chosen
label = Label(root, textvariable=label_text).pack()

# Create button, to change label text
exit_button = Button(root, text="Exit program", command=exit_program).pack()


root.mainloop()
