from tkinter import *
root = Tk()
root.geometry("300x400")

def add ():
    todo = text.get() + "\n"
    lst.insert (END, todo)
    
btn = Button(text = "Just a button", command = add)
btn.pack()
text = Entry()
text.pack()
lst = Text()
lst.pack()



root.mainloop()
print(lst)
