from tkinter import *

food = ["Pita", "Rollo", "Bułka"]

window = Tk()
window.title('Wybierz kebsa')
window.config(background='purple')

x = IntVar()

for i in range(len(food)):
    radioButton = Radiobutton(window,
                              text=food[i],
                              variable=x,
                              value=i,
                              bg= 'purple')
    radioButton.pack()

window.mainloop()