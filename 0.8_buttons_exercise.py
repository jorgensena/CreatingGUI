"""exercise using buttons and labels"""

from tkinter import *
root = Tk()

def change_num(num):
    if num == 7:
        current.set(current.get()*7)
    elif num == 3:
        current.set(current.get()+3)
    elif num == 2:
        current.set(current.get()-2)
    elif num == 0:
        current.set(current.get()*0)


root.title("Puzzle number buttons")
root.minsize(300, 50)

current = IntVar()
goal = IntVar()

current.set(0)
goal.set(71)

Label(root, textvariable=current, fg="white", bg="#49c2f2",
      font=("Courier", 30, "bold")).pack(side=LEFT)

Button(root, text="x7", font=("Arial", 24),
       command=lambda: change_num(7)).pack(side=LEFT)
Button(root, text="+3", font=("Arial", 24),
       command=lambda: change_num(3)).pack(side=LEFT)
Button(root, text="-2", font=("Arial", 24),
       command=lambda: change_num(2)).pack(side=LEFT)
Button(root, text="0", font=("Arial", 24),
       command=lambda: change_num(0)).pack(side=LEFT)

Label(root, textvariable=goal, fg="white", bg="#49c2f2",
      font=("Biome", 30, "bold")).pack(side=LEFT)

root.mainloop()
