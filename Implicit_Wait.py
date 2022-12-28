import time
from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class ImplicitWait():
    def implicite_wait(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.get("https://login.salesforce.com/")
        driver.maximize_window()
        driver.find_element(By.ID, "username").send_keys("amthshimul@gmail.com")
        driver.find_element(By.ID, "password").send_keys("shimul123")



implwait = ImplicitWait()
implwait.implicite_wait()