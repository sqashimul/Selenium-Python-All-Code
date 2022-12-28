import time
from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class AutoSuggetionAndDate():
    def auto_sugg_drop_date_handle(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys("New Delhi")
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(4)
        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
        time.sleep(4)
        search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div")
        print(len(search_results))
        for results in search_results:
            print(results.text)
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(4)
                break

        date1 = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        date1.click()
        time.sleep(4)
        # driver.find_element(By.XPATH, "//td[@id='04/02/2023']").click()
        # time.sleep(4)

        all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD ']")
        for date in all_dates:
            if date.get_attribute("data-date") == "03/03/2023":
                date.click()
                time.sleep(4)
                break

autosuggetiondatehandle = AutoSuggetionAndDate()
autosuggetiondatehandle.auto_sugg_drop_date_handle()