from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Chrome

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")

user_ele=driver.find_element_by_name("userName")
print(user_ele.is_displayed())  #returns true/false based of element status
print(user_ele.is_enabled())     #returns true/false

pwd_ele=driver.find_element_by_name("password")
print(pwd_ele.is_displayed())  #returns true/false based of element status
print(pwd_ele.is_enabled())

user_ele.send_keys(mercury)
pwd_ele.send_keys(mercury)

driver.find_element_by_name("submit").click()
roundrip_radio=driver.find_element_by_css_selector("input[value="roundtrip]")



