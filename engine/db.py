import csv
import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO sys_command VALUES (null,'excel', 'C://ProgramData//Microsoft//Windows//Start Menu//Programs//Excel.lnk')"
cursor.execute(query)
con.commit()
query = "INSERT INTO sys_command VALUES (null,'powerpoint', 'C://ProgramData//Microsoft//Windows//Start Menu//Programs//PowerPoint.lnk')"
cursor.execute(query)
con.commit()
query = "INSERT INTO sys_command VALUES (null,'word', 'C://ProgramData//Microsoft//Windows//Start Menu//Programs//Word.lnk')"
cursor.execute(query)
con.commit()
query = "INSERT INTO sys_command VALUES (null,'google chrome', 'C://ProgramData//Microsoft//Windows//Start Menu//Programs//Google Chrome.lnk')"
cursor.execute(query)
con.commit()
query = "INSERT INTO web_command VALUES (null,'gmail', 'https://mail.google.com/mail/u/0/#inbox')"
cursor.execute(query)
con.commit()
query = "INSERT INTO web_command VALUES (null,'google maps', 'https://www.google.com/maps/@14.5965592,77.6558435,15.78z?entry=ttu')"
cursor.execute(query)
con.commit()
query = "INSERT INTO web_command VALUES (null,'best college website in anantapur', 'http://www.alits.ac.in/')"
cursor.execute(query)
con.commit()

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
# cursor.execute(query)
# con.commit()


# testing module
# app_name = "android studio"
# cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
# results = cursor.fetchall()
# print(results[0][0])

# Create a table with the desired columns
#cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')


# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 30]

# # Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # Commit changes and close connection
# con.commit()
# con.close()

# query = "INSERT INTO contacts VALUES (null,'pawan', '1234567890', 'null')"
# cursor.execute(query)
# con.commit()

# query = 'kunal'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])

def new_func(con, cursor):
    query = "INSERT INTO contacts VALUES (null,'madhu', '6305313849','null')"
    cursor.execute(query)
    con.commit()

def new_func(con, cursor):
    query = "INSERT INTO contacts VALUES (null,'Gopi', '8919736998','null')"
    cursor.execute(query)
    con.commit()