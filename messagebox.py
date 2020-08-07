from tkinter import messagebox as mb
from tkinter import *
window = Tk()
window.geometry('400x350')
text = Text()

def answerfunc():
    answer = mb.askyesno(title = "Question", message = "Check the data ?")
    if answer:
        data = text.get('1.0', 'end')
        data = data[0:-1]
        if data.isdigit():
            mb.showinfo(message = 'This is a number!')
        else:
            mb.showerror(message = 'This is not a number')

button = Button(text = 'Copy', command = answerfunc)
text.place(x = 125, y = 10,height = 20, width = 150)
button.place(x = 180, y = 40)
window.mainloop()