from tkinter import *

def swap():
    root.update()
    x1 = label.winfo_x()
    x2 = label2.winfo_x()

    label.place_configure(x=x2)
    label2.place_configure(x=x1)
    
root = Tk()

label = Label(root, text='Hello')
label.place(x=100, y=100)

label2 = Label(root, text='Hello2')
label2.place(x=150, y=100)

btn = Button(root, text='Swap', command=swap)
btn.place(x=125, y=150)

root.mainloop()
