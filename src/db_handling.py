from sqlite3 import *



class Database:

    def __init__(self, dbFileName):

        self.connection = connect(dbFileName)
        self.cursor = self.connection.cursor()

    def execute(self, string):

        try:
            result = list(self.cursor.execute(string))
        except Exception as inst:
            print(type(inst))     
            print(inst)
            return []
        else:
            self.connection.commit()
            return result

"""
database = Database("problems.db")

database.execute("SELECT * FROM Problem;")
"""