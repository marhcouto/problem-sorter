from tkinter import *

class Menu:
    def __init__(self, window):
        self.window = window

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, newWindow):
        self.__window = newWindow

    def place(self):
        pass

    def unplace(self):
        pass

class InsertMenu(Menu):

    def __init__(self, gui):
        super().__init__(gui)
        self.myLabel = Label(self.window.gui, text = "Inserting Menu")
        self.backButton = Button(self.window.gui, text = "Go Back", command = self.goBackCommand)

    def goBackCommand(self):
        self.window.changeMenu(MainMenu(self.window), False)

    def place(self):
        self.myLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        self.backButton.place(relx = 0.2, rely = 0.9, anchor = CENTER)

    def unplace(self):
        self.myLabel.place_forget()     



class SearchMenu(Menu):

    def __init__(self, gui):
        super().__init__(gui)
        self.myLabel = Label(self.window.gui, text = "Delete Menu")
        self.backButton = Button(self.window.gui, text = "Go Back", command = self.goBackCommand)

    def goBackCommand(self):
        self.window.changeMenu(MainMenu(self.window), False)

    def place(self):
        self.myLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)   
        self.backButton.place(relx = 0.2, rely = 0.9, anchor = CENTER)

    def unplace(self):
        self.myLabel.place_forget()     


class DeleteMenu(Menu):

    def __init__(self, gui):
        super().__init__(gui)
        self.myLabel = Label(self.window.gui, text = "Search Menu")
        self.backButton = Button(self.window.gui, text = "Go Back", command = self.goBackCommand)

    def goBackCommand(self):
        self.window.changeMenu(MainMenu(self.window), False)

    def place(self):
        self.myLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)   
        self.backButton.place(relx = 0.2, rely = 0.9, anchor = CENTER)

    def unplace(self):
        self.myLabel.place_forget()     
    
    

class MainMenu(Menu):

    def __init__(self, window):
        super().__init__(window)
        self.insertButton = Button(self.window.gui, text = "Insert Problems", command = self.insertCommand)
        self.searchButton = Button(self.window.gui, text = "Search Problems", command = self.searchCommand)
        self.deleteButton = Button(self.window.gui, text = "Delete Problems", command = self.deleteCommand)
        self.myLabel = Label(self.window.gui, text = "Welcome to Problem Sorter")

    def insertCommand(self):
        self.window.changeMenu(InsertMenu(self.window), False)

    def deleteCommand(self):
        self.window.changeMenu(DeleteMenu(self.window), False)

    def searchCommand(self):
        self.window.changeMenu(SearchMenu(self.window), False)

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


class Window:

    def __init__(self, gui):
        self.gui = gui

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
