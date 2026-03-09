import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

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

#toggle dark mode / light mode
driver.find_element(By.XPATH, "(//input[@type='checkbox'])").click()
time.sleep(3)
print("UI changed to light mode")
driver.find_element(By.XPATH, "(//input[@type='checkbox'])").click()
time.sleep(3)
print("UI changed to dark mode")

#import workflow
file_input = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___1uti6m1')]")
file_input.click()
time.sleep(3)

file_path = os.path.abspath("C:\\CxInsights_v1.4.1.1\\workflows\\Undistort%two.xml")
#print(file_path)

file_input.send_keys(file_path)