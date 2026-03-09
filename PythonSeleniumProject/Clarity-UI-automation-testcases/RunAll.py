import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pyautogui
import logging

driver = webdriver.Chrome()

#open url
driver.get('http://10.1.10.115/clarity/')
driver.fullscreen_window()
time.sleep(5)


logging.basicConfig(filename='m90-14-RunAll.log',  # File name to write logs to
                    level=logging.INFO,# Logging level
                    format='%(asctime)s - %(levelname)s - %(message)s')


#login
email = driver.find_element(By.XPATH, "//*[contains(@id, 'input-email')]")
email.send_keys("admin@cathxocean.com")
password = driver.find_element(By.XPATH, "//*[contains(@id, 'input-password')]")
password.send_keys("admin")
password.submit()
time.sleep(5)

#toggle dark mode / light mode
try:
    driver.find_element(By.XPATH, "(//input[@type='checkbox'])").click()
    time.sleep(3)
    print("UI changed to light mode")
    driver.find_element(By.XPATH, "(//input[@type='checkbox'])").click()
    time.sleep(3)
    print("UI changed to dark mode")
    logging.info(f'User was able to toggle between light and dark mode')
except Exception as e:
    logging.error(f'Problem occurred while toggling between light mode and dark mode - {e}')


#create workflows and verify that is saved
#Add Acquire and Save workflow
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___y407490')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[contains(@value, 'Acquire and Save')]").click()
workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'workflow-name')]")
workflow.clear()
workflow.send_keys("Acquire and Save")
time.sleep(2)
workflow.submit()
time.sleep(3)
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Acquire and Save Workflow was added to list")
    logging.info(f'Acquire and Save Workflow was added to list and saved')
else:
    print("Acquire and Save Workflow was not added")
    logging.error(f'Problem occurred while adding Acquire and Save workflow and could not be added to the list')

#m90 settings
m90_image = driver.find_element(By.XPATH, "//*[starts-with(@class, 'p--relative ___')][1]")
m90_image.click()

time.sleep(2)
driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])[2]").click()
time.sleep(2)

#change frame rate
frame_rate = driver.find_element(By.ID, "acq_frame_rate")
frame_rate.clear()
time.sleep(2)
frame_rate.send_keys("24")
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
    print("Workflow was saved with updated frame rate and resolution")
    logging.info(f'Resolution set to HD\n'
                 f'Frame rate set to 24')
else:
    print("Workflow was not saved with updated frame rate and resolution")
    logging.error(f'Frame rate and Resolution could not be saved')

#change image format
save_image = driver.find_element(By.XPATH, "//*[contains(@class, 'p--relative')][3]")
save_image.click()
time.sleep(2)
driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])[2]").click()
time.sleep(2)

image_format = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Select__select')]")
select = Select(image_format)
select.select_by_value("png")
time.sleep(2)

#save as
time.sleep(5)
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-MenuButton__menuIcon')]").click()
time.sleep(3)
save_as = driver.find_element(By.XPATH, "(//span[@class='fui-MenuItem__content r1ls86vo'])")
save_as.click()
time.sleep(3)
profile_name = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0'])")
#profile_name.clear()
profile_name.send_keys("save-copy")
time.sleep(2)
save_button = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___1srby3n')]")
save_button.click()
time.sleep(2)

#verify that the profile was saved
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Save Profile was created")
    logging.info(f'Image format changed to PNG\n'
                 f'New profile for Acquire and Save workflow was created')
else:
    print("Save Profile was not created")
    logging.error(f'Profile could not added to the list')

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
    logging.info(f'The workflow is currently running...\n'
                 f'Engine status: Running')
else:
    print("Engine status is not running")
    logging.error(f'The workflow could not be run')

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
    logging.info(f'The workflow is currently paused\n'
                 f'Engine status: Paused')
else:
    print("Engine status is not paused")
    logging.error(f'The workflow could not be paused')

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
    logging.info(f'The workflow is resumed\n'
                 f'Engine status: Running')
else:
    print("Engine status is not running")
    logging.error(f'The workflow could not be resumed')

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
    logging.info(f'The workflow is canceled/terminated\n'
                 f'Engine status: Loaded')
else:
    print("Engine status is not loaded")
    logging.error(f'The workflow could not be terminated')


#Add Distortion Corrected workflow
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___y407490')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[contains(@value, 'Distortion Corrected')]").click()
workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'workflow-name')]")
workflow.clear()
workflow.send_keys("Distortion Corrected")
time.sleep(2)
workflow.submit()
time.sleep(3)
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Distortion Corrected Workflow was added to list")
    logging.info(f'Distortion Corrected workflow was created and added to the list')
else:
    print("Distortion Corrected Workflow was not added")
    logging.error(f'Problem occurred while adding Distortion Corrected and could not be added to the list')

#Add Illumination Balanced workflow
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___y407490')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[contains(@value, 'Illumination Balanced')]").click()
workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'workflow-name')]")
workflow.clear()
workflow.send_keys("Illumination Balanced")
time.sleep(2)
workflow.submit()
time.sleep(3)
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Illumination Balanced Workflow was added to list")
    logging.info(f'Illumination Balanced workflow was created and added to the list')
else:
    print("Illumination Balanced Workflow was not added")
    logging.error(f'Problem occurred while adding Illumination Balanced and could not be added to the list')

# Add Basic Image Enhancement workflow
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___y407490')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[contains(@value, 'Basic Image Enchancement')]").click()
workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'workflow-name')]")
workflow.clear()
workflow.send_keys("Basic Image Enhancement")
time.sleep(2)
workflow.submit()
time.sleep(3)
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Basic Image Enhancement Workflow was added to list")
    logging.info(f'Basic Image Enhancement was created and added to the list')
else:
    print("Basic Image Enhancement Workflow was not added")
    logging.error(f'Problem occurred while adding Basic Image Enhancement and could not be added to the list')

#Add Advanced Image Enhancement workflow
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___y407490')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[contains(@value, 'Advanced Image Enchancement')]").click()
workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'workflow-name')]")
workflow.clear()
workflow.send_keys("Advanced Image Enhancement")
time.sleep(2)
workflow.submit()
time.sleep(3)
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Advanced Image Enhancement Workflow was added to list")
    logging.info(f'Advanced Image Enhancement was created and added to the list')
else:
    print("Advanced Image Enhancement Workflow was not added")
    logging.error(f'Problem occurred while adding Advanced Image Enhancement and could not be added to the list')

#Add Mask Generation workflow
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___y407490')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[contains(@value, 'Mask Generation')]").click()
workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'workflow-name')]")
workflow.clear()
workflow.send_keys("Mask Generation")
time.sleep(2)
workflow.submit()
time.sleep(3)
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Mask Generation Workflow was added to list")
    logging.info(f'Mask Generation was created and added to the list')
else:
    print("Mask Generation Workflow was not added")
    logging.error(f'Problem occurred while adding Mask Generation and could not be added to the list')

"""""
#export workflow
time.sleep(5)
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-MenuButton__menuIcon')]").click()
time.sleep(3)
export = driver.find_element(By.XPATH, "(//span[@class='fui-MenuItem__content r1ls86vo'])")
export.click()
time.sleep(2)

"""

#import workflow
file_input = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___1uti6m1')]")
file_input.click()
time.sleep(3)

filepath = "C:\\Users\\SaikrishnaPalvalliMa\\Downloads\\New Workflow.zip"
try:
    pyautogui.write(filepath)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)
    print("A workflow was imported to Clarity")
    logging.info(f'A workflow was imported to Clarity UI from {filepath}')
except Exception as e:
    logging.error(f'Problem occurred while importing workflow - {e}')
#pyautogui.hotkey('alt', 'tab')
driver.fullscreen_window()
time.sleep(5)


#delete an existing workflow
delete_workflow = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___cpe5h10')]").click()
time.sleep(2)
dialog_content = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-DialogContent')]")
dialog_text = dialog_content.text
if "You can’t restore deleted workflows and all changes will be lost." in dialog_text:
    print("Workflow deletion warning was displayed in the popup")
else:
    print("No deletion warning was displayed to user")
try:
    driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___1srby3n')]").click()
    print("A workflow was deleted from the list")
    time.sleep(2)
except Exception as e:
    logging.error(f'Problem occurred while deleting workflow - {e}')