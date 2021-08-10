from tkinter import CENTER, Button, Entry, Label, LabelFrame, Listbox, font, S, N, NE, NW, END, Message, Tk, W, E
from PIL import Image, ImageTk

from position import Position
import os_tinkering



LIST_WIDTH = 50 if os_tinkering.getOs() != "Darwin" else 25


class GUIMenu:

    def __init__(self, app):
        self.widgets = {}
        self.app = app
        self.makeMenu()


    def addWidget(self, name, widget, position):
        self.widgets[name] = (widget, position)


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

        self.addWidget("searchButton", Button(self.app.gui, text = "Search/Delete Problems", 
        command = lambda : self.app.changeMenu(SearchMenu(self.app), False)), 
        Position(0.5, 0.9, Position.MODE_RELATIVE, CENTER))
        self.addWidget("insertButton", Button(self.app.gui, text = "Insert Problems", 
        command = lambda : self.app.changeMenu(InsertMenu(self.app), False)),
        Position(0.2, 0.9, Position.MODE_RELATIVE, CENTER))
        self.addWidget("deleteButton", Button(self.app.gui, text = "Instructions", 
        command = lambda : self.app.changeMenu(InfoMenu(self.app), False)),
        Position(0.8, 0.9, Position.MODE_RELATIVE, CENTER))
        self.addWidget("menuLabel", Label(self.app.gui, text = "Welcome to Problem Sorter", font = font.Font(size = 30)),
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))

        self.image = ImageTk.PhotoImage(Image.open(os_tinkering.DIR_NAME + "/../img/theme.png"))

        self.addWidget("imageLabel", Label(image = self.image),
        Position(0.5, 0.5, Position.MODE_RELATIVE, CENTER))

      

class SearchMenu(GUIMenu):

    def __init__(self, app):
        super().__init__(app)


    def makeMenu(self):
        
        # TITLE
        self.addWidget("menuLabel", Label(self.app.gui, text = "Search or Delete", font = font.Font(size = 26)),
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))
        
        # FRAMES
        self.addWidget("searchFrame", LabelFrame(self.app.gui, text = "Search Options", height = 300, width = 400, relief = "sunken", labelanchor = N, font = font.Font(size = 18)), 
        Position(0.05, 0.15, Position.MODE_RELATIVE, NW))
        self.addWidget("resultsFrame", LabelFrame(self.app.gui, text = "Results", height = 300, width = 400, relief = "sunken", labelanchor = N, font = font.Font(size = 18)), 
        Position(0.95, 0.15, Position.MODE_RELATIVE, NE))
        self.addWidget("messageFrame", LabelFrame(self.app.gui, text = "Messages", height = 100, width = 700, relief = "sunken", labelanchor = N, font = font.Font(size = 18)),
        Position(0.5, 0.68, Position.MODE_RELATIVE, N))

        # LEFTSIDE
        self.addWidget("themeListLabel", Label(self.widgets["searchFrame"][0], text = "Themes", font = font.Font(size = 14, underline = True)), 
        Position(0.08, 0.08, Position.MODE_RELATIVE, W))

        self.addWidget("themeList", Listbox(self.widgets["searchFrame"][0], height = 10, width = LIST_WIDTH, selectmode = "multiple"), 
        Position(0.5, 0.85, Position.MODE_RELATIVE, S))

        self.initializeThemeList()

        # RIGHTSIDE
        self.addWidget("resultList", Listbox(self.widgets["resultsFrame"][0], height = 10, width = LIST_WIDTH), 
        Position(0.5, 0.85, Position.MODE_RELATIVE, S))

        self.addWidget("resultListLabel", Label(self.widgets["resultsFrame"][0], text = "File paths", font = font.Font(size = 14, underline = True)),
        Position(0.08, 0.08, Position.MODE_RELATIVE, W))

        self.addWidget("message", Message(self.app.gui, text = "Awaiting actions", width = 600),
        Position(0.2, 0.73, Position.MODE_RELATIVE, NW))

        # BUTTONS
        self.addWidget("lookupButton", Button(self.widgets["resultsFrame"][0], text = "Look up", 
        command =  self.lookupCommand),
        Position(0.3, 0.925, Position.MODE_RELATIVE, CENTER))

        self.addWidget("deleteButton", Button(self.widgets["resultsFrame"][0], text = "Delete",
        command = self.deleteCommand),
        Position(0.7, 0.925, Position.MODE_RELATIVE, CENTER))
 
        self.addWidget("goBack", Button(self.app.gui, text = "Go Back", 
        command = lambda : self.app.changeMenu(MainMenu(self.app), False)), 
        Position(0.2, 0.9, Position.MODE_RELATIVE, CENTER))

        self.addWidget("search", Button(self.app.gui, text = "Search Files",
        command = self.searchCommand),
        Position(0.5, 0.9, Position.MODE_RELATIVE, CENTER))

        self.addWidget("reset", Button(self.app.gui, text = "Reset",
        command = self.resetCommand),
        Position(0.8, 0.9, Position.MODE_RELATIVE, CENTER))


    def resetCommand(self):

        resultList = self.widgets["resultList"][0]
        message = self.widgets["message"][0]
        message.configure(text = "Awaiting actions")
        resultList.delete(0, END)


    def initializeThemeList(self):

        getThemesQuery = "SELECT name FROM Theme;"
        themeList = self.widgets["themeList"][0]

        themeList.delete(0, END)

        for line in self.app.db.execute(getThemesQuery):
            themeList.insert(0, line[0])


    def lookupCommand(self):

        if len(self.widgets["resultList"][0].curselection()) <= 0:
            self.widgets["message"][0].configure(text = "No files selected. Please select a file")
            return


        fileName = self.widgets["resultList"][0].get(0, END)[self.widgets["resultList"][0].curselection()[0]]
        os_tinkering.getFile(fileName)
    

    def searchCommand(self):

        themeList = self.widgets["themeList"][0]
        resultList = self.widgets["resultList"][0]
        list1 = []

        if len(themeList.curselection()) <= 0:
            query = "SELECT location FROM Problem;"
            for path in self.app.db.execute(query):
                list1.append(path[0])
        else:
            query = "SELECT Problem.location FROM Problem JOIN ProblemTheme JOIN Theme ON Theme.id = ProblemTheme.themeID AND Problem.id = ProblemTheme.problemId AND Theme.name = '{theme}'"
            for i in themeList.curselection():
                theme = themeList.get(0, END)[i]
                for path in self.app.db.execute(query.format(theme = theme)):
                    list1.append(path[0])

        resultList.delete(0, END)

        for path in list1:
            resultList.insert(0, path)

        self.widgets["message"][0].configure(text = "Presenting search results")


    def deleteCommand(self):

        if len(self.widgets["resultList"][0].curselection()) <= 0:
            self.widgets["message"][0].configure(text = "No files selected. Please select a file")
            return

        fileName = self.widgets["resultList"][0].get(0, END)[self.widgets["resultList"][0].curselection()[0]]

        query1 = "DELETE FROM ProblemTheme WHERE ProblemTheme.problemId = (SELECT id FROM Problem WHERE location = '{filename}');"
        query2 = "DELETE FROM Problem WHERE location = '{filename}';"

        self.app.db.execute(query1.format(filename = fileName))
        self.app.db.execute(query2.format(filename = fileName))
        self.widgets["message"][0].configure(text = "File successfully removed from the database")

        self.searchCommand()

    


class InfoMenu(GUIMenu):

    def __init__(self, app):
        super().__init__(app)


    def makeMenu(self):
        self.addWidget("menuLabel", Label(self.app.gui, text = "Instructions", font = font.Font(size = 26)),
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))
        self.addWidget("message", Message(self.app.gui, width = 800, text = " - In the search menu, you can search for exercises/exams containing exercises that associate with the themes you chose," +
                                                                    " followed by lookup of the file or elimination of its registry.\n\n" +
                                                                    " - When multiple themes are selected, the files presented are the ones which associate with at least one of the themes.\n\n" + 
                                                                    " - In the insertion menu, you can insert new entries in the database, filling in the fields with the corresponding info." + 
                                                                    " For one file, multiple themes can be selected. Deletion and insertion of themes is also possible.\n\n" + 
                                                                    " - For insertions, if new files are selected, they will be inserted; if the chosen file already exists, its themes will be updated," + 
                                                                    " same goes for themes.\n\n" +
                                                                    " - Reset buttons serve to reset the current menu to its initial state, deleting the results of a search for example.", 
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
        self.addWidget("menuLabel", Label(self.app.gui, text = "Inserting Menu", font = font.Font(size = 26)),
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))

        # LABELS
        self.addWidget("themeLabel", Label(self.app.gui, text = "Add a Theme", font = font.Font(size = 12, weight = "bold")),
        Position(0.3, 0.2, Position.MODE_RELATIVE, CENTER))
        self.addWidget("pathLabel", Label(self.app.gui, text = "Document's path", font = font.Font(size = 12, weight = "bold")),
        Position(0.7, 0.2, Position.MODE_RELATIVE, CENTER))
        self.addWidget("listLabel", Label(self.app.gui, text = "Themes", font = font.Font(size = 12, weight = "bold")),
        Position(0.5, 0.35, Position.MODE_RELATIVE, CENTER))
        self.addWidget("messageLabel", Label(self.app.gui, text = "Messages", font = font.Font(size = 12, weight = "bold")),
        Position(0.75, 0.35, Position.MODE_RELATIVE, CENTER))

        # LIST
        self.addWidget("themeList", Listbox(self.app.gui, height = 14, width = LIST_WIDTH), 
        Position(0.5, 0.7, Position.MODE_RELATIVE, S))

        self.initializeThemeList()

        # ENTRIES
        self.addWidget("themeEntry", Entry(self.app.gui, relief = "sunken"),
        Position(0.3, 0.25, Position.MODE_RELATIVE, CENTER))
        self.addWidget("pathEntry", Entry(self.app.gui, relief = "sunken"),
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
        Position(0.5, 0.9, Position.MODE_RELATIVE, CENTER))

        self.addWidget("reset", Button(self.app.gui, text = "Reset",
        command = self.resetCommand), 
        Position(0.8, 0.9, Position.MODE_RELATIVE, CENTER))

        self.addWidget("addButton", Button(self.app.gui, text = "Add theme",
        command = self.addThemeCommand),
        Position(0.4, 0.75, Position.MODE_RELATIVE, CENTER))

        self.addWidget("removeButton", Button(self.app.gui, text = "Remove theme", 
        command = self.removeThemeCommand),
        Position(0.6, 0.75, Position.MODE_RELATIVE, CENTER))

    
    def initializeThemeList(self):

        getThemesQuery = "SELECT name FROM Theme;"
        themeList = self.widgets["themeList"][0]

        themeList.delete(0, END)

        for line in self.app.db.execute(getThemesQuery):
            themeList.insert(0, line[0])


    def removeThemeCommand(self):

        themeList = self.widgets["themeList"][0]
        removeTheme = "DELETE FROM Theme WHERE name = '{theme}';"
        removeTheme2 = "DELETE FROM ProblemTheme WHERE EXISTS (SELECT * FROM Theme WHERE id = themeId AND name = '{theme}');"

        for i in themeList.curselection():
            theme = themeList.get(0, END)[i]
            self.app.db.execute(removeTheme2.format(theme = theme))
            self.app.db.execute(removeTheme.format(theme = theme))

        self.initializeThemeList()
        self.widgets["message"][0].configure(text = "Theme removed from database")


    def resetCommand(self):

        themeEntry = self.widgets["themeEntry"][0]
        pathEntry = self.widgets["pathEntry"][0]
        message = self.widgets["message"][0]

        message.configure(text = "Awaiting actions")
        themeEntry.delete(0, END)
        pathEntry.delete(0, END)

    
    def addThemeCommand(self):

        theme = self.widgets["themeEntry"][0].get()
        insertThemes = "INSERT INTO Theme (name) VALUES('{theme}');"
        self.app.db.execute(insertThemes.format(theme = theme))
        self.initializeThemeList()
        self.widgets["message"][0].configure(text = "Theme added to database")


    def submitionCommand(self):
        
        themeList = self.widgets["themeList"][0]

        if len(themeList.curselection()) <= 0:
            self.widgets["message"][0].configure(text = "No themes selected. Please, select a theme from the theme list")
            return

        path = self.widgets["pathEntry"][0].get()
        insertProblem = "INSERT INTO Problem (location) VALUES('{path}');".format(path = path)
        insertPT = "INSERT INTO ProblemTheme (themeId, problemId) VALUES({idT}, {idP});"
        getThemeIds = "SELECT id FROM Theme WHERE name = '{theme}';"
        getProblemId = "SELECT id FROM Problem WHERE location = '{path}';".format(path = path)

        self.app.db.execute(insertProblem)
        
        themeIds = set()

        for i in themeList.curselection():
            theme = themeList.get(0, END)[i]
            themeIds.add(self.app.db.execute(getThemeIds.format(theme = theme))[0][0])

        problemId = self.app.db.execute(getProblemId)[0][0]

        for i in themeIds:
            self.app.db.execute(insertPT.format(idT = i, idP = problemId))

        self.resetCommand()

        self.widgets["message"][0].configure(text = "Database successfully updated")











