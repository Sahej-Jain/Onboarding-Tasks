from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time, os
from dotenv import load_dotenv

load_dotenv()
URL = os.environ.get("URL") 
options = UiAutomator2Options()

# Initialize the remote Webdriver using BrowserStack remote URL
# and options defined above
driver = webdriver.Remote(URL, options=options)

try:
  time.sleep(3)
  el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="filter-btn")
  el1.click()
  time.sleep(3)
  el2 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Samsung\")")
  el2.click()
  time.sleep(3)
  driver.press_keycode(4);
  time.sleep(3)
  el3 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Add to cart\")")
  el3.click()
  time.sleep(3)
  el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(23)")
  el4.click()
  time.sleep(3)
  el5 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"CHECKOUT\")")
  el5.click()
  driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Added to Cart"}}')
  driver.quit()
except:
  driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Error"}}')
