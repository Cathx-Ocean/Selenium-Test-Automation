import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#open url
driver.get('http://10.1.10.123/clarity/')
driver.fullscreen_window()
time.sleep(5)

#login
email = driver.find_element(By.XPATH, "//*[contains(@id, 'input-email')]")
email.send_keys("admin@cathxocean.com")
password = driver.find_element(By.XPATH, "//*[contains(@id, 'input-password')]")
password.send_keys("admin")
password.submit()
time.sleep(5)


#disable safemode
safemode_off = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ml--XL')]").click()
time.sleep(2)
dialog_on_content = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-ToastBody')]")
time.sleep(2)
dialog_on_text = dialog_on_content.text
if "Safe Mode" in dialog_on_text:
    print("Safemode was turned off")
else:
    print("Safemode was not turned off")
#dialog_close = driver.find_element(By.XPATH, "//*[contains(@class, 'p--absolute')]").click()
time.sleep(5)


#enable safemode
safemode_on = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ml--XL')]").click()
time.sleep(5)
dialog_off_content = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Toast rhf7k35 p--absolute')]")
time.sleep(2)
dialog_off_text = dialog_off_content.text
if "The safe mode is " in dialog_off_text:
    print("Safemode was turned on")
else:
    print("Safemode was not turned on")
#dialog_close = driver.find_element(By.XPATH, "//*[contains(@id, 'p--absolute')]").click()
time.sleep(2)

