import os
import platform
import getpass




def getFile(fileName):
    if platform.system() == "Windows":
        print("windows")
    elif platform.system() == "Linux":
         
        username = getpass.getuser()
        print(username)
        os.system("ls -l {f}".format(f = fileName))
        os.system("chown " + username + " " + fileName)
        os.system("chmod u+rx " + fileName)
        os.system("ls -l {f}".format(f = fileName))
        os.system("open " + fileName)
        
        print("penguins")
    elif platform.system() == "Darwin":
        print("apples")
