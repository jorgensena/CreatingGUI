""" buttons n labels n geometry """

from tkinter import *
root = Tk()

def show_adj(adj):
    adj_text.set(adj)

def show_noun(noun):
    noun_text.set(noun)


root.title("Button Geometry")
root.geometry("300x200")

noun_text = StringVar()
adj_text = StringVar()

adj_text = Label(root, textvariable=adj_text, font=("Biome", 20, "bold"))\
    .grid(row=0, column=0, columnspan=2)
noun_label = Label(root, textvariable=noun_text, font=("Biome", 20, "bold"))\
    .grid(row=0, column=1, columnspan=2)
Button(root, text="Happy", command=lambda: show_adj("Happy"))\
    .grid(row=1, column=0, sticky=E)
Button(root, text="Sad", command=lambda: show_adj("Sad"))\
    .grid(row=1, column=1)
Button(root, text="Creepy", command=lambda: show_adj("Creepy"))\
    .grid(row=1, column=2, sticky=W)
Button(root, text="Dog", command=lambda: show_noun("Dog"))\
    .grid(row=2, column=0, sticky=E)
Button(root, text="Clown", command=lambda: show_noun("Clown"))\
    .grid(row=2, column=1)
Button(root, text="Banana", command=lambda: show_noun("Banana"))\
    .grid(row=2, column=2, sticky=W)

root.mainloop()


