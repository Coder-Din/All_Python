from tkinter import *
window = Tk()
window.title('My APP')
window.geometry('500x500')


label1 = Label(text='Hello World!')
label1.grid(column=0, row=0)

label2 = Label(text='Bye Bye World!')
label2.grid(column=2, row=0)


button1 = Button(text='CLICK ME!')
button1.grid(column=0, row=2)

button2 = Button(text='DO NOT CLICK ME!')
button2.grid(column=2, row=2)

entry1 = Entry(width=20)
entry1.grid(column=1, row=1)

text1 = Text(height=10, width=20)
text1.grid(column=1, row=2)



window.mainloop()
