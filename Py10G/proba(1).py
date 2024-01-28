from tkinter import *
def clik_me_hi():
    onCl = box.curselection()
    print(f'{en.get()} {box.get(onCl)}!')
    lb1 = Label(text=f'{en.get()} з днем народженням!вмвмодвиимядіиоиядмомияіф', fg='#FFFFFF',bg='#FFFFFF')
    lb1.place(x=135, y=140)
    lb1 = Label(text=f'{en.get()} {box.get(onCl)}!', fg='#A85135',bg='#FFFFFF')
    lb1.place(x=135, y=140)
    global fl_img
    if var.get()==1:
        fl_img = PhotoImage(file='flowers.png')
        en["bg"] = "#F5D450"
        but["bg"] = "#F5D450"
        butt["bg"] = "#F5D450"
        en["fg"] = "#E37D90"
        but["fg"] = "#E37D90"
        butt["fg"] = "#E37D90"
        lb["fg"] = "#E37D90"
        lb1["fg"] = "#E37D90"
        boxOn["fg"] = "#E37D90"
        boxOn2["fg"] = "#E37D90"
    elif var.get()==2:
        fl_img = PhotoImage(file='free-sticker-cake-4359682.png')
        en["bg"] = "#F9DD96"
        but["bg"] = "#F9DD96"
        butt["bg"] = "#F9DD96"
        en["fg"] = "#E2394B"
        but["fg"] = "#E2394B"
        butt["fg"] = "#E2394B"
        lb["fg"] = "#E2394B"
        lb1["fg"] = "#E2394B"
        boxOn["fg"] = "#E2394B"
        boxOn2["fg"] = "#E2394B"
    elif var.get()==3:
        fl_img = PhotoImage(file='free-sticker-beach-8408730.png')
        en["bg"] = "#3F7993"
        but["bg"] = "#3F7993"
        butt["bg"] = "#3F7993"
        en["fg"] = "#FFCC6F"
        but["fg"] = "#FFCC6F"
        butt["fg"] = "#FFCC6F"
        lb["fg"] = "#FFCC6F"
        lb1["fg"] = "#FFCC6F"
        boxOn["fg"] = "#FFCC6F"
        boxOn2["fg"] = "#FFCC6F"
    con = Canvas(tk,width=350,height=350,bd=0, highlightthickness=0)
    con["bg"] = "#FFFFFF"
    con.create_image(200,175,image=fl_img)
    con.place(x=0, y=170)
tk = Tk()
tk.title("Привітання")
tk.geometry('500x500')
tk["bg"] = "#FFFFFF"
lb = Label(text='Введіть ім\'я:', fg='#A85135',bg='#FFFFFF')
en = Entry(fg="#A85135", bg="#C8E47A", width=18)
boxOn = Label(text='Вітання',fg='#A85135',bg='#FFFFFF')
box = Listbox(height=4)
box.insert(END,"з днем народженям")
box.insert(END,"з 8 березная")
box.insert(END,"з Новим роком")
onCl = box.curselection()
var = IntVar()
boxOn2 = Label(text='Зображення на листі', fg='#A85135',bg='#FFFFFF')
rbut1 = Radiobutton(text='Квіти',variable=var,value=1,bg='#FFFFFF')
rbut2 = Radiobutton(text='Торт',variable=var,value=2,bg='#FFFFFF')
rbut3 = Radiobutton(text='Пейзаж',variable=var,value=3,bg='#FFFFFF')
but = Button(text='Привітання',
    command=clik_me_hi,
    width=15,
    height=2,
    bg="#C8E47A",
    fg="#A85135")
butt = Button(text='Вихід',
    command=tk.destroy,
    width=15,
    height=2,
    bg="#C8E47A",
    fg="#A85135")
lb.place(x=80, y=50)
en.place(x=200, y=50)
boxOn.place(x=350, y=50)
boxOn2.place(x=350, y=160)
rbut1.place(x=350, y=180)
rbut2.place(x=350, y=200)
rbut3.place(x=350, y=220)
box.place(x=350, y=70)
but.place(x=80, y=80)
butt.place(x=200, y=80)
tk.mainloop()