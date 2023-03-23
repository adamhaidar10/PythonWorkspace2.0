from fastapi import FastAPI
import pymysql
from pydantic import BaseModel
app = FastAPI()


class Contact(BaseModel):
    firstname : str
    lastname : str
    city : str
    phonenumber : int
    emailaddress : str





@app.get("/contacts")
def api_get_contacts(firstname : str = ""):
    # connect to the database
    con = pymysql.connect(host="localhost", user="root", password="root123", database="onlineStore")
    cur = con.cursor()

    # query the database
    if firstname == "":
        sql = "select * from contacts"
    else:
        sql = f"select * from contacts where first_name = '{firstname}'"

    cur.execute(sql)
    res = cur.fetchall()
    
    
    
    # close the database connection
    cur.close()
    con.close()


    
    # format the results
    l = []
    
    for contact in res:
        d = {"id" : contact[0],
            "first_name" : contact[1],
             "last_name"  : contact[2],
             "city" : contact[3],
             "phone_number" : contact[4],
             "email_address" : contact[5]}



        l.append(d)
    return l

@app.post("/contacts")
def api_post_contact(contact : Contact):
    # connectt to the database
    con = pymysql.connect(host="localhost", user="root", password="root123", database="onlineStore")
    cur = con.cursor()


    # run a query to insert data
    sql = f"insert into contacts(first_name, last_name, city, phone_number, email_address) values('{contact.firstname}','{contact.lastname}', '{contact.city}', {contact.phonenumber}, '{contact.emailaddress}')"
    cur.execute(sql)
    con.commit()
    # close the connection
    cur.close()
    con.close()

    # return something to the calling application
    return {"message": "inserted"}


    





