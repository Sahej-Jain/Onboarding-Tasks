import time
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions
from dotenv import load_dotenv

# Configuring the credentials
load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME")
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY")
URL = os.environ.get("URL") or "https://hub.browserstack.com/wd/hub"

# Fixture to initialize the driver
@pytest.fixture(scope="module")
def driver():
    options = ChromeOptions()
    # Add capabilities if necessary, such as BStack options
    driver = webdriver.Remote(
        command_executor=URL,
        options=options
    )
    driver.maximize_window()
    yield driver
    driver.quit()

# Test functions
def test_file_upload(driver):
    driver.get("https://the-internet.herokuapp.com/")
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "File Uplo").click()
    time.sleep(3)
    file_input = driver.find_element(By.ID, "file-upload")
    file_input.send_keys("/Users/sahej/Desktop/Selenium_tests/test.jpg")
    driver.find_element(By.ID, "file-submit").click()
    time.sleep(3)
    assert "File Uploaded!" in driver.page_source

def test_drag_and_drop(driver):
    driver.get("https://the-internet.herokuapp.com/")
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Drag and Drop").click()
    time.sleep(2)
    drg = driver.find_element(By.ID, "column-a")
    drp = driver.find_element(By.ID, "column-b")
    ActionChains(driver).drag_and_drop(drg, drp).perform()
    time.sleep(3)
    assert drg.text == "B"
    assert drp.text == "A"

# Example of setting session status (for BrowserStack integration)
def test_set_session_status(driver):
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Website URL verified successfully"}}'
    )

