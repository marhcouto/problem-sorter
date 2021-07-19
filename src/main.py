from gui_app import Application
from gui_menu import *

# from db_inter import *



def main():

    app = Application()
    app.changeMenu(MainMenu(app), True)
    app.run()

if __name__ == "__main__":
    main()