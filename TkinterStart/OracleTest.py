import cx_Oracle as Oracle

connection = Oracle.connect('system/admin@localhost/xe')
cursor = connection.cursor()

cursor.execute('SELECT * FROM PHONE_DETAILS')

print(cursor.fetchone())

rows = cursor.fetchall()
for row in rows:
    print(row[1])

cursor.close()
connection.close()
