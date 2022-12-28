import time
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://omayo.blogspot.com/")

# check_boxes = driver.find_elements(By.XPATH, "//input[@name='color']")
# for check_box in check_boxes:
#     if check_box.is_selected():
#         pass
#         time.sleep(3)
#     else:
#         check_box.click()
#         time.sleep(3)


radio_options = driver.find_elements(By.XPATH, "//input[@name='gender']")
for radio in radio_options :
    if radio.is_selected():
        pass
        time.sleep(3)
    else:
        radio.click()
        time.sleep(3)
