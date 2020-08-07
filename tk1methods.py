from tkinter import *
window = Tk()
window.geometry("500x500")
btn1 = Button(text="Button1", relief=RIDGE, bd=5, activebackground="blue",
              activeforeground="white", width=30)
lbl1 = Label(text="Very fat Borders are very bad for the aesthetics",
             relief=RIDGE, bd=20)
lbl2 = Label(text="But so are Super fat borders",
             relief=RIDGE, bd=50)
ety1 = Entry()
btn1.place(x=200, y=400)
lbl1.place(x=25, y=150)
ety1.place(x=150, y=50)
lbl2.place(x=150, y=200)

