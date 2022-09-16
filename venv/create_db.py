import sqlite3

connection = sqlite3.connect('newdata_db.sqlite')

connection.execute("""
    CREATE TABLE info(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        prices TEXT,
        urls TEXT
        )
""")