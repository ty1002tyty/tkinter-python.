import  tkinter
window= tkinter.Tk()
window.title('라디오버튼')
window.geometry('400x300+100+100')

b1=tkinter.Button(window,text='50,50')
b2=tkinter.Button(window,text='100,200')
b3=tkinter.Button(window,text='300,200')

b1.place(x=50,y=50)
b2.place(x=100,y=200)
b3.place(x=300,y=200)

window.mainloop()