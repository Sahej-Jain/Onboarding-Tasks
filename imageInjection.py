from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import time, os
from dotenv import load_dotenv

# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720

load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") 
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") 
URL = os.environ.get("URL") 
options = UiAutomator2Options()

# Initialize the remote Webdriver using BrowserStack remote URL
driver = webdriver.Remote(URL, options=options)
driver.execute_script("browserstack_executor: {\"action\":\"cameraImageInjection\", \"arguments\": { \"imageUrl\" : \"media://3552622899a03bbca625d27885f8b3ba7f12e4e6\" }}")
el1 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button")
el1.click()
time.sleep(10)
el2 = driver.find_element(by=AppiumBy.ID, value="com.bsstag.cameraimage:id/button")
el2.click()
time.sleep(10)
el3 = driver.find_element(by=AppiumBy.ID, value="com.sec.android.app.camera:id/bottom_background")
el3.click()

el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="OK")
el4.click()


# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()