from gui_app import Application
from gui_menu import *
from db_handling import Database



def main():

    app = Application(Database("problems.db"), "icon.ico")
    app.changeMenu(MainMenu(app), True)
    app.run()



if __name__ == "__main__":
    main()