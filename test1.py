from tkinter import *

def submit():
    password = entry.get()
    print("Twoje hasło to: " + password)

def delete():
    entry.delete(0, END)
    print('Password has ben deleted')

def backspace():
    entry.delete((len(entry.get())-1), END)

window = Tk()

window.title('Enter password')

entry = Entry(window,
              font=('arial',
                    30),
              show='*',
              fg='#00FF00',
              bg='black')
entry.pack(side=LEFT)

submit_button = Button(window, text='submit', command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text='delete', command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text='backspace', command=backspace)
backspace_button.pack(side=RIGHT)



window.mainloop()