# Imports
import sqlite3

# Variables
database = sqlite3.connect("fartass2.db")
cursor = database.cursor()


# Functions
def getMessages():
    query = list(cursor.execute('SELECT message FROM messages').fetchall())

    for i in range(0, len(query)):
        query[i] = query[i][0]

    return query


def addMessage(message):
    cursor.execute("INSERT INTO messages VALUES (?)", [message])
    database.commit()
