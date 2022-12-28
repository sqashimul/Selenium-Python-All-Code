import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class JavaScriptExecute():
    def java_script_exec(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        # driver.get("https://www.yatra.com/")

        driver.execute_script("window.open('https://www.yatra.com/', '_self');")
        driver.maximize_window()
        time.sleep(8)
        element1 = driver.execute_script("return document.getElementsByTagName('p')[1];")
        driver.execute_script("arguments[0].click();", element1)



exejs = JavaScriptExecute()
exejs.java_script_exec()
