

def func():
    price=0
    if cv1.get()==1:
        price+=5000
    if cv2.get()==1:
        price+=6000
    if cv3.get()==1:
        price+=12000
    label1.config(text='가격:'+str(price)+'원')
    

    





import  tkinter
window= tkinter.Tk()
window.title('체크버튼')
window.geometry('300x200+100+100')

cv1 = tkinter.IntVar()
check1 = tkinter.Checkbutton(window, text='짜장면',variable=cv1,command=func)
check1.pack()


cv2 = tkinter.IntVar()
check2 = tkinter.Checkbutton(window, text='짬뽕',variable=cv2,command=func)
check2.pack()


cv3 = tkinter.IntVar()
check3 = tkinter.Checkbutton(window, text='탕수육',variable=cv3,command=func)
check3.pack()

label1 = tkinter.Label(window, text='가격 :0원')
label1.pack()










window.mainloop()