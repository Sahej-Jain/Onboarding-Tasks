# import the modules:
from dotenv import load_dotenv
import os,time, requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

# configuring the credentials:
load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") 
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") 
options = ChromeOptions()
options.set_capability('sessionName', 'BStack Sample Test')
driver = webdriver.Chrome(options=options)
session_id=driver.session_id

# executing the code:
try:
    driver.get('https://bstackdemo.com/')
except Exception as err:
    try:
        # after the network is up:
        url = f"https://api.browserstack.com/automate/sessions/{session_id}/update_network.json"
        data = {
            "networkProfile": "4g-lte-good"
        }
        username = BROWSERSTACK_USERNAME or "sahej_HLQNRT"
        access_key =BROWSERSTACK_ACCESS_KEY or  "d94xB3WXqNxqLq1nZvy6"
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.put(url, json=data, auth=(username, access_key), headers=headers)
        time.sleep(10)
        driver.get('https://bstackdemo.com/')
        time.sleep(5)
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Website URL Successfully Verified!"}}')
    except:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Failed"}}')
driver.quit()