import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import logging

driver = webdriver.Chrome()

#open url
driver.get('http://10.1.10.123/clarity/')
driver.fullscreen_window()
time.sleep(5)

#login
email = driver.find_element(By.XPATH, "//*[contains(@id, 'input-email')]")
email.send_keys("admin@cathxocean.com")
password = driver.find_element(By.XPATH, "//*[contains(@id, 'input-password')]")
password.send_keys("admin")
password.submit()
time.sleep(5)

"""""
#export workflow
#time.sleep(5)
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-MenuButton__menuIcon')]").click()
time.sleep(3)
export = driver.find_element(By.XPATH, "(//span[@class='fui-MenuItem__content r1ls86vo'])[2]")
export.click()
time.sleep(2)

"""
# run workflow
run_workflow = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___19y96bh')]").click()
time.sleep(3)

continue_workflow = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___1srby3n')]").click()
time.sleep(5)
run_content = driver.find_element(By.XPATH, "//*[contains(@class, 'd--flex ai--center jc--flex-start w--100')]")
run_text = run_content.text
if "Running Workflow" in run_text:
    print("Workflow is running....")
else:
    print("No workflow was running")
time.sleep(10)

# terminate workflow
driver.find_element(By.XPATH, "//*[contains(@class, 'd--flex ai--center jc--flex-start w--100')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___qlotnu0')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___10fb9qa')]").click()
time.sleep(2)
terminate_content = driver.find_element(By.XPATH, "//*[contains(@class, 'd--flex ai--center jc--flex-start w--100')]")
terminate_text = terminate_content.text
if "Workflow Terminated" in terminate_text:
    print("Workflow is Terminated")
else:
    print("No workflow was terminated")

driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs p--absolute')]").click()

