import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class ElementState():
    def enable_disable(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://training.openspan.com/login")
        driver.maximize_window()
        d_state = driver.find_element(By.XPATH,"//input[@id='login_button']").is_enabled()
        print(d_state)

        driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys("abcde")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys("abcde234")
        time.sleep(2)
        d_state1 = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(d_state1)
        time.sleep(3)

dstate = ElementState()
dstate.enable_disable()
