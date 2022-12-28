import time
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://www.worldometers.info/geography/flags-of-the-world/")
driver.maximize_window()

#Scroll Down page by Pixel
# driver.execute_script("window.scrollBy(0, 3000)", "")
# time.sleep(4)

#Scroll down page till the element is visable
# flag = driver.find_element(By.XPATH, "//img[@src='/img/flags/small/tn_nz-flag.gif']")
# driver.execute_script("arguments[0].scrollIntoView();", flag)
# time.sleep(5)

#Scroll dowun page till the end
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
time.sleep(5)