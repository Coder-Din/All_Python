from tkinter import *
import random

root = Tk()
root.geometry('460x340')
root.title('N-я цифра числа')

numF = random.randint(1, 999) / 10
numF01 = numF
cNum = 0
lst1 = ['//10', '%10', '/10', '*10', '//1', '%1', '/1', '*1']
num = Label(root, text=str(numF), font='Verdana 48')
rc = random.choice(lst1)
lbl1 = Label(root, text=rc)
lbl2 = Label (root, text="Congratulations, you've done it right")
lst2 = []
lbllst = Label(root, text = str(lst2))
lbllst.grid (row = 6, column = 0, columnspan = 4)

def stepBack():
    lst2.pop()
    lbllst.config(text = str(lst2))
    print(lst2)

btn2 = Button (root, text = 'Step back', command = stepBack)
btn2.grid (row = 7, column = 0, columnspan = 4)

def intDivBy10():                  
    global numF
    todo = '//10'
    numF //= 10
    num.config(text=str(numF))
    lst2.append(str(numF))
    lbllst.config(text = str(lst2))
    lbllst.grid (row = 6, column = 0, columnspan = 4)
    
    if todo == rc:
        lbl2.grid(row=5, column=0, columnspan=4)
    

def modOper10():
    global numF
    todo = '%10'
    numF %= 10
    num.config(text=str(numF))
    lst2.append(str(numF))
    lbllst.config(text = str(lst2))
    lbllst.grid (row = 6, column = 0, columnspan = 4)

    if todo == rc:
        lbl2.grid(row=5, column=0, columnspan=4)

def divBy10():
    global numF
    todo = '/10'
    numF /= 10
    num.config(text=str(numF))
    lst2.append(str(numF))
    lbllst.config(text = str(lst2))
    lbllst.grid (row = 6, column = 0, columnspan = 4)

    if todo == rc:
        lbl2.grid(row=5, column=0, columnspan=4)

def mulBy10():
    global numF
    todo = '*10'
    numF *= 10
    num.config(text=str(numF))
    lst2.append(str(numF))
    lbllst.config(text = str(lst2))
    lbllst.grid (row = 6, column = 0, columnspan = 4)

    if todo == rc:
        lbl2.grid(row=5, column=0, columnspan=4)
    
def intDivBy1():
    global numF
    todo = '//1'
    numF //= 1
    num.config(text=str(numF))
    lst2.append(str(numF))
    lbllst.config(text = str(lst2))
    lbllst.grid (row = 6, column = 0, columnspan = 4)

    if todo == rc:
        lbl2.grid(row=5, column=0, columnspan=4)

def modOper1():
    global numF
    todo = '%1'
    numF %= 1
    num.config(text=str(numF))
    lst2.append(str(numF))
    lbllst.config(text = str(lst2))
    lbllst.grid (row = 6, column = 0, columnspan = 4)

    if todo == rc:
        lbl2.grid(row=5, column=0, columnspan=4)

def divBy1():
    global numF
    todo = '/1'
    numF /= 1
    num.config(text=str(numF))
    lst2.append(str(numF))
    lbllst.config(text = str(lst2))
    lbllst.grid (row = 6, column = 0, columnspan = 4)

    if todo == rc:
        lbl2.grid(row=5, column=0, columnspan=4)

def mulBy1():
    global numF
    todo = '*1'
    numF *= 1
    num.config(text=str(numF))
    lst2.append(str(numF))
    lbllst.config(text = str(lst2))
    lbllst.grid (row = 6, column = 0, columnspan = 4)

    if todo == rc:
        lbl2.grid(row=5, column=0, columnspan=4)

def cancelOper():
    global numF
    global numF01
    numF = numF01
    num.config(text=str(numF))
    lst2.append(numF)
    lbl2.config(text='')
    
btn10_1 = Button(root, text='// 10', width=7, font='Verdana 18', command=intDivBy10)
btn10_2 = Button(root, text='% 10', width=7, font='Verdana 18', command=modOper10)
btn10_3 = Button(root, text='/ 10', width=7, font='Verdana 18', command=divBy10)
btn10_4 = Button(root, text='* 10', width=7, font='Verdana 18', command=mulBy10)
btn1_1 = Button(root, text='// 1', width=7, font='Verdana 18', command=intDivBy1)
btn1_2 = Button(root, text='% 1 ', width=7, font='Verdana 18', command=modOper1)
btn1_3 = Button(root, text='/ 1 ', width=7, font='Verdana 18', command=divBy1)
btn1_4 = Button(root, text='* 1 ', width=7, font='Verdana 18', command=mulBy1)

btn_cancel = Button(root, text='Отмена', font='Verdana 18',
 command=cancelOper)

num.grid(row=0, column=0, columnspan=4)
lbl1.grid(row=4, column=0, columnspan=4)

btn10_1.grid(row=1, column=0)
btn10_2.grid(row=1, column=1)
btn10_3.grid(row=1, column=2)
btn10_4.grid(row=1, column=3)
btn1_1.grid(row=2, column=0)
btn1_2.grid(row=2, column=1)
btn1_3.grid(row=2, column=2)
btn1_4.grid(row=2, column=3)
btn_cancel.grid(row=3, column=1, columnspan=2)

root.mainloop()
