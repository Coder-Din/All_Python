from tkinter import *

window = Tk()
lbl1 = Label(text = "Введите математическое выражение из чисел и знаков +, -, *, /, //, %, **")
lbl1.pack()
entry1 = Entry(width=50, bg="white", justify=CENTER)
entry1.focus()
entry1.pack()
lbl2 = Label()
lbl2.pack()

def solver(event):
    global entry1, lbl2
    lbl2["text"] = eval(entry1.get())

entry1.bind('<Return>', solver)
window.mainloop()
