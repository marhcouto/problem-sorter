from tkinter import *

class Menu:
    def __init__(self, gui):
        self.gui = gui

    @property
    def gui(self):
        return self.__gui

    @gui.setter
    def gui(self, newGui):
        self.__gui = newGui

    def place(self):
        pass

    def unplace(self):
        pass

class InsertMenu(Menu):

    def __init__(self, gui):
        super().__init__(gui)
    
    def build():
        pass

class MainMenu(Menu):

    def __init__(self, gui):
        super().__init__(gui)
        self.insertButton = Button(self.gui, text = "Insert Problems")
        self.searchButton = Button(self.gui, text = "Search Problems")
        self.deleteButton = Button(self.gui, text = "Delete Problems")
        self.myLabel = Label(self.gui, text = "Welcome to Problem Sorter")
        
    
    def place(self):
        self.myLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        self.insertButton.place(relx = 0.2, rely = 0.9, anchor = CENTER)
        self.searchButton.place(relx = 0.5, rely = 0.9, anchor = CENTER)
        self.deleteButton.place(relx = 0.8, rely = 0.9, anchor = CENTER)

    def unplace(self):
        self.myLabel.place_forget()
        self.insertButton.place_forget()
        self.deleteButton.place_forget()
        self.searchButton.place_forget()


def main():
    gui = Tk()
    gui.geometry("500x200")
    mainMenu = MainMenu(gui)

    mainMenu.place()
    gui.mainloop()

if __name__ == "__main__":
    main()