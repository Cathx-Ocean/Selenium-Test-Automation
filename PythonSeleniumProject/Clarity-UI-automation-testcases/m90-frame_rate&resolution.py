import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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

#create workflow and verify that is saved
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___y407490')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[contains(@value, 'Acquire and Save')]").click()
workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'workflow-name')]")
workflow.clear()
workflow.send_keys("test-m90")
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
time.sleep(3)

#m90 settings
m90_image = driver.find_element(By.XPATH, "(//span[@class='flowItem_text'])[1]")
m90_image.click()
time.sleep(2)
driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])[2]").click()
time.sleep(2)

#change frame rate
frame_rate = driver.find_element(By.ID, "acq_frame_rate")
frame_rate.clear()
frame_rate.send_keys("10")
time.sleep(2)

#change resolution
resolution = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Select__select')]")
select = Select(resolution)
select.select_by_value("uhd")
time.sleep(2)

save_button = driver.find_element(By.XPATH, "//*[contains(@id, 'primaryActionButton')]").click()
time.sleep(3)

#verify that the workflow was saved
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Workflow was saved")
else:
    print("Workflow was not saved")

#run workflow
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