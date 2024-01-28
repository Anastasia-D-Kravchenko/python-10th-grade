from tkinter import *
def getting(self):
    sel = int(self)
    global i1
    i1 = sel * 72
    var1.set(sel)
def getting1(self):
    sel = int(self)
    global i2
    i2 = sel * 12
    var2.set(sel)
def getting2(self):
    sel = int(self)
    global i3
    i3 = sel * 16
    var3.set(sel)
def getting3(self):
    sel = int(self)
    global i4
    i4 = sel * 8
    var4.set(sel)
def rozrax():
    var5.set(i1+i2+i3+i4)
i1 = 0
i2 = 0
i3 = 0
i4 = 0
tk = Tk()
tk.title("Піцерія")
tk.geometry('440x310')
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
tk.mainloop()