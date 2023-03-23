# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# # create web driver object
# wd = webdriver.Chrome()
# # navigate to a webpage
# wd.get("http://35.178.198.206/index.html")


# time.sleep(5)

# # navigate to another page
# l = wd.find_element(By.PARTIAL_LINK_TEXT, "little picture") 

# l.click()
# time.sleep(5)
# # nav back to homepage
# d = wd.find_element(By.LINK_TEXT, "Go back to index page")
# d.click()
# By.PARTIAL_LINK_TEXT, "little picture"
# time.sleep(5)
# # filled in fields in form
# f = wd.find_element(By.NAME, "name")
# f.send_keys("Jane")

# f = wd.find_element(By.NAME, "commenttext")
# f.send_keys("This is a comment entered by Jane")
# time.sleep(5)

# f = wd.find_element(By.NAME, "commentlocation")
# f.send_keys("Taipei")
# time.sleep(5)
# # submitted form
# f.submit()
# time.sleep(5)
# # nav back to homepage
# l = wd.find_element(By.LINK_TEXT, "Back to home")
# l.click()
# time.sleep(5)

# # close browser
# print(type(l))


# wd.quit



import time
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

# go to the cards query page and enter a query
wd.get("http://<AUT IP>/getcard.html")
wd.find_element(By.NAME, "cardholder").send_keys("Betty")
wd.find_element(By.NAME, "cardholder").submit()

# pause while the page loads
time.sleep(2)

# get a reference to the table
table = wd.find_element(By.CSS_SELECTOR, "html > body > table")

# find the number of rows in the table
rows = table.find_elements(By.XPATH, "//tr")
print("Number of rows : {}".format(len(rows)))

# loop round each row
i = 1
while i < len(rows):
    # count the columns on this row
    columns = rows[i].find_elements(By.XPATH, "td")
    print("Row {} has {} columns".format(i, len(columns)))

    # loop round each column
    j = 0
    while j < len(columns):
        cell_data = columns[j].text
        print("{}, {} : {}".format(i, j, cell_data))
        j += 1

    i += 1