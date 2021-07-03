from selenium import webdriver



driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/register.php")

driver.save_screenshot("C:\Screenshots\homepage1.png")

driver.get_screenshot_as_file("C:\Screenshots\homepage2.png")