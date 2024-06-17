import  tkinter
window= tkinter.Tk()
window.title('이미지')
window.geometry('400x300+100+100')

image=tkinter.PhotoImage(file="./gui/짜장면.png")

label=tkinter.Label(window,image=image)
label.pack()


window.mainloop()