import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
print(driver.title)
driver.find_element(By.NAME, "login").click()     #send_keys("amthshimul@gmail.com")

wait = WebDriverWait(driver, 10)
driver.find_element(By.XPATH, "//input[@title='Sign in']").click()
alert = wait.until(ec.alert_is_present())
print(alert.text)
alert.accept()
driver.close()