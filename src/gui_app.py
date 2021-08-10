from tkinter import Tk

from os_tinkering import getOs

class Application:

    def __init__(self, db, icon):
        self.gui = Tk()
        if getOs() == "Windows" or getOs() == "Darwin":
            self.gui.iconbitmap(icon)
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



