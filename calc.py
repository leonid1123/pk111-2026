import sqlite3
import random


class App:
    def __init__(self):
        self.conn = sqlite3.connect('dice.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Results(
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Пункт_игры TEXT,
        Описание TEXT,
        Сумма INTEGER)    
        ''')
        self.conn.commit()

        self.cur.execute('SELECT * FROM Results')
        ans = self.cur.fetchall()
        if len(ans) < 1:
            sql = 'INSERT INTO Results(Пункт_игры, Описание) VALUES(?,?)'
            info = (
                ('Школа 1', 'Три кости с гранью 1'),
                ('Школа 2', 'Три кости с гранью 2'),
                ('Школа 3', 'Три кости с гранью 3'),
                ('Школа 4', 'Три кости с гранью 4'),
                ('Школа 5', 'Три кости с гранью 5'),
                ('Школа 6', 'Три кости с гранью 6'),
                ('Пара', 'Две кости с равными гранями'),
                ('Треугольник', 'Три кости с равными гранями'),
                ('Каре', 'Четыре кости с равными гранями'),
                ('Покер', 'Пять костей с равными гранями'),
                ('Две пары', 'Две пары равных граней'),
                ('Фул', 'Две кости с равными гранями и три кости с равными гранями'),
                ('Малая дорога', 'Комбинация значений граней 1-2-3-4-5'),
                ('Большая дорога', 'Комбинация значений граней 2-3-4-5-6'),
                ('Сумма', 'Любая комбинация значений граней'),
                    )
            self.cur.executemany(sql, info)
            self.conn.commit()

        self.cur.execute('SELECT * FROM Results')
        ans = self.cur.fetchall()
        for item in ans:
            print(item)

        name1 = input('Как зовут первого игрока? ')
        name2 = input('Как зовут второго игрока? ')

        dices = [random.randint(1,6),
                random.randint(1,6),
                random.randint(1,6),
                random.randint(1,6),
                random.randint(1,6)]
        for item in range(1,4):
            print(f'Попытка номер {item}')
            print(dices)
            ans = input('какие перебросить? /1,2,3,4,5, 0-ничего /')
            num = ans.split(',')
            if num[0] != '0':
                for i in num:
                    dices[int(i)-1] = random.randint(1,6)


app = App()
app.conn.close()
