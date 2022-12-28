import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class FindElementByIDandName():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        lista = driver.find_elements(By.TAG_NAME,"a")
        print(len(lista))
        for i in lista:
            print(i.text)
        # listb = driver.find_elements(By.TAG_NAME,'input')
        # print(len(listb))

        time.sleep(6)

findbyid = FindElementByIDandName()
findbyid.locate_by_id_demo()

