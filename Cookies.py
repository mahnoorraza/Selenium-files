from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://www.foodpanda.com/")

#capture all the cookies created by browser
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

#add new cookie to a browser
'''
cookie={'name': 'Mycookie','value': '1234567890'}
driver.add_cookie(cookie)

cookies=driver.get_cookies()

#deleting cookie file

driver.delete_cookie('MyCookie')
cookies=driver.get_cookies()
print(len(cookies))'''




