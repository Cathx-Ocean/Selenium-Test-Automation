import time
from selenium import webdriver
from selenium.webdriver.common.by import By
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
driver.find_element(By.XPATH, "//*[contains(@value, 'Six')]").click()
workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'workflow-name')]")
workflow.clear()
workflow.send_keys("maskk")
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

#Mask Generation microservice
ffmask = driver.find_element(By.XPATH, "(//span[@class='flowItem_text'])")
ffmask.click()
time.sleep(2)
driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])").click()
time.sleep(2)
input_images = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0 ___1q6bera ffczdla'])[1]")
input_images.clear()
input_images.send_keys("/cathx_data/images/output/One/Port_L1000/Port_L1000_Stills/Port_L1000_0000")
time.sleep(2)
mask_output = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0 ___1q6bera ffczdla'])[2]")
mask_output.clear()
mask_output.send_keys("/cathx_data/images/dataset")
time.sleep(2)
mask_name = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0'])")
mask_name.clear()
mask_name.send_keys("ff-mask-img")
time.sleep(2)

#testing minimum image count slider
min_img_slider = driver.find_element(By.XPATH, "(//input[@type='range'])[1]")
actions = ActionChains(driver)
actions.click_and_hold(min_img_slider).move_by_offset(50, 0).release().perform()
time.sleep(2)

min_img_count = driver.find_element(By.ID, "min_image_count")
min_img_count.clear()
min_img_count.send_keys("10")
time.sleep(2)

#testing maximum image count slider
max_img_slider = driver.find_element(By.XPATH, "(//input[@type='range'])[2]")
actions = ActionChains(driver)
actions.click_and_hold(max_img_slider).move_by_offset(50, 0).release().perform()
time.sleep(2)

max_img_count = driver.find_element(By.ID, "max_image_count")
max_img_count.clear()
max_img_count.send_keys("50")
time.sleep(2)

#testing maximum features slider
max_features_slider = driver.find_element(By.XPATH, "(//input[@type='range'])[3]")
actions = ActionChains(driver)
actions.click_and_hold(max_features_slider).move_by_offset(50, 0).release().perform()
time.sleep(2)

features = driver.find_element(By.ID, "featureless_keypoint_threshold")
features.clear()
features.send_keys("1000")
time.sleep(2)

save_button = driver.find_element(By.XPATH, "//*[contains(@id, 'primaryActionButton')]").click()
time.sleep(3)

#verify that the workflow was saved
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Workflow was saved after flat-field mask details")
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


#logout
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Link ___1u1e4t5')]").click()
time.sleep(3)


