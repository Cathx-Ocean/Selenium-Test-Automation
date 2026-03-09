import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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

#select any workflow
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs w--100')]").click()
time.sleep(5)

"""""
#change camera name
m90_image = driver.find_element(By.XPATH, "(//span[@class='flowItem_text'])[1]")
m90_image.click()
time.sleep(2)
driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])[1]").click()
time.sleep(2)
camera_name = driver.find_element(By.XPATH, "(//input[@class='fui-Input__input r12stul0'])")
camera_name.clear()
camera_name.send_keys("m90-test")
time.sleep(2)

"""

#change camera time sync method
driver.find_element(By.XPATH, "(//span[@class='fui-AccordionHeader__expandIcon ___7oynyr0 f1l02sjl f22iagw f122n59 f106mvju f1pp30po f1vdfbxk'])[5]").click()
time.sleep(2)
time_sync = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Select__select')]")
select = Select(time_sync)
select.select_by_value("NTPWithPPS")
time.sleep(2)

save_button = driver.find_element(By.XPATH, "//*[contains(@id, 'primaryActionButton')]").click()
time.sleep(3)

#verify that the workflow was saved
saved_workflow = driver.find_element(By.XPATH, "//*[contains(@id, 'toast-title')]")
saved_text = saved_workflow.text
expected_text = "Saved!"
if saved_text == expected_text:
    print("Workflow was saved after changing camera name and time sync method")
else:
    print("Workflow was not saved")