from tkinter import *

root = Tk()
root.title('Rainbow')
root.geometry('205x380')
root.resizable(False, False)

code = ['#FF0000', '#FFA500', '#FFFF00', '#008000', '#0000FF', '#000080', '#4B0082']
colors = ['red', 'orange', 'yellow', 'green', 'light blue', 'blue', 'purple']

lb_color = Label(text = '', font = 'Arial, 14', bg = '#ffffff', width = 20, height = 2)
lb_code = Label(text = '', font = 'Arial, 14', bg = '#ffffff', width = 20, height = 2)
lb_color.pack()
lb_code.pack()

def change_label(index):
    lb_color.config(text = colors[index])
    lb_code.config(text = code[index])

for index in range(len(code)):
    btn = Button(bg = code[index], width = 25, height = 2, command = lambda index1 = index: change_label(index1))
    btn.pack()

root.mainloop()
