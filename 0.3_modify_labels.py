"""modify labels by specifying geometry"""

from tkinter import *
root = Tk()

# changing the title of the window
root.title("Exercise 3 - Geometry")

# window geometry - to set size of 500px wide x 200px tail
root.geometry("600x200")  # string using 'x' not '*' - no spaces either side
root.maxsize(400, 400)  # int values - sets max resizable dimensions

# adding a label widget
computer = Label(root, bg="#73c9aa", fg="white", text="Computer",
                 font=("Times", 30, "italic"))
computer.pack(fill=X)

science = Label(root, fg="#1e6282", text="SCIENCE", font=("Biome", 30))
science.pack(fill=X)

lit = Label(root, bg="#9e3c2c", fg="#e0dd80", text="is lit",
            font=("Kigelia", 40, "bold"))
lit.pack(fill=X)

root.mainloop()
