'''Application models a Learning Management System with a Many-to-Many Relationship.'''

import sqlite3

conn = sqlite3.connect("lmsdb.sqlite")    # Connect to lmsdb if it exists or create it if not.
cur = conn.cursor() # Create a cursor object to execute SQL commands.


cur.execute("DROP TABLE IF EXISTS User")
cur.execute('''CREATE TABLE User (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT UNIQUE,
                email TEXT)
            ''')

cur.execute("DROP TABLE IF EXISTS Course")
cur.execute('''CREATE TABLE Course (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                title TEXT UNIQUE)
            ''')

cur.execute("DROP TABLE IF EXISTS Member")
cur.execute('''CREATE TABLE Member (
                user_id INTEGER,
                course_id INTEGER,
                role INTEGER,
                PRIMARY KEY (user_id, course_id))
            ''')

cur.execute('''INSERT INTO User (name, email) 
               VALUES ("Jane", "jane@email.com")''')
cur.execute('''INSERT INTO User (name, email) 
               VALUES ("John", "john@email.com")''')
cur.execute('''INSERT INTO User (name, email) 
               VALUES ("Ed", "ed@email.com")''')
            
cur.execute('''INSERT INTO Course (title) 
               VALUES ("Python")''')
cur.execute('''INSERT INTO Course (title) 
               VALUES ("SQL")''')
cur.execute('''INSERT INTO Course (title) 
               VALUES ("PHP")''')
    
conn.commit()

cur.close()