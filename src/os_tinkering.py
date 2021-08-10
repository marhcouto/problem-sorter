import os
import platform

DIR_NAME = os.path.dirname(__file__)


def getOs():
    return platform.system()

    


def getFile(fileName):

    if getOs() == "Windows":
        os.system("start '{filename}'".format(filename = fileName))
    elif getOs() == "Linux":
        os.system("xdg-open '{filename}'".format(filename = fileName))
    elif getOs() == "Darwin":
        os.system("open '{filename}'".format(filename = fileName))
