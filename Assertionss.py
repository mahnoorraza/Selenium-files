#import unittest
#from selenium import webdriver




#class Test(unittest.TestCase):
 #   def testName(self):
  #      driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
   #     driver.get("https://www.google.com/")
    #    titleOfWebPage=driver.title

        #self.assertEqual("Google123",titleOfWebPage,"webpages titles are not same")
     #   self.assertNotEqual("Google", titleOfWebPage)

#if __name__ == "__main__":
 #       unittest.main()

# - - -------------------------------------------------------------------------------

import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        #driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        #driver = None
        #driver.get("https://google.com/")
        #titleOfWebPage=driver.title

        #self.assertFalse(titleOfWebPage == "Google")
        #self.assertIsNotNone(driver)
# -- ------------------------------------------------------------------------------------------

        #list=("python", "selenium", "java")
        #self.assertNotIn("java", list)

# ------------------------------------------------------------------------------------------------

        #self.assertGreater(100,10)
        #self.assertLess(100, 10)
        self.assertGreaterEqual(250, 250)


if __name__ == "__main__":
    unittest.main()





















