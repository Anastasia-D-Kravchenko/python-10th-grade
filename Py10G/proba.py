from tkinter import *
def clik_me_hi():
    onCl = box.curselection()
    print(f'{en.get()} {box.get(onCl)}!')
    lb1 = Label(text=f'{en.get()} з днем народженням!вмвмодвиимядіиоиядмомияіф', fg='#FFFFFF',bg='#FFFFFF')
    lb1.place(x=135, y=140)
    lb1 = Label(text=f'{en.get()} {box.get(onCl)}!', fg='#A85135',bg='#FFFFFF')
    lb1.place(x=135, y=140)
    con.place(x=0, y=170)
tk = Tk()
tk.title("Привітання")
tk.geometry('500x500')
tk["bg"] = "#FFFFFF"
lb = Label(text='Введіть ім\'я:', fg='#A85135',bg='#FFFFFF')
en = Entry(fg="#A85135", bg="#C8E47A", width=18)
boxOn = Label(text='Вітання', fg='#A85135',bg='#FFFFFF')
box = Listbox(height=4)
box.insert(END,"з днем народженям")
box.insert(END,"з 8 березная")
box.insert(END,"з Новим роком")
onCl = box.curselection()
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
box.place(x=350, y=70)
but.place(x=80, y=80)
butt.place(x=200, y=80)
con = Canvas(tk,width=500,height=350)
con["bg"] = "#FFFFFF"
fl_img = PhotoImage(file='flowers.png')
con.create_image(200,175,image=fl_img)
tk.mainloop()