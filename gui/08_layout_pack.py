import  tkinter
window= tkinter.Tk()
window.title('라디오버튼')
window.geometry('300x200+100+100')

b1= tkinter.Button(window,text='top')
b2= tkinter.Button(window,text='left')
b3= tkinter.Button(window,text='right')
b4= tkinter.Button(window,text='bottom')
b5= tkinter.Button(window,text='center')

b6= tkinter.Button(window,text='center-2')
b7= tkinter.Button(window,text='top-2')

b1.pack(side='top',fill='x')
b2.pack(side='left',fill='y')
b3.pack(side='right')
b4.pack(side='bottom')
b5.pack()
b6.pack()
b7.pack()

window.mainloop()