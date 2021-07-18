from tkinter import *


gui = Tk()
gui.geometry("500x200")

myLabel = Label(gui, text = "Welcome to Problem Sorter")

insertButton = Button(gui, text = "Insert Problems")
searchButton = Button(gui, text = "Search Problems")
deleteButton = Button(gui, text = "Delete Problems")

myLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)
insertButton.place(relx = 0.2, rely = 0.9, anchor = CENTER)
searchButton.place(relx = 0.5, rely = 0.9, anchor = CENTER)
deleteButton.place(relx = 0.8, rely = 0.9, anchor = CENTER)

gui.mainloop()

