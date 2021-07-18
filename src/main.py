from gui_window import Window
from gui_menu import Menu
from menu_factory import *
import tkinter as tk
# from db_inter import *



def main():
    gui = tk.Tk()
    gui.geometry("500x200")
    window = Window(gui)
    window.changeMenu(MainMenuFactory(window).makeMenu(), True)
    window.run()

if __name__ == "__main__":
    main()