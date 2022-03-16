"""exercise using buttons and labels"""

from tkinter import *
root = Tk()

def print_num(num):
    label_text.set(num)


root.title("Lambda counting")
root.minsize(300, 50)

message1 = Label(root, text="3", font=("Biome", 30, "bold")).pack()

Button(root, text="1", command=lambda: print_num(1)).pack()
Button(root, text="2", command=lambda: print_num(2)).pack()
Button(root, text="3", command=lambda: print_num(3)).pack()
Button(root, text="4", command=lambda: print_num(4)).pack()
Button(root, text="5", command=lambda: print_num(5)).pack()
Button(root, text="6", command=lambda: print_num(6)).pack()

label_text = StringVar()
message2 = Label(root, textvariable=label_text, font=("Courier", 24, "bold"))
message2.pack()

root.mainloop()
