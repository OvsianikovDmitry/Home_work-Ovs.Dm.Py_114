import sqlite3

con = sqlite3.connect('first.db')
cursor = con.cursor()

any_list = ['house',3,'world',5,8,9,'dog','day',7,12]

cursor.execute('''CREATE TABLE IF NOT EXISTS table_text(col_1 TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS table_number(col_1 INTEGER)''')

for i in any_list:
    if type(i) == str:
        cursor.execute('''INSERT INTO table_text(col_1) VALUES (?)''', (i,))
        con.commit()
        num_letters = int(len(i))
        cursor.execute('''INSERT INTO table_number(col_1) VALUES(?)''', (num_letters,))
        con.commit()
    elif type(i)  == int:
        if i%2 == 0:
            cursor.execute('''INSERT INTO table_number(col_1) VALUES(?)''', (i,))
            con.commit()
        else:
            cursor.execute('''INSERT INTO table_text(col_1) VALUES('нечётное')''')
            con.commit()

cursor.execute('''SELECT * FROM table_number''')
number = cursor.fetchall()
con.commit()

count_number = 0
for i in number:
    count_number += 1

if count_number >= 5:
    cursor.execute('''SELECT * FROM table_text''')
    x = cursor.fetchone()
    cursor.execute('''DELETE FROM table_text WHERE col_1 = ? ''', (x))
    con.commit()
else:
    cursor.execute('''SELECT * FROM table_text''')
    x = cursor.fetchone()
    cursor.execute('''UPDATE table_text SET col_1 = 'Hello' WHERE col_1 = ? ''', (x))
    con.commit()