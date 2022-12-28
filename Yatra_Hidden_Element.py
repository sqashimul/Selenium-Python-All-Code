import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class YatratHidden():
    def yatra_is_display(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/hotels")
        driver.find_element(By.XPATH, "//label[normalize-space()='Traveller and Hotel']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()
        time.sleep(2)
        elem = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        print(elem)
        # driver.find_element(By.XPATH, "//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[]").click
        # elem1 = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        # print(elem1)

YatraDisplayed = YatratHidden()
YatraDisplayed.yatra_is_display()