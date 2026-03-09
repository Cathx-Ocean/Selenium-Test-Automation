import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#open url
driver.get('http://10.1.10.93/clarity/')
driver.fullscreen_window()
time.sleep(5)

#login
email = driver.find_element(By.XPATH, "//*[contains(@id, 'input-email')]")
email.send_keys("admin@cathx.com")
password = driver.find_element(By.XPATH, "//*[contains(@id, 'input-password')]")
password.send_keys("admin")
password.submit()
time.sleep(5)

#create workflow and verify that is saved
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___y407490')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[contains(@value, 'One')]").click()
workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'workflow-name')]")
workflow.clear()
workflow.send_keys("test-nav")
time.sleep(2)
workflow.submit()
time.sleep(3)
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Workflow was created and saved")
else:
    print("Workflow was not created or saved")

#live navigation microservice
nav = driver.find_element(By.XPATH, "(//span[@class='flowItem_text'])[2]")
nav.click()
time.sleep(2)
driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])").click()
time.sleep(2)
ip_address = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0'])")
ip_address.clear()
ip_address.send_keys("10.1.10.42")
time.sleep(2)
port_number = driver.find_element(By.ID, "port_number")
port_number.clear()
port_number.send_keys("50001")

save_button = driver.find_element(By.XPATH, "//*[contains(@id, 'primaryActionButton')]").click()
time.sleep(3)

#verify that the workflow was saved
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Workflow was saved after updating navigation details")
else:
    print("Workflow was not saved")

#run workflow
#driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs w--100')]").click()
#time.sleep(2)
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