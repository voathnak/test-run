__author__ = 'vlim'


import psycopg2

connection = psycopg2.connect(database="TrainingDB", user="postgres", password="avalde", host="192.168.30.125", port="5432")

print "Opened database successfully"

cr = connection.cursor()
print cr
cr.execute("""SELECT name FROM product_product""")
# cr.execute('''CREATE TABLE COMPANYdodo
#        (ID INT PRIMARY KEY     NOT NULL,
#        NAME           TEXT    NOT NULL,
#        AGE            INT     NOT NULL,
#        ADDRESS        CHAR(50),
#        SALARY         REAL);''')
# print "Table created successfully"
#
# connection.commit()
rows = cr.fetchall()
print rows
for row in rows:
    print row[0]
connection.close()