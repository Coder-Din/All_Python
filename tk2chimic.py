from tkinter import *
root = Tk()
root.geometry('180x540')
root.title('Chimic')

elements=['O', 'H', 'C', 'S', 'Cl', 'Na']
sub1=['OH', 'OC', 'OHS', 'HCl', 'ClNa', 'OHNa', 'HS', 'OS', 'OSNa', 'HC', 'CNa', 'OCl']
sub2=['H2O', 'C02', 'H2S04', 'HCl', 'NaCl', 'NaOH', 'H2S', 'SO2', 'Na2SO4', 'CH4', 'Na3C', 'Cl2O7']
sub3=['вода', 'углекислый газ', 'серная кислота', 'соляная кислота', 'поваренная соль', 'едкий натр', 'сероводород', 'оксид серы', 'сульфат натрия', 'метан', 'карбид натрия', 'оксид хлора']

im = PhotoImage(file='flask11.gif')
lbl1 = Label(text='Chemical Elements', width=25)
lbl2 = Label(text='', width=220, height=220, image=im, compound=CENTER)
lbl3 = Label(text='', width=25)

elem1 = IntVar()
elem1.set(0)
elem2 = IntVar()
elem2.set(0)
elem3 = IntVar()
elem3.set(0)
elem4 = IntVar()
elem4.set(0)
elem5 = IntVar()
elem5.set(0)
elem6 = IntVar()
elem6.set(0)

radio1 = Checkbutton(text = 'O', onvalue=1, offvalue=0, indicatoron = 0, variable=elem1, width=7, height=3)
radio2 = Checkbutton(text = 'H', onvalue=1, offvalue=0, indicatoron = 0, variable=elem2, width=7, height=3)
radio3 = Checkbutton(text = 'C', onvalue=1, offvalue=0, indicatoron = 0, variable=elem3, width=7, height=3)
radio4 = Checkbutton(text = 'S', onvalue=1, offvalue=0, indicatoron = 0, variable=elem4, width=7, height=3)
radio5 = Checkbutton(text = 'Cl', onvalue=1, offvalue=0, indicatoron = 0, variable=elem5, width=7, height=3)
radio6 = Checkbutton(text = 'Na', onvalue=1, offvalue=0, indicatoron = 0, variable=elem6, width=7, height=3)

def substance():
    subst = ''
    elemcheck = [elem1.get(), elem2.get(), elem3.get(), elem4.get(), elem5.get(), elem6.get()]
    for i in range(len(elemcheck)):
        if elemcheck[i] == 1:
            subst = subst + elements[i]
    if sub1.count(subst) != 0:
        a = sub1.index(subst)
        lbl2.config(text = sub2[a])
        lbl3.config(text = sub3[a])
    else:
        lbl2.config(text = '')
        lbl3.config(text = 'No connection found')

btn=Button(text="Соединить элементы", bg='#87CEEB', width=25, height=2, command=substance)
btn.place(x=0, y=150)

lbl1.place(x=0, y=10)
lbl2.place(x=0, y=150, width=180)
lbl3.place(x=0, y=350)

radio1.place(x=0, y=40)
radio2.place(x=60, y=40)
radio3.place(x=120, y=40)
radio4.place(x=0, y=95)
radio5.place(x=60, y=95)
radio6.place(x=120, y=95)

root.mainloop()