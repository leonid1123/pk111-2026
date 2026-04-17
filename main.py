import sqlite3
conn = sqlite3.connect('users.db')
cur = conn.cursor()

cur.execute('SELECT * FROM Users')
print(cur.fetchall())
cur.execute('SELECT * FROM Msg')
print(cur.fetchall())

def get_id(_name):
    sql = 'SELECT Id FROM Users WHERE name=?'
    cur.execute(sql,(_name,))
    id = cur.fetchone()[0]
    print("OverLord id - ", id)
    return id


sql = '''SELECT Msg.Msg_text, Users.name 
FROM Msg
INNER JOIN Users
ON Users.id = Msg.destination 
WHERE Msg.destination=?'''
cur.execute(sql, (get_id("OverLord"),))
ans = cur.fetchall()[0]
print(ans)
print(ans[1], '-написал-', ans[0])



