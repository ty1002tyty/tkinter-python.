

def func():
    print('버튼을 클릭했습니다.')

import tkinter
window = tkinter.Tk()
window.title('Tkinter 버튼')
window.geometry('300x200+100+100')


btn = tkinter.Button(window,text='버튼클릭',command=func)
btn.pack()
window.mainloop()