from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://project-stack-2b2bd.firebaseapp.com/signup")
driver.maximize_window()
time.sleep(4)

def signup(FirstName, LastName, Email, Password):
    # FirstName
    driver.find_element_by_id("firstName").send_keys(FirstName)
    time.sleep(3)
    # LastName
    driver.find_element_by_id("lastName").send_keys(LastName)
    time.sleep(3)
    #Email
    driver.find_element_by_id("email").send_keys(Email)
    #Password
    driver.find_element_by_id("password").send_keys(Password)
    # Click Signup button
    driver.find_element_by_xpath("//*[@id='root']/div/div[2]/form/div[5]/button").click()
    time.sleep(5)

def createProjects(Title, Project_Content):
    driver.find_element_by_xpath("//*[@id='title']").send_keys(Title)
    time.sleep(3)
    driver.find_element_by_css_selector("#content").send_keys(Project_Content)
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='root']/div/div[2]/form/div[3]/button").click()


def SignIn(Email1, Password1):
    driver.find_element_by_xpath("//*[@id='email']").send_keys(Email1)
    time.sleep(2)
    driver.find_element_by_css_selector("#password").send_keys(Password1)
    time.sleep(2)
    driver.find_element_by_css_selector("#root > div > div.container > form > div:nth-child(4) > button").click()
    time.sleep(3)


def CreateProjects(Title1, Project_Content1):

    driver.find_element_by_xpath("//*[@id='title']").send_keys(Title1)
    time.sleep(3)
    driver.find_element_by_css_selector("#content").send_keys(Project_Content1)
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='root']/div/div[2]/form/div[3]/button").click()
    #driver.find_element_by_xpath("//*[@id='root']/div/div[1]/nav/div/span/ul/li[1]/a")




if __name__ == "__main__":
    #SignUp
    FirstName = ["Mahnoor"]
    LastName = ["Raza"]
    Email = ["Abc117@domain.com"]
    Password = ["12345678"]

    #createproject
    Title = ["MyfirstTest", "MySecondTest", "MythirdTest", "MyFourthTest", "MyFifthtest", "MySixthTest", "MySeventhTest"]
    Project_Content = ["Selenium", "Python", "Appium", "Javascript", "Jmeter", "Blockchain", "Xord"]

    # SignIn
    Email1 = ["Abc111@domain.com"]
    Password1 = ["12345678"]


    #Createagain
    Title1 = ["hello", "hi", "crying", "baby"]
    Project_Content1 = ["ok", "bye", "sweetheart", "ll"]

    #SignUp
    for i in range(0, len(FirstName)):
        signup(FirstName[i], LastName[i], Email[i], Password[i])

    for i in range(0, len(Title)):
        #NewProjectclick
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/nav/div/span/ul/li[1]/a").click()
        time.sleep(2)
        createProjects(Title[i], Project_Content[i])
    #Logout
    driver.find_element_by_xpath("//*[@id='root']/div/div[1]/nav/div/span/ul/li[2]/a").click()

    #SignIn
    for j in range(0, len(Password1)):
        SignIn(Email1[j], Password1[j])

    for j in range(0, len(Project_Content1)):
        #NewProjectagain
        #driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/nav/div/span/ul/li[1]/a").click()
        driver.find_element_by_xpath("// *[ @ id = 'root'] / div / div[1] / nav / div / span / ul / li[1] / a").click()
        time.sleep(2)
        CreateProjects(Title1[j], Project_Content1[j])


    #Select top 5 projects
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='root']/div/div[1]/nav/div/span/ul/li[3]/a").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[1]/div/a[1]/div/div/span").click()
    time.sleep(5)
    driver.back()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[1]/div/a[2]/div/div/span").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[1]/div/a[3]/div/div/span").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[1]/div/a[4]/div/div/span").click()
    time.sleep(5)
    driver.back()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[1]/div/a[5]/div/div/span").click()
    time.sleep(4)
  #Logout
driver.find_element_by_xpath("//*[@id='root']/div/div[1]/nav/div/span/ul/li[2]/a").click()
time.sleep(3)
driver.close()