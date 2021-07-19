import os
import platform
import getpass




def getFile(fileName):
    if platform.system() == "Windows":
        print("windows")
    elif platform.system() == "Linux":
        """ 
        username = getpass.getuser()
        print(username)
        os.system("chown " + username + " " + fileName)
        os.system(fileName)
        """
        print("penguins")
    elif platform.system() == "Darwin":
        print("apples")
