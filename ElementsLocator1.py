import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class FindElementByIDandName():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.CSS_SELECTOR,"#login-input").send_keys('amthshimul@gmail.com')
        time.sleep(4)

findbyid = FindElementByIDandName()
findbyid.locate_by_id_demo()





















# from webdriver_manager.firefox import GeckoDriverManager
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#driver = webdriver.Chrome(executable_path = "C:\\browserdrivers\\chromedriver.exe")
# driver = webdriver.Firefox(executable_path = "C:\\browserdrivers\\geckodriver.exe")
# driver = webdriver.Edge(executable_path = "C:\\browserdrivers\\msedgedriver.exe")

# driver.get("https://www.daraz.com.bd/")
# driver.maximize_window()
# print(driver.title)
# driver.close()