"""buttons introduction"""

from tkinter import *

def say_hi():
    Label(root, bg="purple", fg="white", text="Hi Wen Qi!",
          font=("Biome", 50, "bold")).pack()


# changing the title of the window
root = Tk()
root.title("Buttons")
root.minsize(200, 100)

# Creating a button object
button1 = Button(root, text="Say hi!", command=say_hi)
button1.pack()

root.mainloop()
