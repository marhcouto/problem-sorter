from position import Position
import tkinter as tk

class Menu:
    def __init__(self):
        self.widgets = {}

    def addWidget(self, widget, position):
        self.widgets[widget] = position;

    def removeWidget(self, widget):
        self.widgets.pop(widget)

    def place(self):
        for widget, pos in self.widgets.items():
            if pos.mode == Position.MODE_RELATIVE:
                widget.place(relx = pos.x, rely = pos.y, anchor = tk.CENTER)
            elif pos.mode == Position.MODE_ABSOLUTE:
                widget.place(x = pos.x, y = pos.y, anchor = tk.CENTER)

    def unplace(self):
        for widget in self.widgets.keys():
            widget.place_forget()