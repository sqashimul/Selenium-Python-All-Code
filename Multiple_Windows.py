import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class MultipleWindow():
    def multi_window_handle(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        parrent_handle = driver.current_window_handle
        print(parrent_handle)
        driver.find_element(By.XPATH, "//img[@alt='Flat 10% OFF (upto Rs. 7,500)']").click()
        all_handle = driver.window_handles
        print(all_handle)
        for handle in all_handle:
            if handle != parrent_handle:
                driver.switch_to.window(handle)
                driver.find_element(By.XPATH, "//a[@title='Facebook']").click()
                time.sleep(4)
                driver.close()
                time.sleep(4)
                break
        driver.switch_to.window(parrent_handle)
        driver.find_element(By.XPATH, "//img[@alt='Flat 10% OFF (upto Rs. 7,500)']").click()



mulwindo = MultipleWindow()
mulwindo.multi_window_handle()