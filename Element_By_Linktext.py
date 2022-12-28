import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class FindElementByIDandName():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        # driver.find_element(By.LINK_TEXT,"Yatra for Business").click()
        driver.find_element(By.PARTIAL_LINK_TEXT,"Yatra for Busine").click()
        time.sleep(6)

findbyid = FindElementByIDandName()
findbyid.locate_by_id_demo()

