import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://app.hubspot.com/login")
print(driver.title)

user_name = driver.find_element(By.ID, "username")
user_name.send_keys("amthshimul@gmail.com")
driver.find_element(By.ID, "password").send_keys("dsds@123")
