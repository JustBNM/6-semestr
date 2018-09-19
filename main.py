from tkinter import *

WINDOW_GEOMETRY = "300x250"

#создаём окно
root = Tk()
root.title("Games")
root.geometry(WINDOW_GEOMETRY)

#кнопка приветствия
label1 = Label(text="Hello stranger", fg="#eee", bg="#333")
label1.pack()


text = "Select game"
label2 = Label(text=text, justify=LEFT)
label2.place(relx=.40, rely=.45)

#функции кнопок из других файлов
def click_button1():
    from second import Aerohockey
    Aerohockey.main()
def click_button_death():
    from second import died
    died.show()


#Зададим параметры кнопок
btn1 = Button(text="aerohockey", background="#555", foreground="#ccc",
             padx="10", pady="5", font="100", command=click_button1)

btn1.pack(side = LEFT)


btn2 = Button(text="smth else", background="#555", foreground="#ccc",
             padx="10", pady="5", font="100")
btn2.pack(side = RIGHT)


btn3 = Button(text="you died", background="#555", foreground="#ccc",
             padx="10", pady="5", font="100", command = click_button_death)
btn3.pack(side = BOTTOM)

#Запуск окна

root.mainloop()