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

    driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/button[2]').click()
    time.sleep(7)
    driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div[1]/nav/div[2]/ul/li[3]/div/a').click()
    
except Exception as e:
    print("An error occurred:", str(e))

finally:
    time.sleep(50)
    driver.quit()
