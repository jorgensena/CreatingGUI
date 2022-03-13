"""widgets intro"""

from tkinter import *
# variable does not have to be called root
root = Tk()

# changing the title of the window
root.title("My first window")

# window geometry - to set size of 500px wide x 200px tail
root.geometry("600x200")  # string using 'x' not '*' - no spaces either side
root.maxsize(800, 800)  # int values - sets max resizable dimensions

# adding a label widget
welcome = Label(root, bg="#9773c9", fg="white", text="Welcome",
                font=("Times", 50, "bold"))
greeting = Label(root, fg="#9773c9", text="Wen Qi :)", font=("Arial", 40))
space = Label()
computer = Label(root, bg="#73c9aa", fg="white", text="Computer",
                 font=("Times", 30, "italic"))
science = Label(root, fg="#1e6282", text="SCIENCE", font=("Biome", 30))
lit = Label(root, bg="#9e3c2c", fg="#e0dd80", text="is lit",
            font=("Kigelia", 40, "bold"))

# need to use .pack() to show the object in the root
welcome.pack()
greeting.pack()
space.pack()
computer.pack()
science.pack()
lit.pack()

root.mainloop()
