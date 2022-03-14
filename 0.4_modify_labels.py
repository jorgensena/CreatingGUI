"""modify labels by specifying geometry 2"""

from tkinter import *
root = Tk()

# changing the title of the window
root.title("Exercise 4 - Geometry")

# adding a label widget
computer = Label(root, bg="#73c9aa", fg="white", text="Computer",
                 font=("Times", 30, "italic"))
computer.pack(fill=Y, side=LEFT)

science = Label(root, fg="#1e6282", text="SCIENCE", font=("Biome", 30))
science.pack(fill=Y, side=RIGHT)

lit = Label(root, bg="#9e3c2c", fg="#e0dd80", text="is lit",
            font=("Kigelia", 40, "bold"))
lit.pack(fill=Y)

root.mainloop()
