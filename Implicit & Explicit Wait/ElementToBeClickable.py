import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://app.hubspot.com/login")
print(driver.title)

wait = WebDriverWait(driver, 10)
signup_link = wait.until(ec.element_to_be_clickable((By.XPATH, "//i18n-string[normalize-space()='Sign up']")))
print(signup_link.text)
signup_link.click()

first_name = wait.until(ec.visibility_of_element_located((By.NAME, "FIRST_NAME")))
first_name.send_keys("Shimul")

