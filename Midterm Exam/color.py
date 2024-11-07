from tkinter import *
class MyWindow:
    def __init__(self,win):
        self.btn5 = Button(win, text="Click to change color", width=20, height=1, command=self.color)
        self.btn5.place(x=150, y=150)

    def color(self):
        self.btn5 = Button(text="Click to change color", width=20, height=1, command=self.color2, bg='#FFFF00')
        self.btn5.place(x=150, y=150)
    def color2(self):
        self.btn5 = Button(text="Click to change color", width=20, height=1, command=self.color)
        self.btn5.place(x=150, y=150)

window = Tk()
mywin = MyWindow(window)
window.geometry("450x350+500+10")
window.title("Simple Calculator")
window.mainloop()