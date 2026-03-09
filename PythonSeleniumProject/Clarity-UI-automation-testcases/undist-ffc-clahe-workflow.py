import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

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
driver.find_element(By.XPATH, "//*[contains(@value, 'Four')]").click()
workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'workflow-name')]")
workflow.clear()
workflow.send_keys("test-distortion-flat-field-clahe")
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


#enter mask filepath
mask_path = driver.find_element(By.XPATH, "(//span[@class='flowItem_text'])[3]")
mask_path.click()
time.sleep(2)
driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])").click()
time.sleep(2)
path_to_mask = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0 ___1q6bera ffczdla'])")
path_to_mask.clear()
path_to_mask.send_keys("/cathx_data/images/dataset/ff-mask-hd.png")
time.sleep(2)


#enter calibration filepath
dist_calib = driver.find_element(By.XPATH, "(//span[@class='flowItem_text'])[4]")
dist_calib.click()
time.sleep(2)
save_microservice = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-DialogContent r1v5zwsm')]")
save_microservice_text = save_microservice.text
if "You have unsaved changes to your microservice(s). Would you like to save them before proceeding? Please note that any unsaved changes will be lost." in save_microservice_text:
    print("Save microservice warning was displayed after clicking distortion correction microservice")
else:
    print("Save microservice warning was not displayed after clicking distortion correction microservice")
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___1srby3n')]").click()
time.sleep(3)
#driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])").click()
#time.sleep(3)
calib_path = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0 ___1q6bera ffczdla'])")
calib_path.clear()
calib_path.send_keys("/cathx_data/images/calibration/ExampleParameterFiles/camera_parameters/WOS20_Port_L1000_cam_params.yml")
time.sleep(2)
save_image = driver.find_element(By.XPATH, "(//span[@class='flowItem_text'])[5]")
save_image.click()
time.sleep(2)
save_microservice = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-DialogContent r1v5zwsm')]")
save_microservice_text = save_microservice.text
if "You have unsaved changes to your microservice(s). Would you like to save them before proceeding? Please note that any unsaved changes will be lost." in save_microservice_text:
    print("Save microservice warning was displayed after clicking clahe microservice")
else:
    print("Save microservice warning was not displayed after clicking clahe microservice")
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___1srby3n')]").click()
time.sleep(3)

#update clahe settings
clahe = driver.find_element(By.XPATH, "(//span[@class='flowItem_text'])[5]")
clahe.click()
time.sleep(2)
#driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])[1]").click()
#time.sleep(2)
clahe_clip_limit = driver.find_element(By.ID, "clahe_clip_limit")
clahe_clip_limit.clear()
clahe_clip_limit.send_keys("1.5")
clip_limit_slider = driver.find_element(By.XPATH, "(//input[@type='range'])[1]")
actions = ActionChains(driver)
actions.click_and_hold(clip_limit_slider).move_by_offset(50, 0).release().perform()
time.sleep(2)
driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])[2]").click()
time.sleep(2)


grid_size_x = driver.find_element(By.ID, "title_grid_size_x")
grid_size_x.clear()
grid_size_x.send_keys("10")
time.sleep(2)

#testing sliders
grid_size_x_slider = driver.find_element(By.XPATH, "(//input[@type='range'])[2]")
actions = ActionChains(driver)
actions.click_and_hold(grid_size_x_slider).move_by_offset(50, 0).release().perform()
actions.click_and_hold(grid_size_x_slider).move_by_offset(0, 50).release().perform()
time.sleep(2)

grid_size_y = driver.find_element(By.ID, "title_grid_size_y")
grid_size_y.clear()
grid_size_y.send_keys("10")
time.sleep(2)

#testing sliders
grid_size_y_slider = driver.find_element(By.XPATH, "(//input[@type='range'])[3]")
actions = ActionChains(driver)
actions.click_and_hold(grid_size_y_slider).move_by_offset(50, 0).release().perform()
actions.click_and_hold(grid_size_y_slider).move_by_offset(0, 50).release().perform()
time.sleep(2)


#enter details for image saving location
save_image = driver.find_element(By.XPATH, "(//span[@class='flowItem_text'])[6]")
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
driver.find_element(By.XPATH, "(//span[@class='fui-Text ___i24qii0 fk6fouc fod5ikn faaz57k fl43uef fpgzoln f1w7gpdv f6juhto f1gl81tg f2jf649'])[1]").click()
time.sleep(2)
camera_name = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0'])[1]")
camera_name.clear()
camera_name.send_keys("Port_Stills")
time.sleep(2)
#base_folder_path = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0 ___1q6bera ffczdla'])")
#base_folder_path.clear()
#base_folder_path.send_keys("/cathx_data/images/output")
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

#testing sliders
image_quality_slider = driver.find_element(By.XPATH, "(//input[@type='range'])[3]")
actions = ActionChains(driver)
actions.click_and_hold(image_quality_slider).move_by_offset(20, 0).release().perform()
actions.click_and_hold(image_quality_slider).move_by_offset(0, 20).release().perform()
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
time.sleep(2)
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
time.sleep(10)
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