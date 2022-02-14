from tkinter import*


def plus():
    a = text1.get()
    b = text2.get()
    c = int(a) + int(b)
    metka.config(text=str(c))
    


    
win = Tk()
win.geometry('600x500+400+200')
win.title("Мини-калькулятор")
text1 = Entry(win,bd = 4, font=("Arial",30,"bold"))
text2 = Entry(win,bd = 4, font=("Arial",30,"bold"))
btn1 = Button(win,relief=RIDGE,bd=7, bg='white',font=("Arial",10,"bold"),height = 2, width=3,text="+",command=plus)
#btn1.grid(row=0, column=0, sticky="nsew")
btn2 = Button(win,relief=RIDGE,bd=7, bg='white',font=("Arial",10,"bold"), height = 2, width=3, text="-")
btn3 = Button(win,relief=RIDGE,bd=7, bg='white',font=("Arial",10,"bold"), height = 2, width=3, text="*")
btn4 = Button(win,relief=RIDGE,bd=7, bg='white',font=("Arial",10,"bold"), height = 2, width=3, text="/")
metka = Label(win,bd = 4, bg="white",font=("Arial",30,"bold"), height = 1, width=18)


#gkjklfjgklfljglkl
#kg;lfkg;ldfk




text1.pack(pady=20)
text2.pack(pady=5)
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
metka.pack(pady=20)
win.mainloop()




