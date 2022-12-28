import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class RightClickDobleClick():
    def right_doble_click(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        # Right_Click
        achains = ActionChains(driver)
        elem1 = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        copyelem = driver.find_element(By.XPATH, "//span[normalize-space()='Copy']")
        achains.context_click(elem1).perform()
        time.sleep(4)
        copyelem.click()
        time.sleep(3)

        # Double_Click
        # achains = ActionChains(driver)
        # elem2 = driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")
        # achains.context_click(elem2).perform()
        # time.sleep(3)

rdclick =RightClickDobleClick()
rdclick.right_doble_click()