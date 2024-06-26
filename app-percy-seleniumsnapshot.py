# imports:
from appium import webdriver
from percy import percy_screenshot
from dotenv import load_dotenv
import os
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# credentials:
load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") 
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") 

username = BROWSERSTACK_USERNAME
access_key = BROWSERSTACK_ACCESS_KEY
options = UiAutomator2Options().load_capabilities({
    "platformName" : "android",
    "platformVersion" : "9.0",
    "deviceName" : "Google Pixel 3",
    "app" : "your app url",
    'bstack:options' : {
        "projectName" : "App Automate project",
        "buildName" : "browserstack-build-2",
        "sessionName" : "BStack first_test",
        "userName" : BROWSERSTACK_USERNAME,
        "accessKey" : BROWSERSTACK_ACCESS_KEY,
        "enableCameraImageInjection":"true",
        "resignApp": "true"
    }
})

driver = webdriver.Remote(f"https://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub", options=options)
percy_screenshot(driver, 'Homepage') # take a screenshot

driver.quit()