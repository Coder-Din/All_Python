from tkinter import *
from tkinter import filedialog

window = Tk()
window.title('Text Editer')

def Loadfile():
    filename = filedialog.Open(window, filetypes = [('*.txt files', '.txt')]).show()
    if filename == '':
        return
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', open(filename, 'rt').read())

def Savefile():
    filename = filedialog.SaveAs(window, filetypes = [('*.txt files', '.txt')]).show()
    if filename == '':
        return
    if not filename.endswith(".txt"):
        filename += ".txt"
    open(filename, 'wt').write(textbox.get('1.0', 'end'))

def Quit():
    global window
    window.destroy()

panel = Frame(window, height = 60, bg = 'gray')
textframe = Frame(window, height = 340, width = 600)
textbox = Text(textframe, font = 'Arial, 24', wrap = 'word')
scroll = Scrollbar(textframe)
load = Button(panel, text = 'load', width = 30, command = Loadfile)
save = Button(panel, text = 'save', width = 30, command = Savefile)
quit = Button(panel, text = 'quit', width = 30, command = Quit)

scroll['command'] = textbox.yview
textbox['yscrollcommand'] = scroll.set

panel.pack(side = 'top', fill = 'x')
textframe.pack(side = 'bottom', fill = 'x')
textbox.pack(side = 'left', fill = 'both')
scroll.pack(side = 'right', fill = 'y')
load.place(x = 10, y = 18)
save.place(x = 570, y = 18)
quit.place(x = 1130, y = 18)

window.mainloop()