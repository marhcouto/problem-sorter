from gui_menu import Menu
from position import Position
from gui_window import Window

from tkinter import Button, Label



class MenuFactory():

    def __init__(self, window):
        self.__window = window

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, newWindow):
        self.__window = newWindow

    def makeMenu(self):
        pass


class MainMenuFactory(MenuFactory):

    def __init__(self, window):
        super().__init__(window)

    def makeMenu(self):
        menu = Menu()
        menu.addWidget(Button(self.window.gui, text = "Search Problems", command = lambda : self.window.changeMenu(SearchMenuFactory(self.window).makeMenu(), False)), 
        Position(0.5, 0.9, Position.MODE_RELATIVE))
        menu.addWidget(Button(self.window.gui, text = "Insert Problems", command = lambda : self.window.changeMenu(InsertMenuFactory(self.window).makeMenu(), False)),
        Position(0.2, 0.9, Position.MODE_RELATIVE))
        menu.addWidget(Button(self.window.gui, text = "Delete Problems", command = lambda : self.window.changeMenu(DeleteMenuFactory(self.window).makeMenu(), False)),
        Position(0.8, 0.9, Position.MODE_RELATIVE))
        menu.addWidget(Label(self.window.gui, text = "Welcome to Problem Sorter"),
        Position(0.5, 0.1, Position.MODE_RELATIVE))
        return menu

class InsertMenuFactory(MenuFactory):

    def __init__(self, window):
        super().__init__(window)


    def makeMenu(self):
        menu = Menu()
        menu.addWidget(Label(self.window.gui, text = "Inserting Menu"),
        Position(0.5, 0.1, Position.MODE_RELATIVE))
        menu.addWidget(Button(self.window.gui, text = "Go Back", command = lambda : self.window.changeMenu(MainMenuFactory(self.window).makeMenu(), False)), 
        Position(0.5, 0.9, Position.MODE_RELATIVE))
        return menu

class InsertMenuFactory(MenuFactory):

    def __init__(self, window):
        super().__init__(window)


    def makeMenu(self):
        menu = Menu()
        menu.addWidget(Label(self.window.gui, text = "Inserting Menu"),
        Position(0.5, 0.1, Position.MODE_RELATIVE))
        menu.addWidget(Button(self.window.gui, text = "Go Back", command = lambda : self.window.changeMenu(MainMenuFactory(self.window).makeMenu(), False)), 
        Position(0.5, 0.9, Position.MODE_RELATIVE))
        return menu

class SearchMenuFactory(MenuFactory):

    def __init__(self, window):
        super().__init__(window)


    def makeMenu(self):
        menu = Menu()
        menu.addWidget(Label(self.window.gui, text = "Searching Menu"),
        Position(0.5, 0.1, Position.MODE_RELATIVE))
        menu.addWidget(Button(self.window.gui, text = "Go Back", command = lambda : self.window.changeMenu(MainMenuFactory(self.window).makeMenu(), False)), 
        Position(0.5, 0.9, Position.MODE_RELATIVE))
        return menu

class DeleteMenuFactory(MenuFactory):

    def __init__(self, window):
        super().__init__(window)


    def makeMenu(self):
        menu = Menu()
        menu.addWidget(Label(self.window.gui, text = "Deleting Menu"),
        Position(0.5, 0.1, Position.MODE_RELATIVE))
        menu.addWidget(Button(self.window.gui, text = "Go Back", command = lambda : self.window.changeMenu(MainMenuFactory(self.window).makeMenu(), False)), 
        Position(0.5, 0.9, Position.MODE_RELATIVE))
        return menu
