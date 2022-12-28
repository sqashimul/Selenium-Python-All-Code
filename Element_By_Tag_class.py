import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class FindElementByIDandName():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        print(driver.title)
        driver.maximize_window()
        # driver.find_element(By.TAG_NAME,"input").send_keys("amthshimul@gmail.com")
        driver.find_element(By.CLASS_NAME,"yt-sme-mobile-input ").send_keys("amthshimul@gmail.com")
        time.sleep(6)

findbyid = FindElementByIDandName()
findbyid.locate_by_id_demo()

