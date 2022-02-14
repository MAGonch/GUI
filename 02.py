from tkinter import* #подключаем библиотеку tkinter
win = Tk()                     # создаем окно
win.geometry('600x600+400+200') #размеры окна
win.title("Test Colours")   #заголовок окна
color1 = Button(win, text = "red", height = 3, width = 5)
color1.grid(row=5, column=0)
color2 = Button(win, text = "blue", height = 3, width = 5)
color2.grid(row=5, column=1)
color3 = Button(win, text = "green", height = 3, width = 5)
color3.grid(row=5, column=2)
color3 = Button(win, text = "yellow", height = 3, width = 5)
color3.grid(row=5, column=3)
get_color = Button(win, text = "Получить цвет", height = 30, width = 20)
get_color.grid(row=0, column=3)
pole_color = Label(win, bg = "grey", height = 30, width = 50)
pole_color.grid(row=0, column=1)
pole_viv = Label(win, text = '', height = 5, width = 50)
pole_viv.grid(row=6, column=1)

win.mainloop()
