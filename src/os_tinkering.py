import os
import platform




def getFile(fileName, viewerName):

    print(fileName, viewerName)


    if platform.system() == "Windows":
        print("windows")
    elif platform.system() == "Linux":
        """
        username = getpass.getuser()
        print(username)
        os.system("ls -l {f}".format(f = fileName))
        os.system("chown " + username + " " + fileName)
        os.system("chmod u+rx " + fileName)
        os.system("ls -l {f}".format(f = fileName))
        os.system("open " + fileName)
        """

        if (viewerName == "LibreOffice"):
            os.system("libreoffice --writer '{filename}'".format(filename = fileName))
        else:
            print("Invalid viewer app")

    elif platform.system() == "Darwin":
        print("apples")
