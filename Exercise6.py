from tkinter import *
class MyWindow:
    def __init__(self,win):
        self.lbl1 = Label(win, fg = "#FFFDD0", font = ("Arial", 20, "bold"), text="Simple Calculator",bg='#36454F')
        self.lbl1.place(x=100,y=35)
        self.lbl2 = Label(win, fg="Red", font="Arial", text="First number:",bg='#36454F')
        self.lbl2.place(x=80, y=130)
        self.t2 = Entry(win, bd =2)
        self.t2.place(x=190, y=130)
        self.lbl3 = Label(win, fg="Red", font="Arial", text="Second number:",bg='#36454F')
        self.lbl3.place(x=60, y=160)
        self.t3 = Entry(win, bd=2)
        self.t3.place(x=190, y=160)
        self.lbl4 = Label(win, fg="Red", font="Arial", text="Answer:",bg='#36454F')
        self.lbl4.place(x=100, y=190)
        self.t4 = Entry(win, bd=2)
        self.t4.place(x=190, y=190)
        self.btn1 = Button(win, text = "Addition" ,width=10, height=1, command = self.add,bg='#FDC8B3')
        self.btn1.place(x=160, y=220)
        self.btn2 = Button(win, text="Subtract", width=10, height=1, command=self.sub,bg='#FDC8B3')
        self.btn2.place(x=250, y=220)
        self.btn3 = Button(win, text="Multiply", width=10, height=1, command=self.mul,bg='#FDC8B3')
        self.btn3.place(x=160, y=250)
        self.btn4 = Button(win, text="Divide", width=10, height=1, command=self.div,bg='#FDC8B3')
        self.btn4.place(x=250, y=250)
        self.btn5 = Button(win, text="Clear", width=10, height=1, command=self.clear,bg='#FDC8B3')
        self.btn5.place(x=70, y=235)


    def add (self):
        self.t4.delete(0, 'end')
        num1 = int(self.t2.get())
        num2 = int(self.t3.get())
        result = num1 + num2
        self.t4.insert(END, str(result))

    def sub (self):
        self.t4.delete(0, 'end')
        num1 = int(self.t2.get())
        num2 = int(self.t3.get())
        result = num1 - num2
        self.t4.insert(END, str(result))

    def mul (self):
        self.t4.delete(0, 'end')
        num1 = int(self.t2.get())
        num2 = int(self.t3.get())
        result = num1 * num2
        self.t4.insert(END, str(result))

    def div (self):
        self.t4.delete(0, 'end')
        num1 = int(self.t2.get())
        num2 = int(self.t3.get())
        result = num1 / num2
        self.t4.insert(END, str(result))

    def clear (self):
        self.t2.delete(0, 'end')
        self.t3.delete(0, 'end')
        self.t4.delete(0, 'end')



window = Tk()
mywin = MyWindow(window)
window.configure(bg='#36454F')
window.geometry("450x350+500+10")
window.title("Simple Calculator")
window.mainloop()