import os
import platform




def getOs():
    return platform.system()

    


def getFile(fileName):

    if getOs() == "Windows":
        os.system("start {filename}".format(fileName))
    elif getOs() == "Linux":
        os.system("open {filename}".format(filename = fileName))
    elif getOs() == "Darwin":
        os.system("open {filename}".format(fileName))
