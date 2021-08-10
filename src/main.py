from os_tinkering import DIR_NAME

from gui_app import Application
from gui_menu import *
from db_handling import Database



def main():

    databaseName = DIR_NAME + "/../database/problems.db"
    iconName = DIR_NAME + "/../img/icon.ico"

    print(databaseName)
    app = Application(Database(databaseName), iconName)
    app.changeMenu(MainMenu(app), True)
    app.run()



if __name__ == "__main__":
    main()