from sqlite3 import *



class Database:

    def __init__(self, dbFileName):

        self.cursor = connect(dbFileName).cursor()

    def execute(self, string):

        try:
            result = list(self.cursor.execute(string))
        except Exception as inst:
            print(type(inst))    
            print(inst.args)     
            print(inst)
            return []
        else:
            print(result)
            return result

"""
database = Database("problems.db")

database.execute("SELECT * FROM Problem;")
"""