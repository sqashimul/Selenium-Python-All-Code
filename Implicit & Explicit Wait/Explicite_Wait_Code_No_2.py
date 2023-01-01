import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.expedia.com/")


driver.find_element(By.XPATH, "//span[normalize-space()='Flights']").click() #flights
driver.find_element(By.XPATH, "//span[normalize-space()='One-way']").click() #oneway

driver.find_element(By.XPATH, "//button[@aria-label='Leaving from']").send_keys("San Francisco (SFO - San Francisco Intl.)") #leaving from
time.sleep(2)
driver.find_element(By.XPATH, "//button[@aria-label='Going to']").send_keys("Sydney (SYD - Kingsford Smith Intl.)") #going to

# driver.find_element(By.ID, "d1-btn").clear()
driver.find_element(By.ID, "d1-btn").send_keys("Sat, Jan 7") #date
driver.find_element(By.XPATH, "//*[@id='wizard-flight-pwa-1']/div[3]/div[2]/button").click()

time.sleep(5)