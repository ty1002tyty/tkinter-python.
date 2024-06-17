import tkinter
window = tkinter.Tk()
window.title("프로그램이름")
window.geometry('300x200+100+100')



#라벨 생성
label = tkinter.Label(window,
                      text='라벨입니다',
                      width=10,
                      height=5,
                      fg='red',
                      relief='solid')
label.pack()

window.mainloop()