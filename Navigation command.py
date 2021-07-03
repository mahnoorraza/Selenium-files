from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Chrome

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")

print(driver.title)

driver.get("http://paventestingtools.blogspot.in/")
time.sleep(5)

print(driver.title)
driver.back()

time.sleep(5)
print(driver.title)

driver.forward()
time.sleep(5)
print(driver.title)
