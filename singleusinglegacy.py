# imports:
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# configuring the credentials:
load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME")
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") 
URL = os.environ.get("URL") or "https://hub.browserstack.com/wd/hub"

bstack_options = {
    "os" : "Windows",
    "osVersion" : "10",
    "buildName" : "browserstack assignment 1",
    "sessionName" : "BStack single python test",
    "userName": BROWSERSTACK_USERNAME,
    "accessKey": BROWSERSTACK_ACCESS_KEY
}
bstack_options["source"] = "python:sample-main:v1.0"
options = FirefoxOptions()
options.set_capability('bstack:options', bstack_options)
driver = webdriver.Remote(
    command_executor=URL,
    options=options)

# initializing the driver:
driver.maximize_window()

# opening chrome:
driver.get("https://the-internet.herokuapp.com/")

# uploading file:
driver.find_element(By.LINK_TEXT, "File Upload").click()
file_input = driver.find_element(By.ID, "file-upload")
upload_file = os.path.join(os.path.dirname(__file__),"test.jpg")
file_input.send_keys(upload_file)
driver.find_element(By.ID, "file-submit").click()

# go back to home page:
driver.back()
driver.back()
time.sleep(5)

# drag and drop:
driver.find_element(By.LINK_TEXT, "Drag and Drop").click()
drg = driver.find_element(By.ID, "column-a")
drp = driver.find_element(By.ID, "column-b")
ActionChains(driver).drag_and_drop(drg, drp).perform()
time.sleep(5)

driver.execute_script(
      'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Website URL verified successfully"}}')

# closing the driver:
driver.quit()