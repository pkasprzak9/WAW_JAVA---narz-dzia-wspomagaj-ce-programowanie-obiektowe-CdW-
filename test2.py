from tkinter import *

#   count = 0

def click():
#  global count
#  count+=1
    print('Stop it!')

window = Tk()

#window.geometry("500x500")
window.title("test2")
window.config(background="#9938C0")

# label = Label(window, text="Kłaniam się nisko",
#              background="#9938C0",
#              font=('Arial',30,'bold'),
#              fg='#F59B09',
#              relief=RAISED,
#              bd=5,)

button = Button(window,
                text="Don't click me!",
                font=('Comic Sands', 30),
                fg='#F59B09',
                highlightbackground='#9938C0',
                activeforeground='#F59B09',
                command=click)

button.pack()
# label.pack()
# label.place(x=200, y=200)

window.mainloop()
