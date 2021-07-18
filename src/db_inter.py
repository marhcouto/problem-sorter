import sqlite3

connection = sqlite3.connect("../problems.db")

cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = on")
for row in cursor.execute("SELECT * FROM Problem;"):
    print(row)


print(list(cursor.execute("SELECT * FROM Problem;")))


try:
    cursor.execute("INSERT INTO ProblemTheme (problemId, themeId) VALUES(100, 100);")
except sqlite3.IntegrityError:
    print("UNABLE TO PERFORM OPERATION")
else:
    print("ALL OK")
finally:
    print("I HAPPEN ANYWAY")

