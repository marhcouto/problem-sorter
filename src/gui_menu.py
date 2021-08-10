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

        self.addWidget("searchButton", Button(self.app.gui, text = "Start", 
        command = lambda : self.app.changeMenu(SearchMenu(self.app), False)), 
        Position(0.3, 0.9, Position.MODE_RELATIVE, CENTER))
        self.addWidget("instructionsButton", Button(self.app.gui, text = "Instructions", 
        command = lambda : self.app.changeMenu(InfoMenu(self.app), False)),
        Position(0.7, 0.9, Position.MODE_RELATIVE, CENTER))
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
        self.addWidget("menuLabel", Label(self.app.gui, text = "Use/Manage Database", font = font.Font(size = 26)),
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))
        
        # FRAMES
        self.addWidget("themesFrame", LabelFrame(self.app.gui, text = "Search Options", height = 300, width = 400, relief = "sunken", labelanchor = N, font = font.Font(size = 18)), 
        Position(0.05, 0.15, Position.MODE_RELATIVE, NW))
        self.addWidget("resultsFrame", LabelFrame(self.app.gui, text = "Results", height = 300, width = 400, relief = "sunken", labelanchor = N, font = font.Font(size = 18)), 
        Position(0.95, 0.15, Position.MODE_RELATIVE, NE))
        self.addWidget("messageFrame", LabelFrame(self.app.gui, text = "Messages", height = 100, width = 700, relief = "sunken", labelanchor = N, font = font.Font(size = 18)),
        Position(0.5, 0.68, Position.MODE_RELATIVE, N))

        # LEFTSIDE
        self.addWidget("themeListLabel", Label(self.widgets["themesFrame"][0], text = "Themes", font = font.Font(size = 14, underline = True)), 
        Position(0.08, 0.08, Position.MODE_RELATIVE, W))
        self.addWidget("themeList", Listbox(self.widgets["themesFrame"][0], height = 10, width = LIST_WIDTH, selectmode = "multiple"), 
        Position(0.5, 0.85, Position.MODE_RELATIVE, S))
        self.addWidget("themeEntry", Entry(self.widgets["themesFrame"][0], relief = "sunken"),
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))

        self.initializeThemeList()

        # RIGHTSIDE
        self.addWidget("resultList", Listbox(self.widgets["resultsFrame"][0], height = 10, width = LIST_WIDTH), 
        Position(0.5, 0.85, Position.MODE_RELATIVE, S))
        self.addWidget("resultListLabel", Label(self.widgets["resultsFrame"][0], text = "Files", font = font.Font(size = 14, underline = True)),
        Position(0.08, 0.08, Position.MODE_RELATIVE, W))
        self.addWidget("pathEntry", Entry(self.widgets["resultsFrame"][0], relief = "sunken"),
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))

        self.addWidget("message", Message(self.app.gui, text = "Awaiting actions", width = 600),
        Position(0.2, 0.73, Position.MODE_RELATIVE, NW))

        # BUTTONS
        self.addWidget("lookupButton", Button(self.app.gui, text = "Look up", 
        command =  self.lookupCommand),
        Position(0.4, 0.9, Position.MODE_RELATIVE, CENTER))
        self.addWidget("deleteButton", Button(self.widgets["resultsFrame"][0], text = "Remove problem",
        command = self.removeProblemCommand),
        Position(0.7, 0.925, Position.MODE_RELATIVE, CENTER))
        self.addWidget("goBack", Button(self.app.gui, text = "Go Back", 
        command = lambda : self.app.changeMenu(MainMenu(self.app), False)), 
        Position(0.2, 0.9, Position.MODE_RELATIVE, CENTER))
        self.addWidget("search", Button(self.app.gui, text = "Search Files",
        command = self.searchCommand),
        Position(0.6, 0.9, Position.MODE_RELATIVE, CENTER))
        self.addWidget("reset", Button(self.app.gui, text = "Reset",
        command = self.resetCommand),
        Position(0.8, 0.9, Position.MODE_RELATIVE, CENTER))
        self.addWidget("addThemeButton", Button(self.widgets["themesFrame"][0], text = "Add theme",
        command = self.addThemeCommand),
        Position(0.3, 0.925, Position.MODE_RELATIVE, CENTER))
        self.addWidget("removeThemeButton", Button(self.widgets["themesFrame"][0], text = "Remove theme", 
        command = self.removeThemeCommand),
        Position(0.7, 0.925, Position.MODE_RELATIVE, CENTER))
        self.addWidget("addProblemButton", Button(self.widgets["resultsFrame"][0], text = "Add problem", 
        command =  self.addProblemCommand),
        Position(0.3, 0.925, Position.MODE_RELATIVE, CENTER))


    def resetCommand(self):

        resultList = self.widgets["resultList"][0]
        themeEntry = self.widgets["themeEntry"][0]
        pathEntry = self.widgets["pathEntry"][0]
        message = self.widgets["message"][0]

        themeEntry.delete(0, END)
        pathEntry.delete(0, END)
        message.configure(text = "Awaiting actions")
        resultList.delete(0, END)


    def initializeThemeList(self):

        getThemesQuery = "SELECT name FROM Theme;"
        themeList = self.widgets["themeList"][0]

        themeList.delete(0, END)

        for line in self.app.db.execute(getThemesQuery):
            themeList.insert(0, line[0])

    
    def addThemeCommand(self):
        
        themeEntry = self.widgets["themeEntry"][0]
        theme = self.widgets["themeEntry"][0].get()

        themeEntry.delete(0, END)
        insertThemes = "INSERT INTO Theme (name) VALUES('{theme}');"
        self.app.db.execute(insertThemes.format(theme = theme))
        self.initializeThemeList()
        self.widgets["message"][0].configure(text = "Theme added to database")

    
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


    def removeProblemCommand(self):

        if len(self.widgets["resultList"][0].curselection()) <= 0:
            self.widgets["message"][0].configure(text = "No files selected. Please select a file")
            return

        fileName = self.widgets["resultList"][0].get(0, END)[self.widgets["resultList"][0].curselection()[0]]

        query1 = "DELETE FROM ProblemTheme WHERE ProblemTheme.problemId = (SELECT id FROM Problem WHERE location = '{filename}');"
        query2 = "DELETE FROM Problem WHERE location = '{filename}';"

        self.app.db.execute(query1.format(filename = fileName))
        self.app.db.execute(query2.format(filename = fileName))

        self.searchCommand()
        self.widgets["message"][0].configure(text = "File successfully removed from the database")


    def addProblemCommand(self):
        
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

    


class InfoMenu(GUIMenu):

    def __init__(self, app):
        super().__init__(app)


    def makeMenu(self):
        self.addWidget("menuLabel", Label(self.app.gui, text = "Instructions", font = font.Font(size = 26)),
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))
        self.addWidget("message", Message(self.app.gui, width = 800, text = " - You can search for exercises/exams containing exercises that associate with the themes you selected on the theme list by pressing the 'Search' button." +
                                                                    " If no theme is selected, the search will retrieve all file paths registered in the database." +
                                                                    " When multiple themes are selected, the files presented are the ones which associate with at least one of the themes.\n\n" + 
                                                                    " - You can add new themes by entering their name in the left entry box and pressing the 'Add theme' button. Eliminating them is done by selecting from the theme list the themes you desired to remove and hitting the 'Remove theme' button.\n\n" + 
                                                                    " - Adding new file paths to the system is done in a similar manner, but you are required to select the themes you want to associate with the file prior to clicking the 'Add problem' button. For one file, multiple themes can be selected.\n\n" + 
                                                                    " - If you want to associate a file with one or more new themes, just type the name of the file and proceed as you would to add a new file.\n\n" + 
                                                                    " - Reset buttons serve to reset the menu to its initial state, deleting the results of a search for example.", 
                                                                    font = font.Font(family = "Arial", size = 14)),
        Position(0.1, 0.2, Position.MODE_RELATIVE, NW))
        self.addWidget("goBack", Button(self.app.gui, text = "Go Back", 
        command = lambda : self.app.changeMenu(MainMenu(self.app), False)), 
        Position(0.2, 0.9, Position.MODE_RELATIVE, CENTER))

