# from selenium import webdriver
# import time
# from selenium.webdriver.common.keys import Keys
# print("sample test case started")
# driver = webdriver.Chrome()

# #maximize the window size
# driver.maximize_window()
# #navigate to the url
# driver.get("https://www.google.com/")
# #identify the Google search text box and enter the value
# time.sleep(3)
# driver.find_element_by_name("q").send_keys("javatpoint")
# time.sleep(3)
# #click on the Google search button
# driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
# time.sleep(3)
# #close the browser
# print("sample test case successfully completed")
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
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    element.send_keys("javatpoint")
    element.send_keys(Keys.ENTER)
finally:
    time.sleep(4)
    driver.quit()