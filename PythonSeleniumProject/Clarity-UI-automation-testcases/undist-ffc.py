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
driver.find_element(By.XPATH, "//*[contains(@value, 'Three')]").click()
workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'workflow-name')]")
workflow.clear()
workflow.send_keys("test-ffc")
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

"""""
#folder image provider
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs w--100')]").click()
time.sleep(2)
folder = driver.find_element(By.XPATH, "(//span[@class='flowItem_text'])[1]")
folder.click()
time.sleep(2)
driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])[1]").click()
time.sleep(2)
input_folder = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0 ___1q6bera ffczdla'])")
input_folder.clear()
input_folder.send_keys("/cathx_data/images/dataset/Port_Stills")
time.sleep(2)
driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])[2]").click()
time.sleep(2)
filter_folder = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0 ___1q6bera ffczdla'])[2]")
filter_folder.clear()
filter_folder.send_keys("/cathx_data/images/output")
time.sleep(2)
ffc = driver.find_element(By.XPATH, "(//span[@class='flowItem_text'])[2]")
ffc.click()
time.sleep(2)
save_microservice = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-DialogContent r1v5zwsm')]")
save_microservice_text = save_microservice.text
if "You have unsaved changes to your microservice(s). Would you like to save them before proceeding? Please note that any unsaved changes will be lost." in save_microservice_text:
    print("Save microservice warning was displayed after clicking Flat-Field Correction microservice")
else:
    print("Save microservice warning was not displayed after clicking Flat-Field Correction microservice")
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___1srby3n')]").click()
time.sleep(3)
"""

#update resolution
m90_image = driver.find_element(By.XPATH, "(//span[@class='flowItem_text'])")
m90_image.click()
time.sleep(2)
image_format = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Select__select')]")
select = Select(image_format)
select.select_by_value("hd")
time.sleep(2)
save_button = driver.find_element(By.XPATH, "//*[contains(@id, 'primaryActionButton')]").click()
time.sleep(3)

#verify that the workflow was saved
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Workflow was saved after updating resolution")
else:
    print("Workflow was not saved")

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


#enter mask details
ffc = driver.find_element(By.XPATH, "(//span[@class='flowItem_text'])[3]")
ffc.click()
time.sleep(2)
driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])").click()
time.sleep(2)
mask_path = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0 ___1q6bera ffczdla'])")
mask_path.clear()
time.sleep(2)
mask_path.send_keys("/cathx_data/images/dataset/ff-mask-hd.png")
time.sleep(2)
dist_calib = driver.find_element(By.XPATH, "(//span[@class='flowItem_text'])[3]")
dist_calib.click()
time.sleep(2)
save_microservice = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-DialogContent r1v5zwsm')]")
save_microservice_text = save_microservice.text
if "You have unsaved changes to your microservice(s). Would you like to save them before proceeding? Please note that any unsaved changes will be lost." in save_microservice_text:
    print("Save microservice warning was displayed after clicking Distortion Correction microservice")
else:
    print("Save microservice warning was not displayed after clicking Distortion Correction microservice")
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___1srby3n')]").click()
time.sleep(3)

#enter calibration filepath
#driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs w--100')]").click()
#time.sleep(2)
dist_calib = driver.find_element(By.XPATH, "(//span[@class='flowItem_text'])[4]")
dist_calib.click()
time.sleep(2)
#driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])").click()
#time.sleep(2)
calib_path = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0 ___1q6bera ffczdla'])")
calib_path.clear()
calib_path.send_keys("/cathx_data/images/calibration/camera_parameters/WOS20_Port_L1000_cam_params.yml")
time.sleep(2)
save_image = driver.find_element(By.XPATH, "(//span[@class='flowItem_text'])[4]")
save_image.click()
time.sleep(2)
save_microservice = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-DialogContent r1v5zwsm')]")
save_microservice_text = save_microservice.text
if "You have unsaved changes to your microservice(s). Would you like to save them before proceeding? Please note that any unsaved changes will be lost." in save_microservice_text:
    print("Save microservice warning was displayed after clicking save image microservice")
else:
    print("Save microservice warning was not displayed after clicking save image microservice")
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___1srby3n')]").click()
time.sleep(3)

#enter details for image saving location
save_image = driver.find_element(By.XPATH, "(//span[@class='flowItem_text'])[5]")
save_image.click()
time.sleep(2)
driver.find_element(By.XPATH, "(//span[@class='fui-Text ___i24qii0 fk6fouc fod5ikn faaz57k fl43uef fpgzoln f1w7gpdv f6juhto f1gl81tg f2jf649'])[1]").click()
time.sleep(2)
camera_name = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0'])[1]")
camera_name.clear()
camera_name.send_keys("Port_Stills")
time.sleep(2)
#base_folder_path = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0 ___1q6bera ffczdla'])")
#base_folder_path.clear()
#base_folder_path.send_keys("/cathx_data/images/dataset/Port_L1000")
time.sleep(2)
session_name = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0'])[2]")
session_name.clear()
session_name.send_keys("test-automation")
time.sleep(2)
subsession_name = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0'])[3]")
subsession_name.clear()
subsession_name.send_keys("save-here")
time.sleep(2)

#driver.find_element(By.XPATH, "(//span[@class='fui-Text ___i24qii0 fk6fouc fod5ikn faaz57k fl43uef fpgzoln f1w7gpdv f6juhto f1gl81tg f2jf649'])[2]").click()
#time.sleep(2)
image_format = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Select__select')]")
select = Select(image_format)
select.select_by_value("png")
time.sleep(2)
image_quality = driver.find_element(By.ID, "image_quality")
image_quality.clear()
image_quality.send_keys("90")
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