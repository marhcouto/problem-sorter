from os_tinkering import DIR_NAME, DB_PATH, ICON_PATH

from gui_app import Application
from gui_menu import *
from db_handling import Database



def main():

    app = Application(Database(DB_PATH), ICON_PATH)
    app.changeMenu(MainMenu(app), True)
    app.run()



if __name__ == "__main__":
    main()