from gui_menu import Menu
from position import Position
from gui_window import Window

from tkinter import Button, Label, Entry, LabelFrame, CENTER, NE, NW



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
        menu.addWidget("searchButton", Button(self.window.gui, text = "Search Problems", command = lambda : self.window.changeMenu(SearchMenuFactory(self.window).makeMenu(), False)), 
        Position(0.5, 0.95, Position.MODE_RELATIVE, CENTER))
        menu.addWidget("insertButton", Button(self.window.gui, text = "Insert Problems", command = lambda : self.window.changeMenu(InsertMenuFactory(self.window).makeMenu(), False)),
        Position(0.1, 0.95, Position.MODE_RELATIVE, CENTER))
        menu.addWidget("deleteButton", Button(self.window.gui, text = "Delete Problems", command = lambda : self.window.changeMenu(DeleteMenuFactory(self.window).makeMenu(), False)),
        Position(0.9, 0.95, Position.MODE_RELATIVE, CENTER))
        menu.addWidget("menuLabel", Label(self.window.gui, text = "Welcome to Problem Sorter"),
        Position(0.5, 0.05, Position.MODE_RELATIVE, CENTER))
        return menu

class InsertMenuFactory(MenuFactory):

    def __init__(self, window):
        super().__init__(window)


    def makeMenu(self):
        menu = Menu()
        menu.addWidget("menuLabel", Label(self.window.gui, text = "Inserting Menu"),
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))
        menu.addWidget("goBack", Button(self.window.gui, text = "Go Back", command = lambda : self.window.changeMenu(MainMenuFactory(self.window).makeMenu(), False)), 
        Position(0.5, 0.9, Position.MODE_RELATIVE, CENTER))
        return menu

class SearchMenuFactory(MenuFactory):

    def __init__(self, window):
        super().__init__(window)


    def makeMenu(self):
        menu = Menu()

        menu.addWidget("menuLabel", Label(self.window.gui, text = "Searching Menu"),
        Position(0.5, 0.05, Position.MODE_RELATIVE, CENTER))

        menu.addWidget("searchFrame", LabelFrame(self.window.gui, text = "Search Options", height = 400, width = 300), 
        Position(0.05, 0.12, Position.MODE_RELATIVE, NW))

        menu.addWidget("goBack", Button(self.window.gui, text = "Go Back", command = lambda : self.window.changeMenu(MainMenuFactory(self.window).makeMenu(), False)), 
        Position(0.5, 0.9, Position.MODE_RELATIVE, CENTER))

        menu.addWidget("entry", Entry(menu.widgets["searchFrame"][0]), 
        Position(0.5, 0.15, Position.MODE_RELATIVE, CENTER))

        menu.addWidget("entryLabel", Label(menu.widgets["searchFrame"][0], text = "Insert theme"), 
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))

        menu.addWidget("resultsLabel", Label(self.window.gui, text = "Results"), 
        Position(0.75, 0.2, Position.MODE_RELATIVE, CENTER))
        return menu

class DeleteMenuFactory(MenuFactory):

    def __init__(self, window):
        super().__init__(window)


    def makeMenu(self):
        menu = Menu()
        menu.addWidget("menuLabel", Label(self.window.gui, text = "Deleting Menu"),
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))
        menu.addWidget("goBack", Button(self.window.gui, text = "Go Back", command = lambda : self.window.changeMenu(MainMenuFactory(self.window).makeMenu(), False)), 
        Position(0.5, 0.9, Position.MODE_RELATIVE, CENTER))
        return menu
