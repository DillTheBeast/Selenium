# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# site = 'https://discord.com/'

# driver = webdriver.Chrome()
# driver.get(site)
# time.sleep(3)

# # Locate element by visible text
# toBrowser = driver.find_element(by=webdriver.common.by.By.XPATH, value="//*[text()='Open Discord in your browser']")
# time.sleep(5)
# elem = driver.find_element(by=webdriver.common.by.By.XPATH, value="//*[text()='Login']")
# elem.send_keys("Brazil")
# elem.send_keys(Keys.ENTER)
# time.sleep(10)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

site = 'https://discord.com/'

driver = webdriver.Chrome() # specify the path if needed
driver.get(site)

# Wait until the specific element is present
try:
    toBrowser = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[text()='Open Discord in your browser']"))
    )
    toBrowser.click() # If you want to click the button

    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[text()='Login']"))
    )
    elem.click() # If you want to click the button
    
except:
    print("Couldn't locate the element")

finally:
    time.sleep(10)
    driver.quit()
