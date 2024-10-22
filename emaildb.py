import sqlite3
import re  # Import re for regular expressions

# Connect to the SQLite database
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Drop the table if it already exists and create a new one
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

# Get the file name from user input
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'

# Open the file for reading
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    # Extract the domain from the email address
    domain = email.split('@')[1]

    # Check if the domain is already in the database
    cur.execute('SELECT count FROM Counts WHERE org = ?', (domain,))
    row = cur.fetchone()
    
    if row is None:
        # If the domain is not found, insert it with a count of 1
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain,))
    else:
        # If it is found, update the count
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))

# Commit changes to the database outside the loop for efficiency
conn.commit()

# Select and print the top 10 organizations by count
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# Close the connection
cur.close()
