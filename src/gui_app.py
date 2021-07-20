import tkinter as tk


class Application:

    def __init__(self, db):
        self.gui = tk.Tk()
        self.gui.geometry("1000x600")
        self.gui.title("Problem Sorter")
        self.db = db

    @property
    def gui(self):
        return self.__gui

    @gui.setter
    def gui(self, newGui):
        self.__gui = newGui

    def changeMenu(self, newMenu, startBool):
        if not startBool:
            self.menu.unplace()
        self.menu = newMenu
        self.menu.place()

    def run(self):
        self.gui.mainloop()



