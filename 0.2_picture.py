"""adding a picture in gui"""

from tkinter import *

root = Tk()
root.title("Using a label to place an image")

# creating a reference to the image
landscape_image = PhotoImage(file="aesthetic-japan.gif")

# Placing the image into the label
image_label = Label(root, image=landscape_image)
image_label.pack()

# Adding text below the label
text_label = Label(root, text="Feel the temperature drop in the pink night",
                   font=("Biome", 25, "bold"), fg="#ed77a0")
text_label.pack()

root.mainloop()
