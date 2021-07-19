from position import Position
import tkinter as tk

class Menu:
    def __init__(self):
        self.widgets = {}

    def addWidget(self, name, widget, position):
        self.widgets[name] = (widget, position);

    def removeWidget(self, name):
        self.widgets.pop(name)

    def place(self):
        for widget,pos in self.widgets.values():
            if pos.mode == Position.MODE_RELATIVE:
                widget.place(relx = pos.x, rely = pos.y, anchor = pos.anchor)
            elif pos.mode == Position.MODE_ABSOLUTE:
                widget.place(x = pos.x, y = pos.y, anchor = pos.anchor)

    def unplace(self):
        for widget, position in self.widgets.values():
            widget.place_forget()