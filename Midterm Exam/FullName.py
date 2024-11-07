from tkinter import *
class MyWindow:
    def __init__(self,win):
        self.lbl1 = Label(win, fg="Red", font="Arial", text="Enter your fullname:")
        self.lbl1.place(x=80, y=130)
        self.t1 = Entry(win, bd =2,)
        self.t1.place(x=270, y=130)
        self.t2 = Entry(win, bd=2,)
        self.t2.place(x=270, y=160)
        self.btn1 = Button(win, text = "Click to display your full name" ,width=25, height=1, command = self.add,fg="Red")
        self.btn1.place(x=80, y=160)

    def add (self):
        name = str(self.t1.get())
        self.t2.insert(END, str(name))

window = Tk()
mywin = MyWindow(window)

window.geometry("600x300+500+10")
window.title("Midterm in OOP")
window.mainloop()

