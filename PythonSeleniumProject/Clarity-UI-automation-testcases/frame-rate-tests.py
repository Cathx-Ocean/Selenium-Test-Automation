import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import logging
import os

folder_path_1 = "//10.1.10.123/clarity/images/session_name/hd-test-24/m90/m90_Stills"
folder_path_2 = "//10.1.10.123/clarity/images/session_name/uhd-test-7/m90/m90_Stills"
folder_path_3 = "//10.1.10.123/clarity/images/session_name/full-test-5/m90/m90_Stills"

folder_path_4 = "//10.1.10.123/clarity/images/session_name/png-hd-test-24/m90/m90_Stills"
folder_path_5 = "//10.1.10.123/clarity/images/session_name/png-uhd-test-7/m90/m90_Stills"
folder_path_6 = "//10.1.10.123/clarity/images/session_name/png-full-test-5/m90/m90_Stills"

folder_path_7 = "//10.1.10.123/clarity/images/session_name/bmp-hd-test-24/m90/m90_Stills"
folder_path_8 = "//10.1.10.123/clarity/images/session_name/bmp-uhd-test-7/m90/m90_Stills"
folder_path_9 = "//10.1.10.123/clarity/images/session_name/bmp-full-test-5/m90/m90_Stills"

run_time = 60
sleep_time = run_time - 8

driver = webdriver.Chrome()

#open url
driver.get('http://10.1.10.123/clarity/')
driver.fullscreen_window()
time.sleep(5)

logging.basicConfig(filename='Frame-Rate-Test2.log',  # File name to write logs to
                    level=logging.INFO, # Logging level
                    format='%(asctime)s - %(levelname)s - %(message)s')

#login
email = driver.find_element(By.XPATH, "//*[contains(@id, 'input-email')]")
email.send_keys("admin@cathxocean.com")
password = driver.find_element(By.XPATH, "//*[contains(@id, 'input-password')]")
password.send_keys("admin")
password.submit()
time.sleep(5)

#Add Acquire and Save workflow
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___y407490')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[contains(@value, 'Acquire and Save')]").click()
workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'workflow-name')]")
workflow.send_keys(Keys.CONTROL + "a")
workflow.send_keys(Keys.DELETE)
workflow.send_keys("fps")
time.sleep(2)
workflow.submit()
time.sleep(3)
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Acquire and Save Workflow was added to list")
    logging.info(f'Acquire and Save Workflow was added to list and saved\n'
                 f'"""JPG"""\n')
else:
    print("Acquire and Save Workflow was not added")
    logging.error(f'Problem occurred while adding Acquire and Save workflow and could not be added to the list')

#disable safemode
safemode_off = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ml--XL')]").click()
time.sleep(2)
dialog_on_content = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-ToastBody')]")
time.sleep(2)
dialog_on_text = dialog_on_content.text
if "Safe Mode" in dialog_on_text:
    print("Safemode was turned off")
    logging.info(f'Safe mode turned off')
else:
    print("Safemode was not turned off")
    logging.info(f'Safe mode is not turned off')
#dialog_close = driver.find_element(By.XPATH, "//*[contains(@class, 'p--absolute')]").click()
time.sleep(5)


"""""
Image Format: JPG
No processing
"""

m90_image = driver.find_element(By.XPATH, "//*[starts-with(@class, 'p--relative ___')][1]")
m90_image.click()
time.sleep(2)
driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])[2]").click()
time.sleep(2)

#change frame rate
frame_rate = driver.find_element(By.ID, "acq_frame_rate")
frame_rate.send_keys(Keys.CONTROL + "a")
frame_rate.send_keys(Keys.DELETE)
#frame_rate.clear()
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
    logging.info(f'\nResolution set to HD\n'
                 f'Frame rate set to 24')
else:
    print("Workflow was not saved with updated frame rate and resolution")
    logging.error(f'Frame rate and Resolution could not be saved')


#update sub-session name
save_image = driver.find_element(By.XPATH, "//*[contains(@class, 'p--relative')][3]")
save_image.click()
time.sleep(2)
driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])[1]").click()
time.sleep(2)

sub_session = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0'])[3]")
sub_session.clear()
sub_session.send_keys("hd-test-24")

save_button = driver.find_element(By.XPATH, "//*[contains(@id, 'primaryActionButton')]").click()
time.sleep(3)

#verify that the workflow was saved
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Workflow was saved with updated sub-session name")
    logging.info(f'Sub-session set to hd-test-24')
else:
    print("Workflow was not saved with updated sub-session name")
    logging.error(f'Sub-session name could not be saved')


#run workflow
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
time.sleep(48)

#terminate workflow
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

file_count = 0
for root, dirs, files in os.walk(folder_path_1):
    file_count += len(files)

print(f"Total images: {file_count}")
FPS = file_count/run_time
print(f"Frame rate = {FPS}")
logging.info(f'\nImage format = JPG\n'
             f'Resolution = HD\n'
             f'Total time run = {run_time}s\n'
             f'Total images = {file_count}\n'
             f'Frame rate = {FPS}\n')


# update sub-session name
save_image = driver.find_element(By.XPATH, "//*[contains(@class, 'p--relative')][3]")
save_image.click()
time.sleep(2)
sub_session = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0'])[3]")
sub_session.send_keys(Keys.CONTROL + "a")
sub_session.send_keys(Keys.DELETE)
sub_session.send_keys("uhd-test-7")

save_button = driver.find_element(By.XPATH, "//*[contains(@id, 'primaryActionButton')]").click()
time.sleep(3)

# verify that the workflow was saved
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Workflow was saved with updated sub-session name")
    logging.info(f'Sub-session set to uhd-test-7')
else:
    print("Workflow was not saved with updated sub-session name")
    logging.error(f'Sub-session name could not be saved')

m90_image = driver.find_element(By.XPATH, "//*[starts-with(@class, 'p--relative ___')][1]")
m90_image.click()
time.sleep(2)
driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])[2]").click()
time.sleep(2)

#change frame rate
frame_rate = driver.find_element(By.ID, "acq_frame_rate")
frame_rate.send_keys(Keys.CONTROL + "a")
frame_rate.send_keys(Keys.DELETE)
#frame_rate.clear()
time.sleep(2)
frame_rate.send_keys("7")
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
    print("Workflow was saved with updated frame rate and resolution")
    logging.info(f'\nResolution set to UHD\n'
                 f'Frame rate set to 7')
else:
    print("Workflow was not saved with updated frame rate and resolution")
    logging.error(f'Frame rate and Resolution could not be saved')

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
time.sleep(sleep_time)

# terminate workflow
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

file_count = 0
for root, dirs, files in os.walk(folder_path_2):
    file_count += len(files)

print(f"Total images: {file_count}")
FPS = file_count / run_time
print(f"Frame rate = {FPS}")
logging.info(f'\nImage format = JPG\n'
             f'Resolution = UHD\n'
             f'Total time run = {run_time}s\n'
             f'Total images = {file_count}\n'
             f'Frame rate = {FPS}\n')

#change frame rate
frame_rate = driver.find_element(By.ID, "acq_frame_rate")
frame_rate.send_keys(Keys.CONTROL + "a")
frame_rate.send_keys(Keys.DELETE)
#frame_rate.clear()
time.sleep(2)
frame_rate.send_keys("5")
time.sleep(2)

#change resolution
resolution = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Select__select')]")
select = Select(resolution)
select.select_by_value("full")
time.sleep(2)

save_button = driver.find_element(By.XPATH, "//*[contains(@id, 'primaryActionButton')]").click()
time.sleep(3)

#verify that the workflow was saved
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Workflow was saved with updated frame rate and resolution")
    logging.info(f'\nResolution set to FULL\n'
                 f'Frame rate set to 5')
else:
    print("Workflow was not saved with updated frame rate and resolution")
    logging.error(f'Frame rate and Resolution could not be saved')


#update sub-session name
save_image = driver.find_element(By.XPATH, "//*[contains(@class, 'p--relative')][3]")
save_image.click()
time.sleep(2)
driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])[1]").click()
time.sleep(2)

sub_session = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0'])[3]")
sub_session.send_keys(Keys.CONTROL + "a")
sub_session.send_keys(Keys.DELETE)
sub_session.send_keys("full-test-5")

save_button = driver.find_element(By.XPATH, "//*[contains(@id, 'primaryActionButton')]").click()
time.sleep(3)

#verify that the workflow was saved
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Workflow was saved with updated sub-session name")
    logging.info(f'Sub-session set to full-test-5')
else:
    print("Workflow was not saved with updated sub-session name")
    logging.error(f'Sub-session name could not be saved')


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
time.sleep(sleep_time)

# terminate workflow
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

file_count = 0
for root, dirs, files in os.walk(folder_path_3):
    file_count += len(files)

print(f"Total images: {file_count}")
FPS = file_count / run_time
print(f"Frame rate = {FPS}")
logging.info(f'\nImage format = JPG\n'
             f'Resolution = FULL\n'
             f'Total time run = {run_time}s\n'
             f'Total images = {file_count}\n'
             f'Frame rate = {FPS}\n'
             f'"""PNG"""\n')


"""""
Image Format = PNG
No processing
"""

sub_session = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0'])[3]")
sub_session.send_keys(Keys.CONTROL + "a")
sub_session.send_keys(Keys.DELETE)
sub_session.send_keys("png-full-test-5")

driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])[2]").click()
time.sleep(2)

image_format = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Select__select')]")
select = Select(image_format)
select.select_by_value("png")
time.sleep(2)

save_button = driver.find_element(By.XPATH, "//*[contains(@id, 'primaryActionButton')]").click()
time.sleep(3)

#verify that the workflow was saved
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Workflow was saved with updated image format and sub-session name")
    logging.info(f'\nImage format set to PNG\n'
                 f'Sub-session set to png-full-test-5')
else:
    print("Workflow was not saved with updated image format and sub-session name")
    logging.error(f'Image format and sub-session name could not be saved')

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
time.sleep(sleep_time)

# terminate workflow
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

file_count = 0
for root, dirs, files in os.walk(folder_path_6):
    file_count += len(files)

print(f"Total images: {file_count}")
FPS = file_count / run_time
print(f"Frame rate = {FPS}")
logging.info(f'\nImage format = PNG\n'
             f'Resolution = FULL\n'
             f'Total time run = {run_time}s\n'
             f'Total images = {file_count}\n'
             f'Frame rate = {FPS}\n')


sub_session = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0'])[3]")
sub_session.send_keys(Keys.CONTROL + "a")
sub_session.send_keys(Keys.DELETE)
sub_session.send_keys("png-uhd-test-7")

save_button = driver.find_element(By.XPATH, "//*[contains(@id, 'primaryActionButton')]").click()
time.sleep(3)

#verify that the workflow was saved
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Workflow was saved with updated sub-session name")
    logging.info(f'Sub-session set to png-uhd-test-5')
else:
    print("Workflow was not saved with updated sub-session name")
    logging.error(f'Sub-session name could not be saved')

m90_image = driver.find_element(By.XPATH, "//*[starts-with(@class, 'p--relative ___')][1]")
m90_image.click()
time.sleep(2)
driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])[2]").click()
time.sleep(2)

#change frame rate
frame_rate = driver.find_element(By.ID, "acq_frame_rate")
frame_rate.send_keys(Keys.CONTROL + "a")
frame_rate.send_keys(Keys.DELETE)
#frame_rate.clear()
time.sleep(2)
frame_rate.send_keys("7")
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
    print("Workflow was saved with updated frame rate and resolution")
    logging.info(f'\nResolution set to UHD\n'
                 f'Frame rate set to 7')
else:
    print("Workflow was not saved with updated frame rate and resolution")
    logging.error(f'Frame rate and Resolution could not be saved')

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
time.sleep(sleep_time)

# terminate workflow
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

file_count = 0
for root, dirs, files in os.walk(folder_path_5):
    file_count += len(files)

print(f"Total images: {file_count}")
FPS = file_count / run_time
print(f"Frame rate = {FPS}")
logging.info(f'\nImage format = PNG\n'
             f'Resolution = UHD\n'
             f'Total time run = {run_time}s\n'
             f'Total images = {file_count}\n'
             f'Frame rate = {FPS}\n')

#change frame rate
frame_rate = driver.find_element(By.ID, "acq_frame_rate")
frame_rate.send_keys(Keys.CONTROL + "a")
frame_rate.send_keys(Keys.DELETE)
#frame_rate.clear()
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
    logging.info(f'\nResolution set to HD\n'
                 f'Frame rate set to 24')
else:
    print("Workflow was not saved with updated frame rate and resolution")
    logging.error(f'Frame rate and Resolution could not be saved')

save_image = driver.find_element(By.XPATH, "//*[contains(@class, 'p--relative')][3]")
save_image.click()
time.sleep(2)
driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])[1]").click()
time.sleep(2)

sub_session = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0'])[3]")
sub_session.send_keys(Keys.CONTROL + "a")
sub_session.send_keys(Keys.DELETE)
sub_session.send_keys("png-hd-test-24")

save_button = driver.find_element(By.XPATH, "//*[contains(@id, 'primaryActionButton')]").click()
time.sleep(3)

#verify that the workflow was saved
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Workflow was saved with updated sub-session name")
    logging.info(f'Sub-session set to png-hd-test-24')
else:
    print("Workflow was not saved with updated sub-session name")
    logging.error(f'Sub-session name could not be saved')


#run workflow
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
time.sleep(sleep_time)

#terminate workflow
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


for root, dirs, files in os.walk(folder_path_4):
    file_count += len(files)

print(f"Total images: {file_count}")
FPS = file_count/run_time
print(f"Frame rate = {FPS}")
logging.info(f'\nImage format = PNG\n'
             f'Resolution = HD\n'
             f'Total time run = {run_time}s\n'
             f'Total images = {file_count}\n'
             f'Frame rate = {FPS}\n'
             f'"""BMP"""\n')

""""
Image Format: BMP
No Processing
"""

sub_session = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0'])[3]")
sub_session.send_keys(Keys.CONTROL + "a")
sub_session.send_keys(Keys.DELETE)
sub_session.send_keys("bmp-hd-test-24")

save_button = driver.find_element(By.XPATH, "//*[contains(@id, 'primaryActionButton')]").click()
time.sleep(3)

#verify that the workflow was saved
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Workflow was saved with updated sub-session name")
    logging.info(f'Sub-session set to bmp-hd-test-24')
else:
    print("Workflow was not saved with updated sub-session name")
    logging.error(f'Sub-session name could not be saved')

driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])[2]").click()
time.sleep(2)

image_format = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Select__select')]")
select = Select(image_format)
select.select_by_value("bmp")
time.sleep(2)

save_button = driver.find_element(By.XPATH, "//*[contains(@id, 'primaryActionButton')]").click()
time.sleep(3)

#verify that the workflow was saved
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Workflow was saved with updated image format and sub-session name")
    logging.info(f'\nImage format set to Windows Bitmap\n'
                 f'Sub-session set to bmp-hd-test-24')
else:
    print("Workflow was not saved with updated image format and sub-session name")
    logging.error(f'Image format and sub-session name could not be saved')

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
time.sleep(sleep_time)

# terminate workflow
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

file_count = 0
for root, dirs, files in os.walk(folder_path_7):
    file_count += len(files)

print(f"Total images: {file_count}")
FPS = file_count / run_time
print(f"Frame rate = {FPS}")
logging.info(f'\nImage format = BMP\n'
             f'Resolution = FULL\n'
             f'Total time run = {run_time}s\n'
             f'Total images = {file_count}\n'
             f'Frame rate = {FPS}\n')


sub_session = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0'])[3]")
sub_session.send_keys(Keys.CONTROL + "a")
sub_session.send_keys(Keys.DELETE)
sub_session.send_keys("bmp-uhd-test-7")

save_button = driver.find_element(By.XPATH, "//*[contains(@id, 'primaryActionButton')]").click()
time.sleep(3)

#verify that the workflow was saved
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Workflow was saved with updated sub-session name")
    logging.info(f'Sub-session set to bmp-uhd-test-7')
else:
    print("Workflow was not saved with updated sub-session name")
    logging.error(f'Sub-session name could not be saved')

m90_image = driver.find_element(By.XPATH, "//*[starts-with(@class, 'p--relative ___')][1]")
m90_image.click()
time.sleep(2)
driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])[2]").click()
time.sleep(2)

#change frame rate
frame_rate = driver.find_element(By.ID, "acq_frame_rate")
frame_rate.send_keys(Keys.CONTROL + "a")
frame_rate.send_keys(Keys.DELETE)
#frame_rate.clear()
time.sleep(2)
frame_rate.send_keys("7")
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
    print("Workflow was saved with updated frame rate and resolution")
    logging.info(f'\nResolution set to UHD\n'
                 f'Frame rate set to 7')
else:
    print("Workflow was not saved with updated frame rate and resolution")
    logging.error(f'Frame rate and Resolution could not be saved')

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
time.sleep(sleep_time)

# terminate workflow
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

file_count = 0
for root, dirs, files in os.walk(folder_path_8):
    file_count += len(files)

print(f"Total images: {file_count}")
FPS = file_count / run_time
print(f"Frame rate = {FPS}")
logging.info(f'\nImage format = BMP\n'
             f'Resolution = UHD\n'
             f'Total time run = {run_time}s\n'
             f'Total images = {file_count}\n'
             f'Frame rate = {FPS}\n')

#change frame rate
frame_rate = driver.find_element(By.ID, "acq_frame_rate")
frame_rate.send_keys(Keys.CONTROL + "a")
frame_rate.send_keys(Keys.DELETE)
#frame_rate.clear()
time.sleep(2)
frame_rate.send_keys("5")
time.sleep(2)

#change resolution
resolution = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Select__select')]")
select = Select(resolution)
select.select_by_value("full")
time.sleep(2)

save_button = driver.find_element(By.XPATH, "//*[contains(@id, 'primaryActionButton')]").click()
time.sleep(3)

#verify that the workflow was saved
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Workflow was saved with updated frame rate and resolution")
    logging.info(f'\nResolution set to FULL\n'
                 f'Frame rate set to 5')
else:
    print("Workflow was not saved with updated frame rate and resolution")
    logging.error(f'Frame rate and Resolution could not be saved')

save_image = driver.find_element(By.XPATH, "//*[contains(@class, 'p--relative')][3]")
save_image.click()
time.sleep(2)
driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])[1]").click()
time.sleep(2)

sub_session = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0'])[3]")
sub_session.send_keys(Keys.CONTROL + "a")
sub_session.send_keys(Keys.DELETE)
sub_session.send_keys("bmp-full-test-5")

save_button = driver.find_element(By.XPATH, "//*[contains(@id, 'primaryActionButton')]").click()
time.sleep(3)

#verify that the workflow was saved
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Workflow was saved with updated sub-session name")
    logging.info(f'Sub-session set to bmp-full-test-5')
else:
    print("Workflow was not saved with updated sub-session name")
    logging.error(f'Sub-session name could not be saved')


#run workflow
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
time.sleep(sleep_time)

#terminate workflow
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

file_count =0
for root, dirs, files in os.walk(folder_path_9):
    file_count += len(files)

print(f"Total images: {file_count}")
FPS = file_count/run_time
print(f"Frame rate = {FPS}")
logging.info(f'\nImage format = BMP\n'
             f'Resolution = FULL\n'
             f'Total time run = {run_time}s\n'
             f'Total images = {file_count}\n'
             f'Frame rate = {FPS}')