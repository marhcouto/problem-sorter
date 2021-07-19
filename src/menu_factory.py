from tkinter.constants import ANCHOR, N, S
from gui_menu import Menu
from position import Position
from gui_window import Window
import os

from tkinter import Button, Label, Entry, LabelFrame, CENTER, Message, NE, NW, Widget, font, Listbox, END



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
        menu.addWidget("deleteButton", Button(self.window.gui, text = "Instructions", command = lambda : self.window.changeMenu(InfoMenuFactory(self.window).makeMenu(), False)),
        Position(0.9, 0.95, Position.MODE_RELATIVE, CENTER))
        menu.addWidget("menuLabel", Label(self.window.gui, text = "Welcome to Problem Sorter", font = font.Font(size = 20)),
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
        
        menu.addWidget("menuLabel", Label(self.window.gui, text = "Search or Delete", font = font.Font(size = 20)),
        Position(0.5, 0.05, Position.MODE_RELATIVE, CENTER))
        
        # FRAMES
        menu.addWidget("searchFrame", LabelFrame(self.window.gui, text = "Search Options", height = 400, width = 400, relief = "sunken", labelanchor = N, font = font.Font(size = 16)), 
        Position(0.05, 0.12, Position.MODE_RELATIVE, NW))
        menu.addWidget("resultsFrame", LabelFrame(self.window.gui, text = "Results", height = 400, width = 400, relief = "sunken", labelanchor = N, font = font.Font(size = 16)), 
        Position(0.95, 0.12, Position.MODE_RELATIVE, NE))

        menu.addWidget("resultList", Listbox(menu.widgets["resultsFrame"][0], height = 25, width = 50), 
        Position(0.5, 0.85, Position.MODE_RELATIVE, S))

        menu.addWidget("entry", Entry(menu.widgets["searchFrame"][0]), 
        Position(0.5, 0.15, Position.MODE_RELATIVE, CENTER))

        menu.addWidget("entryLabel", Label(menu.widgets["searchFrame"][0], text = "Insert theme", font = font.Font(size = 12)), 
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))

        menu.addWidget("themeListLabel", Label(menu.widgets["searchFrame"][0], text = "Selected themes", font = font.Font(size = 12)), 
        Position(0.5, 0.29, Position.MODE_RELATIVE, CENTER))

        menu.addWidget("themeList", Listbox(menu.widgets["searchFrame"][0], height = 16, width = 50), 
        Position(0.5, 0.85, Position.MODE_RELATIVE, S))

        for i in range (100):
            menu.widgets["resultList"][0].insert(i,"Hello")

        menu.widgets["resultList"][0].insert(i,"/home/marhcouto/Documents/BDProblemas/README.md")

        #menu.addWidget("lookupButton", Button(menu.widgets["resultsFrame"][0], text = "Look up",
        #command = lambda : os.system(menu.widgets["resultList"][0].get(0, END)[menu.widgets["resultList"][0].curselection()[0]]) if 0 < len(menu.widgets["resultList"][0].curselection()) else print("banana")),
        #Position(0.3, 0.925, Position.MODE_RELATIVE, CENTER))

        menu.addWidget("deleteButton", Button(menu.widgets["resultsFrame"][0], text = "Delete"),
        Position(0.7, 0.925, Position.MODE_RELATIVE, CENTER))

        menu.addWidget("removeButton", Button(menu.widgets["searchFrame"][0], text = "Remove", 
        command = lambda : menu.widgets["themeList"][0].delete(menu.widgets["themeList"][0].curselection()[0]) if 0 < len(menu.widgets["themeList"][0].curselection()) else "banana"),
        Position(0.7, 0.925, Position.MODE_RELATIVE, CENTER))

        menu.addWidget("addButton", Button(menu.widgets["searchFrame"][0], text = "Add", 
        command = lambda : menu.widgets["themeList"][0].insert(0, menu.widgets["entry"][0].get())),
        Position(0.3, 0.925, Position.MODE_RELATIVE, CENTER))
            
        menu.addWidget("goBack", Button(self.window.gui, text = "Go Back", command = lambda : self.window.changeMenu(MainMenuFactory(self.window).makeMenu(), False)), 
        Position(0.5, 0.9, Position.MODE_RELATIVE, CENTER))
        
        return menu


class InfoMenuFactory(MenuFactory):

    def __init__(self, window):
        super().__init__(window)


    def makeMenu(self):
        menu = Menu()
        menu.addWidget("menuLabel", Label(self.window.gui, text = "Instructions", font = font.Font(size = 20)),
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))
        menu.addWidget("message", Message(self.window.gui, text = " - In the search menu, you can search for exercises/exams containing exercises that associate with the themes you chose,\n" +
                                                                    "followed by lookup of the file or elimination of its registry.\n\n"+
                                                                    " - In the insertion menu, you can insert new entries in the database, filling in the fields with the corresponding info.", 
                                                                    font = font.Font(family = "Arial", size = 14)),
        Position(0.1, 0.2, Position.MODE_RELATIVE, NW))
        menu.addWidget("goBack", Button(self.window.gui, text = "Go Back", command = lambda : self.window.changeMenu(MainMenuFactory(self.window).makeMenu(), False)), 
        Position(0.5, 0.9, Position.MODE_RELATIVE, CENTER))
        return menu
