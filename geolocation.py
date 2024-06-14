# import the packages
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# configuring the credentials:
load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") 
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") 
URL = os.environ.get("URL")

bstack_options = {
    "os" : "Windows",
    "osVersion" : "10",
    "buildName" : "browserstack assignment 1",
    "sessionName" : "BStack single python test",
    "userName": BROWSERSTACK_USERNAME,
    "accessKey": BROWSERSTACK_ACCESS_KEY
}
bstack_options["source"] = "python:sample-main:v1.0"
options = ChromeOptions()
options.set_capability('bstack:options', bstack_options)
driver = webdriver.Remote(
    command_executor=URL,
    options=options)

# executing the test:
try:
  # initializing the driver:
  driver.maximize_window()
  driver.get("https://bstackdemo.com/")
  time.sleep(3)

  # setting the initial location:
  driver.execute_script('window.navigator.geolocation.getCurrentPosition = function(success){ var position = { "coords":{"latitude":"37.090240","longitude":"-95.712891"}}; success(position);}')

  # Signing in:
  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'signin')))
  driver.find_element(By.ID, "signin").click()

  #Entering the username
  WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#username input')))
  username = driver.find_element(By.CSS_SELECTOR, "#username input")
  username.send_keys("fav_user\n")

  #Entering the password
  WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password input')))
  password = driver.find_element(By.CSS_SELECTOR, "#password input")
  password.send_keys("testingisfun99\n")

  #Clicking on Login
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'login-btn')))
  driver.find_element(By.ID, "login-btn").click()

  #Click on Offers
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'offers')))
  driver.find_element(By.ID, "offers").click()
  time.sleep(3)

  # verify the offers:
  offers = driver.find_element(By.ID, "iphone")
  time.sleep(5)
  if offers.is_displayed:
    print("offers verified")
    driver.execute_script(
      'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Website offers verified successfully"}}')
  else:
    driver.execute_script(
      'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Website offers not verified successfully"}}')
    print("Offers not verified")

  time.sleep(2)
  driver.quit()

except Exception as err: 
  print("The error occurred because of ", err)
