from selenium import webdriver

import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
driver.maximize_window()

print(driver.title)
driver.find_element_by_name("Form_submitForm_subdomain").send_keys("naveen automationlabs")


time.sleep(5)