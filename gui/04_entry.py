
db_id='abc'
db_pw='1234'
def btn2_event():
    id=entry_id.get()
    pw=entry_pw.get()
    if db_id==id and db_pw==pw:
        print('로그인 성공')
    else:
        print('로그인 실패')


import tkinter
window = tkinter.Tk()
window.title('프로그램버튼')
window.geometry('300x200+100+100')

label_id = tkinter.Label(window,text='ID')
entry_id = tkinter.Entry(window)
label_id.pack()
entry_id.pack()

abel_pw = tkinter.Label(window,text='PW')
entry_pw = tkinter.Entry(window)
abel_pw.pack()
entry_pw.pack()

btn2 = tkinter.Button(window,text='로그인', command=btn2_event)
btn2.pack()

window.mainloop()