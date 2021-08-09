import os
import platform




def getOs():
    return platform.system()

    


def getFile(fileName):

    print(fileName)

    if getOs() == "Windows":
        os.system("start '{filename}'".format(filename = fileName))
    elif getOs() == "Linux":
        os.system("xdg-open '{filename}'".format(filename = fileName))
    elif getOs() == "Darwin":
        os.system("open '{filename}'".format(filename = fileName))
