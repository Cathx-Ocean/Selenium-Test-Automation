""""
Pre-requisite:
Atleast one workflow must be present on the UI

"""


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

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

#run workflow
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs w--100')]").click()
time.sleep(5)
run_workflow = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___19y96bh')]").click()
time.sleep(3)
run_dialog_content = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-DialogContent r1v5zwsm')]")
dialog_text = run_dialog_content.text
if "Safe mode is currently enabled. Are you sure you want to run this workflow in Safe Mode?" in dialog_text:
    print("Safemode warning was displayed while attempting to run workflow")
else:
    print("Safemode warning was not displayed while attempting to run workflow")

continue_workflow = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___1srby3n')]").click()
time.sleep(5)
run_content = driver.find_element(By.XPATH, "//*[contains(@class, 'd--flex ai--center jc--flex-start w--100')]")
run_text = run_content.text
if "Running Workflow" in run_text:
    print("Workflow is running....")
else:
    print("No workflow was running")

#status check
run_status = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Badge r1l7mb74')]")
status_text = run_status.text
if "Engine Running" in status_text:
    print("Engine status is: running")
else:
    print("Engine status is not running")

#pause workflow
driver.find_element(By.XPATH, "//*[contains(@class, 'd--flex ai--center jc--flex-start w--100')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___1tn2wcx')]").click()
time.sleep(3)
pause_content = driver.find_element(By.XPATH, "//*[contains(@class, 'd--flex ai--center jc--flex-start w--100')]")
pause_text = pause_content.text
if "Workflow Paused" in pause_text:
    print("Workflow is paused")
else:
    print("No workflow was paused")

#status check
pause_status = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Badge r1l7mb74')]")
status_text = pause_status.text
if "Workflow Paused" in status_text:
    print("Engine status is: paused")
else:
    print("Engine status is not paused")

#resume workflow
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___1tn2wcx')]").click()
time.sleep(3)
if "Running Workflow" in run_text:
    print("Workflow is resumed")
else:
    print("No workflow was resumed")

#status check
run_status = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Badge r1l7mb74')]")
status_text = run_status.text
if "Engine Running" in status_text:
    print("Engine status is: running")
else:
    print("Engine status is not running")

#terminate workflow
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___qlotnu0')]").click()
time.sleep(3)
terminate_dialog_content = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-DialogContent r1v5zwsm')]")
terminate_dialog_text = terminate_dialog_content.text
if "You can’t resume terminated workflows and all processed data will be lost." in terminate_dialog_text:
    print("Workflow termination warning was displayed")
else:
    print("No warning was displayed during workflow termination")
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___10fb9qa')]").click()
time.sleep(2)
pause_content = driver.find_element(By.XPATH, "//*[contains(@class, 'd--flex ai--center jc--flex-start w--100')]")
pause_text = pause_content.text
if "Workflow Terminated" in pause_text:
    print("Workflow is Terminated")
else:
    print("No workflow was terminated")

#status check
run_status = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Badge r1l7mb74')]")
status_text = run_status.text
if "Engine Loaded" in status_text:
    print("Engine status is: loaded")
else:
    print("Engine status is not loaded")

