import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class ElementHidden():
    def hidden_is_display(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")

        elem = driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print(elem)
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
        elem1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(elem1)

elemDisplayed = ElementHidden()
elemDisplayed.hidden_is_display()