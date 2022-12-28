import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class GetElementByText():
    def locate_by_text(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com")
        driver.maximize_window()

        text1 = driver.find_element(By.LINK_TEXT,"Yatra for Business").text
        print(text1)
        time.sleep(3)

getbytext = GetElementByText()
getbytext.locate_by_text()
