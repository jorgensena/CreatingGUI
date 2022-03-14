"""using multiple buttons"""

from tkinter import *

def count_up():
    global num
    num += 1
    print(num)

def count_down():
    global num
    num -= 1
    print(num)


# changing the title of the window
root = Tk()
num = 0
root.title("Counting program")
root.minsize(300, 50)

# Creating a button object
button1 = Button(root, text="Count up", command=count_up)
button1.pack()

button2 = Button(root, text="Count down", command=count_down)
button2.pack()

root.mainloop()
