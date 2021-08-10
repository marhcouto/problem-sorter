import os
import platform
import sys

DIR_NAME = sys._MEIPASS if getattr(sys, 'frozen', False) else os.path.dirname(__file__)


def getOs():
    return platform.system()

    


def getFile(fileName):

    if getOs() == "Windows":
        os.system("start '{filename}'".format(filename = fileName))
    elif getOs() == "Linux":
        os.system("xdg-open '{filename}'".format(filename = fileName))
    elif getOs() == "Darwin":
        os.system("open '{filename}'".format(filename = fileName))
