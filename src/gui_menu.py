from position import Position
from tkinter import CENTER, Button, Entry, Label, LabelFrame, Listbox, font, S, N, NE, NW, END, Message, Canvas
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

        # self.addWidget("canvas", Canvas())


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
        self.addWidget("resultList", Listbox(self.widgets["resultsFrame"][0], height = 16, width = 50), 
        Position(0.5, 0.85, Position.MODE_RELATIVE, S))

        self.addWidget("resultListLabel", Label(self.widgets["resultsFrame"][0], text = "Files", font = font.Font(size = 12)),
        Position(0.5, 0.29, Position.MODE_RELATIVE, CENTER))

        self.addWidget("messageLabel", Label(self.widgets["resultsFrame"][0], text = "Messages", font = font.Font(size = 12)), 
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))

        self.addWidget("message", Message(self.widgets["resultsFrame"][0], text = "Awaiting actions", width = 200),
        Position(0.1, 0.15, Position.MODE_RELATIVE, NW))

        # BUTTONS
        self.addWidget("lookupButton", Button(self.widgets["resultsFrame"][0], text = "Look up", 
        command =  self.lookupCommand),
        Position(0.3, 0.925, Position.MODE_RELATIVE, CENTER))

        self.addWidget("deleteButton", Button(self.widgets["resultsFrame"][0], text = "Delete",
        command = self.deleteCommand),
        Position(0.7, 0.925, Position.MODE_RELATIVE, CENTER))

        self.addWidget("removeButton", Button(self.widgets["searchFrame"][0], text = "Remove theme", 
        command = lambda : self.widgets["themeList"][0].delete(self.widgets["themeList"][0].curselection()[0]) if 0 < len(self.widgets["themeList"][0].curselection()) else "banana"),
        Position(0.7, 0.925, Position.MODE_RELATIVE, CENTER))

        self.addWidget("addButton", Button(self.widgets["searchFrame"][0], text = "Add theme", 
        command = lambda : self.widgets["themeList"][0].insert(0, self.widgets["entry"][0].get() if len(self.widgets["entry"][0].get()) > 0 else "bananas")),
        Position(0.3, 0.925, Position.MODE_RELATIVE, CENTER))
            
        self.addWidget("goBack", Button(self.app.gui, text = "Go Back", 
        command = lambda : self.app.changeMenu(MainMenu(self.app), False)), 
        Position(0.2, 0.9, Position.MODE_RELATIVE, CENTER))

        self.addWidget("search", Button(self.app.gui, text = "Search Files",
        command = self.searchCommand),
        Position(0.5, 0.9, Position.MODE_RELATIVE, CENTER))

    def lookupCommand(self):
        
        if len(self.widgets["resultList"][0].curselection()) <= 0:
            self.widgets["message"].configure(text = "No files selected. Please select a file")
            return

        fileName = self.widgets["resultList"][0].get(0, END)[self.widgets["resultList"][0].curselection()[0]]
        print(fileName)
        os_tinkering.getFile(fileName)

    def searchCommand(self):

        themeList = self.widgets["themeList"][0]
        resultList = self.widgets["resultList"][0]

        if len(themeList.get(0, END)) <= 0:
            self.widgets["message"].configure(text = "No themes selected. Please, add a theme to the theme list")
            return

        list1 = []
        query = "SELECT Problem.location FROM Problem JOIN ProblemTheme JOIN Theme ON Theme.id = ProblemTheme.themeID AND Problem.id = ProblemTheme.problemId AND Theme.name = '{theme}'"
        
        for theme in themeList.get(0, END):
            for path in self.app.db.execute(query.format(theme = theme)):
                list1.append(path)

        resultList.delete(0, END)

        for path in list1:
            resultList.insert(0, path[0])

    def deleteCommand(self):

        if len(self.widgets["resultList"][0].curselection()) <= 0:
            self.widgets["message"].configure(text = "No files selected. Please select a file")
            return

        fileName = self.widgets["resultList"][0].get(0, END)[self.widgets["resultList"][0].curselection()[0]]
        query = "DELETE FROM ProblemTheme WHERE ProblemTheme.problemId = (SELECT id FROM Problem WHERE location = '{filename}');"

        result = self.app.db.execute(query.format(filename = fileName))
        self.widgets["message"].configure(text = "{file} was successfully removed from the database".format(file = fileName))

        self.searchCommand()
        


class InfoMenu(GUIMenu):

    def __init__(self, app):
        super().__init__(app)

    def makeMenu(self):
        self.addWidget("menuLabel", Label(self.app.gui, text = "Instructions", font = font.Font(size = 20)),
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))
        self.addWidget("message", Message(self.app.gui, width = 800, text = " - In the search menu, you can search for exercises/exams containing exercises that associate with the themes you chose," +
                                                                    "followed by lookup of the file or elimination of its registry.\n\n"+
                                                                    " - In the insertion menu, you can insert new entries in the database, filling in the fields with the corresponding info." + 
                                                                    "For one file, multiple themes can be inserted.\n\n" + 
                                                                    " - For searches, the themes selected affect the search as a reunion of results.\n\n" +
                                                                    " - For insertions, if new files are selected, they will be inserted; if the chosen file already exists, its themes will be updated," + 
                                                                    " same goes for themes.", 
                                                                    font = font.Font(family = "Arial", size = 14)),
        Position(0.1, 0.2, Position.MODE_RELATIVE, NW))
        self.addWidget("goBack", Button(self.app.gui, text = "Go Back", 
        command = lambda : self.app.changeMenu(MainMenu(self.app), False)), 
        Position(0.2, 0.9, Position.MODE_RELATIVE, CENTER))


class InsertMenu(GUIMenu):

    def __init__(self, app):
        super().__init__(app)

    def makeMenu(self):

        # TITLE
        self.addWidget("menuLabel", Label(self.app.gui, text = "Inserting Menu", font = font.Font(family = 'Helvetica', size = 20)),
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))

        # LABELS
        self.addWidget("themeLabel", Label(self.app.gui, text = "Theme", font = font.Font(size = 12)),
        Position(0.3, 0.2, Position.MODE_RELATIVE, CENTER))
        self.addWidget("pathLabel", Label(self.app.gui, text = "Document's path", font = font.Font(size = 12)),
        Position(0.7, 0.2, Position.MODE_RELATIVE, CENTER))
        self.addWidget("listLabel", Label(self.app.gui, text = "Themes selected", font = font.Font(size = 12)),
        Position(0.5, 0.35, Position.MODE_RELATIVE, CENTER))
        self.addWidget("messageLabel", Label(self.app.gui, text = "Messages", font = font.Font(size = 12)),
        Position(0.75, 0.35, Position.MODE_RELATIVE, CENTER))

        # LIST
        self.addWidget("themeList", Listbox(self.app.gui, height = 16, width = 50), 
        Position(0.5, 0.7, Position.MODE_RELATIVE, S))

        # ENTRIES
        self.addWidget("themeEntry", Entry(self.app.gui),
        Position(0.3, 0.25, Position.MODE_RELATIVE, CENTER))
        self.addWidget("pathEntry", Entry(self.app.gui),
        Position(0.7, 0.25, Position.MODE_RELATIVE, CENTER))

        # MESSAGE
        self.addWidget("message", Message(self.app.gui, text = "Awaiting actions", width = 150),
        Position(0.7, 0.4, Position.MODE_RELATIVE, NW))

        # BUTTONS
        self.addWidget("goBack", Button(self.app.gui, text = "Go Back",
        command = lambda : self.app.changeMenu(MainMenu(self.app), False)), 
        Position(0.2, 0.9, Position.MODE_RELATIVE, CENTER))

        self.addWidget("submit", Button(self.app.gui, text = "Submit",
        command = self.submitionCommand),
        Position(0.8, 0.9, Position.MODE_RELATIVE, CENTER))

        self.addWidget("addButton", Button(self.app.gui, text = "Add theme",
        command = lambda : self.widgets["themeList"][0].insert(0, self.widgets["themeEntry"][0].get())),
        Position(0.4, 0.75, Position.MODE_RELATIVE, CENTER))

        self.addWidget("removeButton", Button(self.app.gui, text = "Remove theme", 
        command = lambda : self.widgets["themeList"][0].delete(self.widgets["themeList"][0].curselection()[0]) if 0 < len(self.widgets["themeList"][0].curselection()) else "banana"),
        Position(0.6, 0.75, Position.MODE_RELATIVE, CENTER))
    
    def submitionCommand(self):
        
        themeList = self.widgets["themeList"][0]

        if len(themeList.get(0, END)) <= 0:
            self.widgets["message"].configure(text = "No themes selected. Please, add a theme to the theme list")
            return

        print("BEFORE:\n", self.app.db.execute("SELECT * FROM ProblemTheme;"))
        print("BEFORE:\n", self.app.db.execute("SELECT * FROM Problem;"))
        print("BEFORE:\n", self.app.db.execute("SELECT * FROM Theme;"))

        path = self.widgets["pathEntry"][0].get()
        insertProblem = "INSERT INTO Problem (location) VALUES('{path}');".format(path = path)
        insertThemes = "INSERT INTO Theme (name) VALUES('{theme}');"
        insertPT = "INSERT INTO ProblemTheme (themeId, problemId) VALUES({idT}, {idP});"
        getThemeIds = "SELECT id FROM Theme WHERE name = '{theme}';"
        getProblemId = "SELECT id FROM Problem WHERE location = '{path}';".format(path = path)

        for theme in themeList.get(0, END):
            self.app.db.execute(insertThemes.format(theme = theme))
        self.app.db.execute(insertProblem)
        
        themeIds = set()

        for theme in themeList.get(0, END):
            themeIds.add(self.app.db.execute(getThemeIds.format(theme = theme))[0][0])

        problemId = self.app.db.execute(getProblemId)[0][0]

        for i in themeIds:
            self.app.db.execute(insertPT.format(idT = i, idP = problemId))

        print("AFTER:\n", self.app.db.execute("SELECT * FROM ProblemTheme;"))
        print("AFTER:\n", self.app.db.execute("SELECT * FROM Problem;"))
        print("AFTER:\n", self.app.db.execute("SELECT * FROM Theme;"))










