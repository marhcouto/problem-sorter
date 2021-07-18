from gui import *
# from db_inter import *



def main():
    gui = Tk()
    gui.geometry("500x200")
    window = Window(gui)
    window.changeMenu(MainMenu(window), True)
    window.run()

if __name__ == "__main__":
    main()