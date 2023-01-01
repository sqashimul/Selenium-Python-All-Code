from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("http://omayo.blogspot.com/")

driver.find_element(By.CLASS_NAME, "dropbtn").click()
wait = WebDriverWait(driver, 15)
facebook_option = wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Facebook")))
facebook_option.click()
