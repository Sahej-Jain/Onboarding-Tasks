# imports:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from percy import percy_snapshot
# from percy import percy_screenshot
# from browserstack_sdk import PercySDK

# initializing the driver:
driver = webdriver.Chrome()
driver.maximize_window()

# opening chrome:
driver.get("https://the-internet.herokuapp.com/")
time.sleep(3)
new_todo_input =driver.find_element(By.LINK_TEXT, "File Upload")
percy_snapshot(driver, 'File upload snapshot')

driver.find_element(By.LINK_TEXT, "File Upload").click()
driver.find_element(By.ID, "file-submit")
percy_snapshot(driver, "file submit")
time.sleep(5)

# go back to home page:
driver.back()
# driver.back()
# time.sleep(5)

# drag and drop:
driver.find_element(By.LINK_TEXT, "Drag and Drop").click()
time.sleep(5)
drg = driver.find_element(By.ID, "column-a")
drp = driver.find_element(By.ID, "column-b")
percy_snapshot(driver, "drag and drop")
time.sleep(5)

driver.quit()