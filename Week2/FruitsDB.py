import sqlite3

# create a connection to a database
con = sqlite3.connect("fruits.db")

# create a cursor
cur = con.cursor()

# create a table
sql_query = "create table if not exists fruit (fruit_id, fruit_name, fruit_qty)"
cur.execute(sql_query)
con.commit()

# insert some data
cur.execute("insert into fruit (fruit_id, fruit_name, fruit_qty) values (1, 'Apples', 50)")
cur.execute("insert into fruit (fruit_id, fruit_name, fruit_qty) values (2, 'Bananas', 10)")
cur.execute("insert into fruit (fruit_id, fruit_name, fruit_qty) values (3, 'Cherries', 80)")
con.commit()

# read some data
cur.execute("select * from fruit where fruit_id = 1")
data = cur.fetchall()
print(data)

total_apples = 0
for item in data:
    total_apples += item[2]

print(total_apples)

# delete some data
cur.execute("delete from fruit where fruit_name = 'Apples'")
con.commit()
# check the data has been deleted
cur.execute("select * from fruit")
data = cur.fetchall()
print(data)

# close the database connection
con.close()