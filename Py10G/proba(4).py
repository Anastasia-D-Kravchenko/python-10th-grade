from tkinter import *
def clik_me_hi():
    print(f'Привіт, {en.get()}!')
    lb2 = Label(text=f'Допобачення, {en.get()}!', fg='#F0F0F0')
    lb1 = Label(text=f'Привіт, {en.get()}!', fg='#EC9704')
    lb1.place(x=100, y=140)
    lb2.place(x=80, y=140)
def clik_me_bay():
    print(f'Допобачення, {en.get()}!')
    lb2 = Label(text=f'Допобачення, {en.get()}!', fg='#EC9704')
    lb2.place(x=80, y=140)
tk = Tk()
tk.title("Не перше")
tk.geometry('300x200')
lb = Label(text='Введіть ім\'я:', fg='#EC9704')
en = Entry(fg="#F7C815", bg="#9C4A1A", width=18)
but = Button(text='Привіт? Чи ні?',
    command=clik_me_hi,
    width=15,
    height=2,
    bg="#9C4A1A",
    fg="#EC9704")
butt = Button(text='Привіт? Точно?',
    command=clik_me_bay,
    width=15,
    height=2,
    bg="#9C4A1A",
    fg="#EC9704")
# but.pack()
lb.place(x=20, y=50)
en.place(x=140, y=50)
but.place(x=20, y=80)
butt.place(x=140, y=80)
tk.mainloop()