from tkinter import *

root = Tk()
root.geometry('500x300')
root.resizable(False, False)

radiovar = BooleanVar()
radio1 = Radiobutton(text = 'Radiobutton1', variable = radiovar, value = 1, indicatoron = 0)
radio2 = Radiobutton(text = 'Radiobutton2', variable = radiovar, value = 0, indicatoron = 0)
radiovar2 = IntVar()

lbl1 = Label(width = '30', height = '10', bg = 'white')
lbl2 = Label(text = '')
sumlbl = 0

def rgbfunc():
    if (radiovar2.get() == 0):
        lbl1.config(bg = 'red')
    elif (radiovar2.get() == 1):
        lbl1.config(bg = 'green')
    else:
        lbl1.config(bg = 'blue')

cradio1 = Radiobutton(text = 'Red', variable = radiovar2, value = 0, command = rgbfunc)
cradio2 = Radiobutton(text = 'Green', variable = radiovar2, value = 1, command = rgbfunc)
cradio3 = Radiobutton(text = 'Blue', variable = radiovar2, value = 2, command = rgbfunc)

checkvar1 = DoubleVar()
checkvar2 = DoubleVar()
checkvar3 = DoubleVar()
checkvar4 = DoubleVar()

def points():
    global sumlbl
    if (checkvar1.get() == 2.5):
        sumlbl += 2.5
        lbl2.config(text = sumlbl)
    elif (checkvar2.get() == 5):
        sumlbl += 5
        lbl2.config(text = sumlbl)
    elif (checkvar3.get() == 7.5):
        sumlbl += 7.5
        lbl2.config(text = sumlbl)
    else:
        sumlbl += 10
        lbl2.config(text = sumlbl)

check1 = Checkbutton(text = '1 task', variable = checkvar1, onvalue = 2.5, command = points)
check2 = Checkbutton(text = '2 task', variable = checkvar2, onvalue = 5, command = points)
check3 = Checkbutton(text = '3 task', variable = checkvar3, onvalue = 7.5, command = points)
check4 = Checkbutton(text = '4 task', variable = checkvar4, onvalue = 10, command = points)

radio1.place(x=20, y=20)
radio2.place(x=130, y=20)

cradio1.place(x=90, y=60)
cradio2.place(x=90, y=80)
cradio3.place(x=90, y=100)

lbl1.place(x=17, y=140)
lbl2.place(x=300, y=150)

check1.place(x=300, y=25)
check2.place(x=300, y=50)
check3.place(x=300, y=75)
check4.place(x=300, y=100)

root.mainloop()
