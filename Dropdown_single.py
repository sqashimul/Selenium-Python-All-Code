import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class DDSingleSelect():
    def dropdowslt(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        driver.maximize_window()
        dropdwon = driver.find_element(By.NAME, "UserTitle")
        dd = Select(dropdwon)

        dd.select_by_index(1)
        time.sleep(3)

        dd.select_by_visible_text("Marketing / PR Manager")
        time.sleep(3)

        dd.select_by_value("CxO_General_Manager_AP")
        time.sleep(3)

dropdownselct = DDSingleSelect()
dropdownselct.dropdowslt()