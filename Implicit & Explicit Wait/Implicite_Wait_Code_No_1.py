from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.facebook.com/")
print(driver.title)

driver.implicitly_wait(10)

assert "Facebook – log in or sign up" in driver.title

driver.find_element(By.NAME, "email").send_keys("zarta@gmail.com")
driver.find_element(By.NAME, "pass").send_keys("gdg23da12")

driver.find_element(By.NAME, "login").click()