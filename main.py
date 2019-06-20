from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
user = "xatm092"
pwd = ""
driver = webdriver.Firefox()
browser = driver.get("https://www.etoro.com/login")
assert "eToro" in driver.title
elem = None
try:
    elem = driver.find_element_by_class_name("i-menu-user-username")
except: pass
if (elem!=None) and (elem.text==user): print("logged in")
else:
#assert "Facebook" in driver.title
    print("Logging in...")
    elem = driver.find_element_by_id("username")
    elem.send_keys(user)
    elem = driver.find_element_by_id("password")
    elem.send_keys(pwd)
    elem.send_keys(Keys.RETURN)
    try:
        wait_ele = EC.presence_of_element_located((By.CLASS_NAME, 'i-menu-user-username'))
        WebDriverWait( browser, 5 ).until(wait_ele)
        elem = driver.find_element_by_class_name("i-menu-user-username")
    except TimeoutException: print("Loading took too much time!")
    except: pass
    if (elem!=None) and (elem.text==user): print("logged in")
    else: print("wtf?")
    driver.close()