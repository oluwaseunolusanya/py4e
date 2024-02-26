'''Application reads mailbox data and counts the number of emails messages
   per organisation i.e. the domain of the email address using a database.'''

import sqlite3

conn = sqlite3.connect("orgdb.sqlite")    # Connect to orgdb if it exists or create it if not.
cur = conn.cursor() # Create a cursor object to query and retrieve data from emaildb.

cur.execute("DROP TABLE IF EXISTS Counts")
cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

fname = input ("Enter file name:")
if (len(fname) < 1):
    fname = "mbox.txt"
fhand = open(fname)
for line in fhand:
    if not line.startswith("From: "):
        continue
    words = line.split()
    email = words[1]
    org = email.split("@")[1]
    print(type(org))
    cur.execute("SELECT count FROM Counts WHERE org = ? ",(org,))
    row = cur.fetchone() # Retrieve a row from the SELECT query result
    if row is None:
        cur.execute("INSERT INTO Counts (org,count) VALUES (?, 1)", (org,))
    else:
        cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?",(org,))
    conn.commit()

    sqlstring = "SELECT org, count FROM Counts ORDER BY count DESC"

    for row in cur.execute(sqlstring):
        print(str(row[0]), row[1])
    
cur.close()