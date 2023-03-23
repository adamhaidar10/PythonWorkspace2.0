import sqlite3

con = sqlite3.connect("books.db")
cur = con.cursor()

cur.execute("create table if not exists books (title text, author text)")
cur.execute("insert into books values ('War and Peace', 'Tolstoy, Leo')")
cur.execute("insert into books values ('Pride and Prejudice', 'Austen, Jane')")
cur.execute("insert into books values ('Great Expectations', 'Dickens, Charles')")


con.commit()




cur.execute("select * from books")
res = cur.fetchall()

bookdata = [("Jude the Obscure", "Hardy, Thomas"),
("Middlemarch", "Eliot, George"),
("Animal Farm", "Orwell, George")]
cur.executemany("insert into books values(?, ?)", bookdata)
con.commit()
print(res)





con.close()