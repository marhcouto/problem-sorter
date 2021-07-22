import tkinter as tk
import tkinter.font as font



window = tk.Tk()
window.geometry("100x100")

label = tk.Label(window, text = "hello")
label.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

window.mainloop()

