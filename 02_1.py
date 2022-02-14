from tkinter import* #подключаем библиотеку tkinter


def clc_left(event):
    win.title('Левый клик')
    win.config(bg='green')


def move(event):
    #получаем координаты мыши
    x = event.x
    y = event.y
    s = f"Движение мышью {x}x{y}"
    win.title(s)




win = Tk()                     # создаем окно
win.geometry('600x600+400+200') #размеры окна
win.title("Обработка событий")   #заголовок окна




win.bind('<Button-1>', clc_left)
win.bind('<Motion>', move)

win.mainloop()   #главный обработчик 
