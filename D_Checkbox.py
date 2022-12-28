import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class SelectCheckbox():
    def is_selected(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com")
        driver.maximize_window()
        driver.find_element(By.XPATH,"//a[normalize-space()='Non Stop Flights']").click()

        elem = driver.find_element(By.XPATH, "//a[normalize-space()='Non Stop Flights']").is_selected()
        print(elem)
        driver.find_element(By.XPATH, "//a[normalize-space()='Student Fare']").click()
        time.sleep(4)
        elem2 = driver.find_element(By.XPATH, "//a[normalize-space()='Student Fare']").is_displayed()
        print(elem2)


checkboxselct = SelectCheckbox()
checkboxselct.is_selected()