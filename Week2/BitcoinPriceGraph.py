import requests
import json
import sqlite3
from matplotlib import pyplot

# create database if it doesn't exist
dbc = sqlite3.connect("bitcoinanalysis.db")
cursor = dbc.cursor()

# create table if it doesn't exist
sql = "create table if not exists prices (month text, high real, low real)"
cursor.execute(sql)
dbc.commit()

# delete any existing data in the table (from previous runs)
sql = "delete from prices"
cursor.execute(sql)
dbc.commit()

# call the api to get monthly time series data
url = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&symbol=BTC&market=GBP&apikey=put-your-API-key-here"
res = requests.get(url)
content = res.content.decode("utf-8")

# turn the response into json
jsoncontent = json.loads(content)

# examine the json
for month in jsoncontent["Time Series (Digital Currency Monthly)"]:
    # get high and low prices
    highvalue = float(jsoncontent["Time Series (Digital Currency Monthly)"][month]["2a. high (GBP)"])
    lowvalue = float(jsoncontent["Time Series (Digital Currency Monthly)"][month]["3a. low (GBP)"])
    print(f"{month} : {highvalue} : {lowvalue}")

    # insert into the database
    sql = f"insert into prices values('{month}', {highvalue}, {lowvalue})"
    #print(sql)
    cursor.execute(sql)
    dbc.commit()

print("-----------------------------------------------------")

# check the data is in the database
sql = "select * from prices"
cursor.execute(sql)
data = cursor.fetchall()
#print(data)

print("-----------------------------------------------------")

# select the highest and lowest prices from the data
sql = "select month, high from prices where high = (select max(high) from prices)"

cursor.execute(sql)
data = cursor.fetchall()
print(f"The highest ever price was {data[0][1]} on {data[0][0]}")

sql = "select month, low from prices where low = (select min(low) from prices)"
cursor.execute(sql)
data = cursor.fetchall()
print(f"The lowest ever price was {data[0][1]} on {data[0][0]}")

print("-----------------------------------------------------")

# get the user to input a year and show the data just for that year
y = input("Enter a year from 2020 to 2023 : ")

sql = f"select month, high from prices where high = (select max(high) from prices where substr(month, 1, 4) = '{y}')"
cursor.execute(sql)
data = cursor.fetchall()
print(f"The highest price in {y} was {data[0][1]} on {data[0][0]}")

sql = f"select month, low from prices where low = (select min(low) from prices where substr(month, 1, 4) = '{y}')"
cursor.execute(sql)
data = cursor.fetchall()
print(f"The lowest price in {y} was {data[0][1]} on {data[0][0]}")

print("-----------------------------------------------------")

# draw a graph of the highest price over time
# get the data from the database
sql = "select month, high from prices"
cursor.execute(sql)
data = cursor.fetchall()
#print(data)
# the data will have the most recent month first (that is how it is returned by the API)
# so reverse it so the oldest month is first
data.reverse()

# copy the data into two separate lists (easier for Matplotlib)
months = []
values = []
for t in data:
    months.append(t[0])
    values.append(t[1])

#print(months)
#print(values)

# Build up the plot, then show it
pyplot.plot(months, values, color="blue", marker="x", linestyle="solid")
pyplot.title = "Price of Bitcoin"
pyplot.ylabel = "£"
pyplot.xlabel = "Month"
pyplot.xticks(rotation=45, ha="right")
pyplot.show()