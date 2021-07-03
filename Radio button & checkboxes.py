from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

#working with the radio buttons

#status=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
#print(status)

#driver.find_element_by_id("RESULT_RadioButton-7_0").click()

#status=driver.find_element_by_id("RESULT_RadioButton-0_0").is_selected()
#print(status)

#working with checkboxes

driver.find_element_by_id("RESULT_CheckBox-8_0").click()
driver.find_element_by_id("RESULT_CheckBox-8_6").click()

status=driver.find_element_by_id("RESULT_CheckBox-8_0").is_selected()
print(status)



