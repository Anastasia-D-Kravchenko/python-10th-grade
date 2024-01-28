from tkinter import *
def getting(self):
    sel = int(self)
    global i1, a1
    i1 = sel * 72
    a1 = sel
    var1.set(sel)
def getting1(self):
    sel = int(self)
    global i2, a2, a1, i1
    i2 = sel * 12
    a2 = sel
    a1 += sel
    var2.set(sel)
def getting2(self):
    sel = int(self)
    global i3, a3
    i3 = sel * 16
    a3 = sel
    var3.set(sel)
def getting3(self):
    sel = int(self)
    global i4, a4
    i4 = sel * 8
    a4 += 1
    var4.set(sel)
def rozrax():
    if var.get()==1:
        global i4, i1, a2, a3
        if a1 != 0 and a2 != 0 and a4 != 0 and a1%2 == 0:
            i4 = i4 * 0.5
            var5.set(i1+i2+i3+i4)
            i4 = i4/0.5
        else:
            var5.set(i1+i2+i3+i4)
    else:
        if var.get()==2:
            b = i1 - i1 * 0.1
            if a2 != 0 or a3 != 0:
                var5.set(b+i2+i3+i4)
            else:
                var5.set(i1+i2+i3+i4)
        else:
            var5.set(i1+i2+i3+i4)
i1,i2,i3,i4,a1,a2,a3,a4 = 0,0,0,0,0,0,0,0
tk = Tk()
tk.title("Піцерія")
tk.geometry('560x310')
tk["bg"] = "#FFFFFF"
lb1 = Label(text='Найменування', fg='#F0865E',bg='#FFFFFF')
lb2 = Label(text='Ціна, грн.', fg='#F0865E',bg='#FFFFFF')
lb3 = Label(text='Кількість', fg='#F0865E',bg='#FFFFFF')
lb4 = Label(text='Вартість, грн.', fg='#F0865E',bg='#FFFFFF')
P1 = Label(text='Піца', fg='#F0865E',bg='#FFFFFF')
P2 = Label(text='Морозиво', fg='#F0865E',bg='#FFFFFF')
P3 = Label(text='Тістечко', fg='#F0865E',bg='#FFFFFF')
P4 = Label(text='Сік', fg='#F0865E',bg='#FFFFFF')
C1 = Label(text='72', fg='#FFFFFF',bg='#F0865E',width=5)
C2 = Label(text='12', fg='#FFFFFF',bg='#F0865E',width=5)
C3 = Label(text='16', fg='#FFFFFF',bg='#F0865E',width=5)
C4 = Label(text='8', fg='#FFFFFF',bg='#F0865E',width=5)
sc1 = Scale(orient=HORIZONTAL,length=80,from_=0,to=40,bg='#FFFFFF',bd=0, highlightthickness=0,command=getting)
sc2 = Scale(orient=HORIZONTAL,length=80,from_=0,to=40,bg='#FFFFFF',bd=0, highlightthickness=0,command=getting1)
sc3 = Scale(orient=HORIZONTAL,length=80,from_=0,to=40,bg='#FFFFFF',bd=0, highlightthickness=0,command=getting2)
sc4 = Scale(orient=HORIZONTAL,length=80,from_=0,to=40,bg='#FFFFFF',bd=0, highlightthickness=0,command=getting3)
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
B1 = Label(text=0, fg='#FFFFFF',bg='#F0865E',width=5,textvariable=var1)
B2 = Label(text=0, fg='#FFFFFF',bg='#F0865E',width=5,textvariable=var2)
B3 = Label(text=0, fg='#FFFFFF',bg='#F0865E',width=5,textvariable=var3)
B4 = Label(text=0, fg='#FFFFFF',bg='#F0865E',width=5,textvariable=var4)
L1 = Label(text='Вартість замовлення:', fg='#F0865E',bg='#FFFFFF')
L2 = Label(text='0', fg='#FFFFFF',bg='#F0865E',width=5,textvariable=var5)
L3 = Label(text='грн.', fg='#F0865E',bg='#FFFFFF')
var = IntVar()
boxOn2 = Label(text='Зображення на листі',bg='#FFFFFF', fg='#F0865E')
rbut1 = Radiobutton(text='Соковита насолода',variable=var,value=1,bg='#FFFFFF', fg='#F0865E')
rbut2 = Radiobutton(text='Ситий день',variable=var,value=2,bg='#FFFFFF', fg='#F0865E')
L4 = Button(text='Розрахувати',
    command=rozrax,
    width=15,
    height=2,
    bg="#9C4949",
    fg="#F0865E")
lb1.place(x=20, y=10)
lb2.place(x=130, y=10)
lb3.place(x=230, y=10)
lb4.place(x=330, y=10)
P1.place(x=20, y=60)
P2.place(x=20, y=110)
P3.place(x=20, y=160)
P4.place(x=20, y=210)
C1.place(x=140, y=60)
C2.place(x=140, y=110)
C3.place(x=140, y=160)
C4.place(x=140, y=210)
B1.place(x=350, y=60)
B2.place(x=350, y=110)
B3.place(x=350, y=160)
B4.place(x=350, y=210)
sc1.place(x=215, y=45)
sc2.place(x=215, y=95)
sc3.place(x=215, y=145)
sc4.place(x=215, y=195)
L1.place(x=20, y=265)
L2.place(x=160, y=265)
L3.place(x=215, y=265)
L4.place(x=280, y=255)
boxOn2.place(x=420, y=10)
rbut1.place(x=420, y=35)
rbut2.place(x=420, y=55)
tk.mainloop()