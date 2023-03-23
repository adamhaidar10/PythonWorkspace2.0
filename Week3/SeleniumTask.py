from selenium import webdriver
from selenium.webdriver.common.by import By
import time

wd = webdriver.Chrome()

wd.get("http://35.178.198.206/index.html")

time.sleep(3)

card = wd.find_element(By.LINK_TEXT, "Enter credit card details")
card.click()

time.sleep(3)

c = wd.find_element(By.NAME, "cardholder")
c.send_keys("Peter Parker")

c = wd.find_element(By.NAME, "cardnumber")
c.send_keys("1234 5678 9101 1121")

c = wd.find_element(By.NAME, "cardtype")
c.send_keys("Visa")

c = wd.find_element(By.NAME, "expirymonth")
c.send_keys("12")

c = wd.find_element(By.NAME, "expiryyear")
c.send_keys("2026") 
time.sleep(2)
c.submit()
time.sleep(5)

c = wd.find_element(By.LINK_TEXT, "Go back to index")
c.click()
time.sleep(5)

c = wd.find_element(By.LINK_TEXT, "Retrieve credit card details")
c.click()
time.sleep(5)

c = wd.find_element(By.NAME, "cardholder")
c.send_keys("Peter Parker")
time.sleep(3)
c.submit()
time.sleep(4)

c = wd.find_element(By.LINK_TEXT, "Go back to index")
c.click()
time.sleep(3)



wd.quit