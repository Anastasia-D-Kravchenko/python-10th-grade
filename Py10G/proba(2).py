from tkinter import *
def clik_me():
    print(en.get())
tk = Tk()
tk.title("Не перше")
tk.geometry('300x200')
en = Entry(fg="blue", bg="yellow", width=25)
but = Button(text='Чого не тишнешь?',
    command=clik_me,
    width=21,
    height=3,
    bg="blue",
    fg="yellow")
# but.pack()
en.place(x=80, y=50)
but.place(x=80, y=80)
tk.mainloop()