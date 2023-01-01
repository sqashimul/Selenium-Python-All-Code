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
email_id = wait.until(ec.presence_of_element_located((By.ID, "username")))
email_id.send_keys("amthshimul@gmail.com")
driver.find_element(By.ID, "password").send_keys("dsds@123")
