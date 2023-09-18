from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")

try:
    #Wait for the condition inside parenthesis to happen before moving on
    element = WebDriverWait(driver, 10).until(
        #Locates the search bar
        #Google homepage = q
        EC.presence_of_element_located((By.NAME, "q"))
    )
    element.send_keys("discord.com")
    element.send_keys(Keys.ENTER)
finally:
    time.sleep(4)
    driver.quit()