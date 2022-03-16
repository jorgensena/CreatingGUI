"""intro to using buttons and labels"""

from tkinter import *
root = Tk()

def press_button():
    text = entry_text.get()
    label_text.set(text)


num = 0
root.title("Changing label text")
root.minsize(300, 50)

entry_text = StringVar()
enter_smth = Entry(textvariable=entry_text, font=("Arial", 15)).pack()

button = Button(root, text="Press to show message", command=press_button)
button.pack()

label_text = StringVar()
message = Label(root, textvariable=label_text, font=("Courier", 24, "bold"))
message.pack()

root.mainloop()
