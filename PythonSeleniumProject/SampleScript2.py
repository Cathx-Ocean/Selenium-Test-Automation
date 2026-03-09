import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

#open url
driver.get("https://magento.softwaretestingboard.com/?ref=hackernoon.com")
driver.fullscreen_window()
time.sleep(5)

#Create a new account
account = driver.find_element(By.LINK_TEXT, "Create an Account").click()
time.sleep(5)
driver.fullscreen_window()
time.sleep(2)
first = driver.find_element(By.ID, "firstname").send_keys("abcd")
last = driver.find_element(By.ID, "lastname").send_keys("xyz")
email = driver.find_element(By.NAME, "email").send_keys("hello@practice.com")
password = driver.find_element(By.NAME, "password").send_keys("iamaqa27!")
confirm_password = driver.find_element(By.NAME, "password_confirmation").send_keys("iamaqa27!")
time.sleep(2)
submit = driver.find_element(By.CSS_SELECTOR, 'div.primary').click()
time.sleep(5)
