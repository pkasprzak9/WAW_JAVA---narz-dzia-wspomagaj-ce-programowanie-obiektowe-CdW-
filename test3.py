from tkinter import *

food = ["Pita", "Rollo", "Bułka"]

window = Tk()
window.title('Wybierz kebsa')

x = IntVar()

for i in range(len(food)):
    radioButton = Radiobutton(window,
                              text=food[i],
                              variable=x,
                              value=i)
    radioButton.pack()

window.mainloop()