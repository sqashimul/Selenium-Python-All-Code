import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class ScreenShot():
    def captr_screen(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        continuescreenshot = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        continuescreenshot.screenshot(".\\test.png")
        continuescreenshot.click()
        time.sleep(2)
        driver.get_screenshot_as_file("C:\Learn Selenium Python\\eroor.png")
        driver.save_screenshot(".\\test1.png")

css = ScreenShot()
css.captr_screen()