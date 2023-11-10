import os
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Set the path to the ChromeDriver executable in the PATH environment variable
chrome_driver_path = "/Users/dillonmaltese/Documents/GitHub/Selenium/chromedriver_mac64"
os.environ["PATH"] += os.pathsep + os.path.dirname(chrome_driver_path)

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the Discord website
driver.get("https://kingschoolct.myschoolapp.com/app/student#studentmyday/assignment-center")

# Wait for a few seconds (you can adjust the duration as needed)
time.sleep(5)

try:
    # Find the text box element by its ID attribute (replace 'label-Username' with the actual ID value)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Username")))
    
    # Input text into the text box
    element.send_keys("dillon.maltese@students.kingschoolct.org")

    time.sleep(2)

    # Find and click the "Login" button (replace 'login_button_id' with the actual ID value)
    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nextBtn")))
    login_button.click()

    time.sleep(5)

    button = driver.find_element(By.CSS_SELECTOR, 'button[aria-labelledby="googleButtonLabel"]')
    button.click()

    time.sleep(5)
#googleButtonLabel

    # After clicking the button, you can simulate pressing the Enter key on the keyboard
    pyautogui.typewrite("dillon.maltese@students.kingschoolct.org")
    pyautogui.typewrite("\n")
    time.sleep(2)
    pyautogui.typewrite("Baseballrocks1!")
    pyautogui.typewrite("\n")
    
    # Wait for a few seconds to see the result
    time.sleep(900)

    #table = driver.find_element(By.XPATH, "//table[@class='fc-content-skeleton']")

    # Find all the rows (tr elements) within the table
    #rows = table.find_elements_by_tag_name("tr")

    # Get the length of the table (number of rows)
    #table_length = len(rows)

    # Print the length of the table
#     print("Table length:", table_length)
except Exception as e:
    print(f"An error occurred: {e}")

# Close the WebDriver when done
driver.quit()
