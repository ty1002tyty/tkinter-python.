
import  tkinter
window= tkinter.Tk()
window.title('라디오버튼')
window.geometry('300x200+100+100')

def func():
    print(rv1.get())


rv1 = tkinter.IntVar()

radio1 = tkinter.Radiobutton(window,text='1번',variable=rv1,value=1,command=func)
radio2 = tkinter.Radiobutton(window,text='2번',variable=rv1,value=2,command=func)
radio3 = tkinter.Radiobutton(window,text='3번',variable=rv1,value=3,command=func)
radio1.pack()
radio2.pack()
radio3.pack()

window.mainloop()