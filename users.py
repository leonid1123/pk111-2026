import sqlite3

conn = sqlite3.connect('users.db')
cur = conn.cursor()

sql = '''CREATE TABLE IF NOT EXISTS
Users(Id INTEGER PRIMARY KEY AUTOINCREMENT,
Login TEXT,
Password TEXT,
Name TEXT,
Date_of_birth DATE,
Img TEXT)'''
cur.execute(sql)
conn.commit()

# sql = '''INSERT INTO Users(Login, Password, Name, Date_of_birth, Img)
# VALUES(?,?,?,?,?)'''
# test_data = (
#     ['vasya','1234','OverLord','2000-01-01','01.jpg'],
#     ['petya','1234','SusliK','2005-01-01','02.jpg'],
#     ['masha','1234','PrincessPEPA','2004-01-01','03.jpg'],
# )
# cur.executemany(sql, test_data)
# conn.commit()
cur.execute('SELECT * FROM Users')
print(cur.fetchall())

sql = '''CREATE TABLE IF NOT EXISTS Msg(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Msg_text TEXT,
author INTEGER,
destination INTEGER)
'''
cur.execute(sql)
conn.commit()

# sql = '''INSERT INTO Msg(Msg_text, author, destination)
# VALUES(?,?,?)
# '''
# test_data = (
#     ['от петя к вася',2,1],
#     ['от вася к маша',1,3],
#     ['от маша к петя',3,2],
#     ['всем привет!',1,0],
#     ['Привет, привет',2,0],
#     ['Hi!!!!',3,0]
# )
# cur.executemany(sql,test_data)
# conn.commit()
cur.execute('SELECT * FROM Msg')
print(cur.fetchall())