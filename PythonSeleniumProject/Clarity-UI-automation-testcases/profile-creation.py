import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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
workflow.send_keys("test-profile-auto100")
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
frame_rate.send_keys("15")
time.sleep(2)

#change resolution
resolution = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Select__select')]")
select = Select(resolution)
select.select_by_value("hd")
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


#save as
time.sleep(5)
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-MenuButton__menuIcon')]").click()
time.sleep(3)
save_as = driver.find_element(By.XPATH, "(//span[@class='fui-MenuItem__content r1ls86vo'])")
save_as.click()
time.sleep(2)

"""""
save_copy = driver.find_element(By.XPATH, "//*[contains(@id, 'dialog-title')]")
save_text = save_copy.text
expected_text = "Save a copy"
if saved_text == expected_text:
    print("Save a copy dialog box was displayed")
else:
    print("Save a copy dialog box was not displayed")
"""

time.sleep(3)
profile_name = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0'])")
#profile_name.clear()
profile_name.send_keys("workflow-profile")
time.sleep(2)
save_button = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___1srby3n')]")
save_button.click()
time.sleep(2)

#verify that the profile was saved
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Profile was created")
else:
    print("Profile was not created")
driver.save_screenshot("C:\\Users\SaikrishnaPalvalliMa\\OneDrive - Cathx Ocean Limited\\Pictures\\selenium\\profile.png")
