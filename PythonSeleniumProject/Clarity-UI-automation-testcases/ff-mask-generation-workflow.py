import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

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
driver.find_element(By.XPATH, "//*[contains(@value, 'Online_Flat-Field_Mask_Generation')]").click()
workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'workflow-name')]")
workflow.clear()
workflow.send_keys("test-mask-generation-2")
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

#ffc mask generation microservice
mask_details = driver.find_element(By.XPATH, "(//span[@class='flowItem_text'])")
mask_details.click()
time.sleep(2)
driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])[1]").click()
time.sleep(2)
input_images_path = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0 ___1q6bera ffczdla'])[1]")
input_images_path.clear()
input_images_path.send_keys("/cathx_data/images/output/Basic")
time.sleep(2)
output_mask_path = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0 ___1q6bera ffczdla'])[2]")
output_mask_path.clear()
output_mask_path.send_keys("/cathx_data/images/output/ffc_mask1.png")
time.sleep(2)
mask_name = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0'])")
mask_name.clear()
mask_name.send_keys("test-mask")
time.sleep(2)

min_image_count = driver.find_element(By.ID, "min_image_count")
min_image_count.clear()
min_image_count.send_keys("0")
time.sleep(2)

#testing sliders
min_image_count_slider = driver.find_element(By.XPATH, "(//input[@type='range'])[1]")
actions = ActionChains(driver)
actions.click_and_hold(min_image_count_slider).move_by_offset(50, 0).release().perform()
actions.click_and_hold(min_image_count_slider).move_by_offset(0, 50).release().perform()
time.sleep(2)

max_image_count = driver.find_element(By.ID, "max_image_count")
max_image_count.clear()
max_image_count.send_keys("0")
time.sleep(2)

#testing sliders
max_image_count_slider = driver.find_element(By.XPATH, "(//input[@type='range'])[2]")
actions = ActionChains(driver)
actions.click_and_hold(max_image_count_slider).move_by_offset(50, 0).release().perform()
actions.click_and_hold(max_image_count_slider).move_by_offset(0, 50).release().perform()
time.sleep(2)

features = driver.find_element(By.ID, "featureless_keypoint_threshold")
features.clear()
features.send_keys("2000")
time.sleep(2)

#testing sliders
features_slider = driver.find_element(By.XPATH, "(//input[@type='range'])[3]")
actions = ActionChains(driver)
actions.click_and_hold(features_slider).move_by_offset(50, 0).release().perform()
actions.click_and_hold(features_slider).move_by_offset(0, 50).release().perform()
time.sleep(2)

#save microservice
save_button = driver.find_element(By.XPATH, "//*[contains(@id, 'primaryActionButton')]").click()
time.sleep(3)
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Workflow was saved after updating mask details")
else:
    print("Workflow was not saved after updating mask details")

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
time.sleep(2)
run_content = driver.find_element(By.XPATH, "//*[contains(@class, 'd--flex ai--center jc--flex-start w--100')]")
run_text = run_content.text
if "Running Workflow" in run_text:
    print("Workflow is running....")
else:
    print("No workflow was running")
time.sleep(5)
complete_content = driver.find_element(By.XPATH, "//*[contains(@class, 'd--flex ai--center jc--flex-start w--100')]")
complete_content_text = complete_content.text
if "Workflow Completed" in complete_content_text:
    print("Workflow finished successfully")
else:
    print("Workflow could not be completed")

#logout
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Link ___1u1e4t5')]").click()
time.sleep(3)
driver.quit()