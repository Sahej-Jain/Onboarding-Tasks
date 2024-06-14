# imports:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.common.action_chains import ActionChains

# initializing the driver:
driver = webdriver.Chrome()
driver.maximize_window()

# opening chrome:
driver.get("https://the-internet.herokuapp.com/")

# uploading file:
driver.find_element(By.LINK_TEXT, "File Upload").click()
file_input = driver.find_element(By.ID, "file-upload")
upload_file = os.path.join(os.path.dirname(__file__),"test.jpg")
file_input.send_keys(upload_file)
driver.find_element(By.ID, "file-submit").click()
time.sleep(5)

# go back to home page:
driver.back()
driver.back()
time.sleep(5)

# drag and drop:
driver.find_element(By.LINK_TEXT, "Drag and Drop").click()
time.sleep(5)
drg = driver.find_element(By.ID, "column-a")
drp = driver.find_element(By.ID, "column-b")
ActionChains(driver).drag_and_drop(drg, drp).perform()
time.sleep(5)

# closing the driver:
driver.quit()
