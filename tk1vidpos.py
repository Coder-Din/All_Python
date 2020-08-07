from tkinter import *
root = Tk()
root.title("This is my title")
root.geometry("300x250")
btn1 = Button(text="Click Me!!!")
btn2 = Button(text="Click Me!!!")
btn3 = Button(text="Click Me!!!")
btn4 = Button(text="Click Me!!!")
btn5 = Button(text="Click Me!!!")

btn6 = Button(text="Click Me!!!")


btn1.grid(row=0, column=0, padx=5, ipadx=5, pady=5, ipady=5) 
btn2.grid(row=0, column=1, padx=5, ipadx=5, pady=5, ipady=5)
btn3.grid(row=1, column=0, padx=5, ipadx=5, pady=5, ipady=5)
btn4.grid(row=1, column=1, padx=5, ipadx=5, pady=5, ipady=5)
btn5.grid(row=0, column=2, padx=5, ipadx=5, pady=5, ipady=30, rowspan=2)
btn6.grid(row=2, column=0, padx=5, ipadx=100, pady=5, ipady=5, columnspan=3)


root.mainloop()
