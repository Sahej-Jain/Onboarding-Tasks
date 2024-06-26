from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os
from dotenv import load_dotenv

load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") 
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") 
URL = os.environ.get("URL") 
options = UiAutomator2Options()

# Initialize the remote Webdriver using BrowserStack remote URL
# and options defined above
driver = webdriver.Remote(URL, options=options)

# Test case for the BrowserStack sample Android app.
# If you have uploaded your app, update the test case here.
time.sleep(3)
driver.orientation = "landscape"
time.sleep(3)
# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()