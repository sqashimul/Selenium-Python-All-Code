import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.redbus.in/")

driver.find_element(By.XPATH, "//i[@id='i-icon-profile']").click()
driver.find_element(By.XPATH, "//li[text()='Sign In/Sign Up']").click()

driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='modalIframe']"))
driver.find_element(By.XPATH, "//div[@class='facebook-text']").click()
time.sleep(4)