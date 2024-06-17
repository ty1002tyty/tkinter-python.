import tkinter
import tkinter.font

window=tkinter.Tk()
window.title('폰트')
window.geometry('300x200+100+100')

font = tkinter.font.Font(family='맑은 고딕',size=20)

label = tkinter.Label(window,text='구암고등학교',font=font)
label.pack()


window.mainloop()