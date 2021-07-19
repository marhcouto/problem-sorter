from position import Position
from tkinter import CENTER, Button, Entry, Label, LabelFrame, Listbox, font, S, N, NE, NW, END, Message
import os_tinkering



class GUIMenu:
    def __init__(self, app):
        self.widgets = {}
        self.app = app
        self.makeMenu()

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

    def makeMenu():
        pass


class MainMenu(GUIMenu):

    def __init__(self, app):
        super().__init__(app)

    def makeMenu(self):

        self.addWidget("searchButton", Button(self.app.gui, text = "Search Problems", 
        command = lambda : self.app.changeMenu(SearchMenu(self.app), False)), 
        Position(0.5, 0.9, Position.MODE_RELATIVE, CENTER))
        self.addWidget("insertButton", Button(self.app.gui, text = "Insert Problems", 
        command = lambda : self.app.changeMenu(InsertMenu(self.app), False)),
        Position(0.1, 0.9, Position.MODE_RELATIVE, CENTER))
        self.addWidget("deleteButton", Button(self.app.gui, text = "Instructions", 
        command = lambda : self.app.changeMenu(InfoMenu(self.app), False)),
        Position(0.9, 0.9, Position.MODE_RELATIVE, CENTER))
        self.addWidget("menuLabel", Label(self.app.gui, text = "Welcome to Problem Sorter", font = font.Font(size = 30)),
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))


class SearchMenu(GUIMenu):

    def __init__(self, app):
        super().__init__(app)

    def makeMenu(self):
        
        # TITLE
        self.addWidget("menuLabel", Label(self.app.gui, text = "Search or Delete", font = font.Font(size = 20)),
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))
        
        # FRAMES
        self.addWidget("searchFrame", LabelFrame(self.app.gui, text = "Search Options", height = 400, width = 400, relief = "sunken", labelanchor = N, font = font.Font(size = 16)), 
        Position(0.05, 0.15, Position.MODE_RELATIVE, NW))
        self.addWidget("resultsFrame", LabelFrame(self.app.gui, text = "Results", height = 400, width = 400, relief = "sunken", labelanchor = N, font = font.Font(size = 16)), 
        Position(0.95, 0.15, Position.MODE_RELATIVE, NE))

        # LEFTSIDE
        self.addWidget("entry", Entry(self.widgets["searchFrame"][0]), 
        Position(0.5, 0.15, Position.MODE_RELATIVE, CENTER))

        self.addWidget("entryLabel", Label(self.widgets["searchFrame"][0], text = "Insert theme", font = font.Font(size = 12)), 
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))

        self.addWidget("themeListLabel", Label(self.widgets["searchFrame"][0], text = "Selected themes", font = font.Font(size = 12)), 
        Position(0.5, 0.29, Position.MODE_RELATIVE, CENTER))

        self.addWidget("themeList", Listbox(self.widgets["searchFrame"][0], height = 16, width = 50), 
        Position(0.5, 0.85, Position.MODE_RELATIVE, S))

        # RIGHTSIDE
        self.addWidget("resultList", Listbox(self.widgets["resultsFrame"][0], height = 25, width = 50), 
        Position(0.5, 0.85, Position.MODE_RELATIVE, S))

        # TODO
        self.widgets["resultList"][0].insert(0,"/home/marhcouto/Documents/BDProblemas/README.md")

        # BUTTONS
        self.addWidget("lookupButton", Button(self.widgets["resultsFrame"][0], text = "Look up",
        command =  self.lookupCommand),
        Position(0.3, 0.925, Position.MODE_RELATIVE, CENTER))

        self.addWidget("deleteButton", Button(self.widgets["resultsFrame"][0], text = "Delete"),
        Position(0.7, 0.925, Position.MODE_RELATIVE, CENTER))

        self.addWidget("removeButton", Button(self.widgets["searchFrame"][0], text = "Remove", 
        command = lambda : self.widgets["themeList"][0].delete(self.widgets["themeList"][0].curselection()[0]) if 0 < len(self.widgets["themeList"][0].curselection()) else "banana"),
        Position(0.7, 0.925, Position.MODE_RELATIVE, CENTER))

        self.addWidget("addButton", Button(self.widgets["searchFrame"][0], text = "Add", 
        command = lambda : self.widgets["themeList"][0].insert(0, self.widgets["entry"][0].get())),
        Position(0.3, 0.925, Position.MODE_RELATIVE, CENTER))
            
        self.addWidget("goBack", Button(self.app.gui, text = "Go Back", 
        command = lambda : self.app.changeMenu(MainMenu(self.app), False)), 
        Position(0.5, 0.9, Position.MODE_RELATIVE, CENTER))

    def lookupCommand(self):
        fileName = self.widgets["resultList"][0].get(0, END)[self.widgets["resultList"][0].curselection()[0]]
        if len(self.widgets["resultList"][0].curselection()) > 0:
            os_tinkering.getFile(fileName)


class InfoMenu(GUIMenu):

    def __init__(self, app):
        super().__init__(app)

    def makeMenu(self):
        self.addWidget("menuLabel", Label(self.app.gui, text = "Instructions", font = font.Font(size = 20)),
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))
        self.addWidget("message", Message(self.app.gui, text = " - In the search menu, you can search for exercises/exams containing exercises that associate with the themes you chose,\n" +
                                                                    "followed by lookup of the file or elimination of its registry.\n\n"+
                                                                    " - In the insertion menu, you can insert new entries in the database, filling in the fields with the corresponding info.", 
                                                                    font = font.Font(family = "Arial", size = 14)),
        Position(0.1, 0.2, Position.MODE_RELATIVE, NW))
        self.addWidget("goBack", Button(self.app.gui, text = "Go Back", 
        command = lambda : self.app.changeMenu(MainMenu(self.app), False)), 
        Position(0.5, 0.9, Position.MODE_RELATIVE, CENTER))


class InsertMenu(GUIMenu):

    def __init__(self, app):
        super().__init__(app)

    def makeMenu(self):

        # TITLE
        self.addWidget("menuLabel", Label(self.app.gui, text = "Inserting Menu", font = font.Font(family = 'Helvetica', size = 20)),
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))

        # LABELS
        self.addWidget("themeLabel", Label(self.app.gui, text = "Theme", font = font.Font(size = 12)),
        Position(0.3, 0.25, Position.MODE_RELATIVE, CENTER))
        self.addWidget("pathLabel", Label(self.app.gui, text = "Document's path", font = font.Font(size = 12)),
        Position(0.7, 0.25, Position.MODE_RELATIVE, CENTER))

        # ENTRIES
        self.addWidget("themeEntry", Entry(self.app.gui),
        Position(0.3, 0.3, Position.MODE_RELATIVE, CENTER))
        self.addWidget("pathEntry", Entry(self.app.gui),
        Position(0.7, 0.3, Position.MODE_RELATIVE, CENTER))

        # BUTTONS
        self.addWidget("goBack", Button(self.app.gui, text = "Go Back",
        command = lambda : self.app.changeMenu(MainMenu(self.app), False)), 
        Position(0.5, 0.9, Position.MODE_RELATIVE, CENTER))

        self.addWidget("submit", Button(self.app.gui, text = "Submit",
        command = self.submitionCommand),
        Position(0.5, 0.5, Position.MODE_RELATIVE, CENTER))
    
    def submitionCommand(self):
        "does bananas"
        # TODO


