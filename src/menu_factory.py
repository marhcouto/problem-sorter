from tkinter.constants import N
from gui_menu import Menu
from position import Position
from gui_window import Window

from tkinter import Button, Canvas, Label, Entry, LabelFrame, CENTER, NE, NW, Widget, font, Listbox



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

        
        menu.addWidget("menuLabel", Label(self.window.gui, text = "WELCOME", font = font.Font(size = 20)),
        Position(0.5, 0.05, Position.MODE_RELATIVE, CENTER))
        
        # FRAMES
        menu.addWidget("searchFrame", LabelFrame(self.window.gui, text = "Search Options", height = 400, width = 400, relief = "sunken", labelanchor = N, font = font.Font(size = 16)), 
        Position(0.05, 0.12, Position.MODE_RELATIVE, NW))
        menu.addWidget("resultsFrame", LabelFrame(self.window.gui, text = "Results", height = 400, width = 400, relief = "sunken", labelanchor = N, font = font.Font(size = 16)), 
        Position(0.95, 0.12, Position.MODE_RELATIVE, NE))

        menu.addWidget("resultList", Listbox(menu.widgets["resultsFrame"][0], height = 25, width = 50), 
        Position(0.5, 0.45, Position.MODE_RELATIVE, CENTER))

        menu.addWidget("entry", Entry(menu.widgets["searchFrame"][0]), 
        Position(0.5, 0.15, Position.MODE_RELATIVE, CENTER))

        menu.addWidget("entryLabel", Label(menu.widgets["searchFrame"][0], text = "Insert theme", font = font.Font(size = 12)), 
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))

        menu.addWidget("themeListLabel", Label(menu.widgets["searchFrame"][0], text = "Selected themes", font = font.Font(size = 12)), 
        Position(0.5, 0.3, Position.MODE_RELATIVE, CENTER))

        menu.addWidget("canvas", Canvas(menu.widgets["searchFrame"][0], height = 10, width = 10, bg = "grey"),
        Position(0.5, 0.5, Position.MODE_RELATIVE, N))

        for i in range (100):
            menu.widgets["resultList"][0].insert(i,"Hello")

        menu.addWidget("lookupButton", Button(menu.widgets["resultsFrame"][0], text = "Look up"),
        Position(0.3, 0.925, Position.MODE_RELATIVE, CENTER))

        menu.addWidget("deleteButton", Button(menu.widgets["resultsFrame"][0], text = "Delete"),
        Position(0.7, 0.925, Position.MODE_RELATIVE, CENTER))
            
        
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
