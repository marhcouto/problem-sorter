from tkinter import CENTER, Button, Entry, Label, LabelFrame, Listbox, font, S, N, NE, NW, END, Message, Tk

from position import Position
import os_tinkering
from PIL import Image, ImageTk




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

        self.image = ImageTk.PhotoImage(Image.open("img/theme.png"))

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
        self.addWidget("searchFrame", LabelFrame(self.app.gui, text = "Search Options", height = 400, width = 400, relief = "sunken", labelanchor = N, font = font.Font(size = 18)), 
        Position(0.05, 0.15, Position.MODE_RELATIVE, NW))
        self.addWidget("resultsFrame", LabelFrame(self.app.gui, text = "Results", height = 400, width = 400, relief = "sunken", labelanchor = N, font = font.Font(size = 18)), 
        Position(0.95, 0.15, Position.MODE_RELATIVE, NE))

        # LEFTSIDE
        self.addWidget("themeListLabel", Label(self.widgets["searchFrame"][0], text = "Themes", font = font.Font(size = 12, weight = "bold")), 
        Position(0.5, 0.29, Position.MODE_RELATIVE, CENTER))

        self.addWidget("themeList", Listbox(self.widgets["searchFrame"][0], height = 16, width = 50, selectmode = "multiple"), 
        Position(0.5, 0.85, Position.MODE_RELATIVE, S))

        self.initializeThemeList()

        # RIGHTSIDE
        self.addWidget("resultList", Listbox(self.widgets["resultsFrame"][0], height = 16, width = 50), 
        Position(0.5, 0.85, Position.MODE_RELATIVE, S))

        self.addWidget("resultListLabel", Label(self.widgets["resultsFrame"][0], text = "Files", font = font.Font(size = 12, weight = "bold")),
        Position(0.5, 0.29, Position.MODE_RELATIVE, CENTER))

        self.addWidget("messageLabel", Label(self.widgets["resultsFrame"][0], text = "Messages", font = font.Font(size = 12, weight = "bold")), 
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
 
        self.addWidget("goBack", Button(self.app.gui, text = "Go Back", 
        command = lambda : self.app.changeMenu(MainMenu(self.app), False)), 
        Position(0.2, 0.9, Position.MODE_RELATIVE, CENTER))

        self.addWidget("search", Button(self.app.gui, text = "Search Files",
        command = self.searchCommand),
        Position(0.5, 0.9, Position.MODE_RELATIVE, CENTER))


    def initializeThemeList(self):

        self.refreshThemes()

        getThemesQuery = "SELECT name FROM Theme;"
        themeList = self.widgets["themeList"][0]

        themeList.delete(0, END)

        for line in self.app.db.execute(getThemesQuery):
            themeList.insert(0, line[0])


    def refreshThemes(self):

        eliminateThemesQuery = "DELETE FROM Theme WHERE NOT EXISTS (SELECT * FROM ProblemTheme WHERE themeId = Theme.id);"
        self.app.db.execute(eliminateThemesQuery)


    def lookupCommand(self):

        if len(self.widgets["resultList"][0].curselection()) <= 0:
            self.widgets["message"][0].configure(text = "No files selected. Please select a file")
            return

        newWindow = Tk()
        newWindow.geometry("400x200")
        newWindow.title("Choose viewer app")

        okButton = Button(newWindow, text = "OK", command = lambda : [(lambda : os_tinkering.getFile(fileName, newList.get(0, END)[newList.curselection()[0]]))(), (lambda : newWindow.destroy())()])
        newList = Listbox(newWindow, width = 20, height = 9)
        newLabel = Label(newWindow, text = "Choose a program to visualize the file", font = font.Font(size = 12))

        newList.insert(0, "Word")
        newList.insert(0, "LibreOffice")
        
        newList.place(relx = 0.5, rely = 0.8, anchor = S)
        newLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        okButton.place(relx = 0.5, rely = 0.9, anchor = CENTER)

        fileName = self.widgets["resultList"][0].get(0, END)[self.widgets["resultList"][0].curselection()[0]]
    

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


    def deleteCommand(self):

        if len(self.widgets["resultList"][0].curselection()) <= 0:
            self.widgets["message"][0].configure(text = "No files selected. Please select a file")
            return

        fileName = self.widgets["resultList"][0].get(0, END)[self.widgets["resultList"][0].curselection()[0]]

        query1 = "DELETE FROM ProblemTheme WHERE ProblemTheme.problemId = (SELECT id FROM Problem WHERE location = '{filename}');"
        query2 = "DELETE FROM Problem WHERE location = '{filename}';"

        self.app.db.execute(query1.format(filename = fileName))
        self.app.db.execute(query2.format(filename = fileName))
        self.widgets["message"][0].configure(text = "{file} was successfully removed from the database".format(file = fileName))

        self.searchCommand()
        self.initializeThemeList()
    


class InfoMenu(GUIMenu):

    def __init__(self, app):
        super().__init__(app)

    def makeMenu(self):
        self.addWidget("menuLabel", Label(self.app.gui, text = "Instructions", font = font.Font(size = 26)),
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))
        self.addWidget("message", Message(self.app.gui, width = 800, text = " - In the search menu, you can search for exercises/exams containing exercises that associate with the themes you chose," +
                                                                    "followed by lookup of the file or elimination of its registry.\n\n" +
                                                                    " - When multiple themes are selected, the files presented are the ones which associate with at least one of the themes.\n\n" + 
                                                                    " - In the insertion menu, you can insert new entries in the database, filling in the fields with the corresponding info." + 
                                                                    "For one file, multiple themes can be inserted.\n\n" + 
                                                                    " - When a theme no longer has files associated to it, it will be automatically eliminated.\n\n" +
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
        self.addWidget("menuLabel", Label(self.app.gui, text = "Inserting Menu", font = font.Font(size = 26)),
        Position(0.5, 0.1, Position.MODE_RELATIVE, CENTER))

        # LABELS
        self.addWidget("themeLabel", Label(self.app.gui, text = "Theme", font = font.Font(size = 12, weight = "bold")),
        Position(0.3, 0.2, Position.MODE_RELATIVE, CENTER))
        self.addWidget("pathLabel", Label(self.app.gui, text = "Document's path", font = font.Font(size = 12, weight = "bold")),
        Position(0.7, 0.2, Position.MODE_RELATIVE, CENTER))
        self.addWidget("listLabel", Label(self.app.gui, text = "Themes selected", font = font.Font(size = 12, weight = "bold")),
        Position(0.5, 0.35, Position.MODE_RELATIVE, CENTER))
        self.addWidget("messageLabel", Label(self.app.gui, text = "Messages", font = font.Font(size = 12, weight = "bold")),
        Position(0.75, 0.35, Position.MODE_RELATIVE, CENTER))

        # LIST
        self.addWidget("themeList", Listbox(self.app.gui, height = 16, width = 50), 
        Position(0.5, 0.7, Position.MODE_RELATIVE, S))

        # ENTRIES
        self.addWidget("themeEntry", Entry(self.app.gui, relief = "flat"),
        Position(0.3, 0.25, Position.MODE_RELATIVE, CENTER))
        self.addWidget("pathEntry", Entry(self.app.gui, relief = "flat"),
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
            self.widgets["message"][0].configure(text = "No themes selected. Please, add a theme to the theme list")
            return

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











