import os
import platform
import sys

DIR_NAME = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(__file__)
DB_PATH = DIR_NAME + "/database/problems.db" if getattr(sys, 'frozen', False) else DIR_NAME + "/../database/problems.db"
ICON_PATH = DIR_NAME + "/img/icon.ico" if getattr(sys, 'frozen', False) else DIR_NAME + "/../img/icon.ico"
IMAGE_PATH = DIR_NAME + "/img/theme.png" if getattr(sys, 'frozen', False) else DIR_NAME + "/../img/theme.png"


def getOs():
    return platform.system()

    


def getFile(fileName):

    if getOs() == "Windows":
        os.system("start '{filename}'".format(filename = fileName))
    elif getOs() == "Linux":
        os.system("xdg-open '{filename}'".format(filename = fileName))
    elif getOs() == "Darwin":
        os.system("open '{filename}'".format(filename = fileName))
