from tkinter import *

window = Tk()
window.title("Python GUI")
window.config(background="#333")

def click():
    print("You clicked the button!")
    window = Tk()
    window.title("Different window")
    window.config(background="#000")
    window.mainloop()

button = Button(window,
                text="click",
                command=click,
                )

button.pack()
window.mainloop()