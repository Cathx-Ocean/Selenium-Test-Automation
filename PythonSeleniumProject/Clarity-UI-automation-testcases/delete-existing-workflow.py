""""
Pre-requisite:
Atleast one workflow must be present on the UI to be deleted

"""

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

#delete existing workflow
delete_workflow = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___cpe5h10')]").click()
time.sleep(2)
dialog_content = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-DialogContent')]")
dialog_text = dialog_content.text
if "You can’t restore deleted workflows and all changes will be lost." in dialog_text:
    print("Workflow deletion warning was displayed in the popup")
else:
    print("No deletion warning was displayed to user")
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___1srby3n')]").click()
print("The workflow was deleted")
time.sleep(2)

#logout
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Link ___1u1e4t5')]").click()
time.sleep(3)


