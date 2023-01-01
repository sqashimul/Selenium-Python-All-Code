import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.yatra.com/")
driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']").send_keys("DEL")
driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']").send_keys("BOM")
driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']").send_keys("12/01/2023")
driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_date']").send_keys("16/01/2023")
time.sleep(15)
driver.find_element(By.XPATH, "//input[@id='BE_flight_flsearch_btn']").click()

time.sleep(4)

