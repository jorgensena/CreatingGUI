"""modify labels by specifying geometry 2"""

from tkinter import *
root = Tk()

# changing the title of the window
root.title("Exercise 5 - Geometry")
root.minsize(600, 400)

# adding a label widget
red = Label(root, bg="#9e3c2c", fg="white", text="RED",
                 font=("Times", 30, "italic")).pack(fill=Y, side=LEFT)

lime = Label(root, bg="#73c9aa", fg="white", text="LIME", font=("Biome", 30))\
    .pack(fill=X, side=BOTTOM)

blue = Label(root, bg="#1e6282", fg="white", text="BLUE",
            font=("Kigelia", 40, "bold")).pack(side=RIGHT, fill=BOTH, padx=30,
                                               pady=30, expand=YES)

root.mainloop()
