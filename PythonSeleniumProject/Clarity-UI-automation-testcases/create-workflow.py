import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#open url
driver.get('http://10.1.10.108/clarity/')
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
driver.find_element(By.XPATH, "//*[contains(@value, 'High Frame Rate')]").click()
workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'workflow-name')]")
workflow.clear()
workflow.send_keys("test-workflow2")
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

#logout
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Link ___1u1e4t5')]").click()
time.sleep(3)


