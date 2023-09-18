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

site = 'https://discord.com/login'

driver = webdriver.Chrome() # specify the path if needed
driver.get(site)

# Wait until the specific element is present
try:
    time.sleep(2)
    # Assuming you want to input the email
    email_elem = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    email_elem.send_keys("dillonmaltese@gmail.com")

    # Assuming you want to input the password next (replace 'your_password' with the actual password or another placeholder)
    password_elem = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_elem.send_keys("Baseballrocks1!")

    button_elem = driver.find_element(By.NAME, "Log In")

    button_elem.click()
    
except Exception as e:
    print("An error occurred:", str(e))

finally:
    time.sleep(10)
    driver.quit()
