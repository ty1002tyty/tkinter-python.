import  tkinter
window= tkinter.Tk()
window.title('라디오버튼')
window.geometry('300x200+100+100')




b1=tkinter.Button(window,text='0,0')
b2=tkinter.Button(window,text='0,1')
b3=tkinter.Button(window,text='0,2')
b4=tkinter.Button(window,text='1,0')
b5=tkinter.Button(window,text='1,1')
b6=tkinter.Button(window,text='1,2')
b7=tkinter.Button(window,text='2,0')
b8=tkinter.Button(window,text='2,1')
b9=tkinter.Button(window,text='2,2')

b1.grid(row=0,column=0,columnspan=2)
b3.grid(row=0,column=2)
b4.grid(row=1,column=0,rowspan=2)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b8.grid(row=2,column=1)
b9.grid(row=2,column=2)




window.mainloop()