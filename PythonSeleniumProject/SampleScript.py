import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome()
driver = webdriver.Firefox()

#open url
driver.get('https://www.saucedemo.com/')
driver.fullscreen_window()
time.sleep(5)

#login
user = driver.find_element(By.ID, "user-name")
user.send_keys("standard_user")
password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")
time.sleep(2)
password.submit()
time.sleep(5)
#driver.maximize_window()

#add item to cart
driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
time.sleep(2)
driver.find_element(By.ID, "shopping_cart_container").click()
time.sleep(2)
driver.find_element(By.NAME, "checkout").click()
time.sleep(2)

#checkout
driver.find_element(By.ID, "first-name").send_keys("abc")
driver.find_element(By.ID, "last-name").send_keys("xyz")
driver.find_element(By.ID, "postal-code").send_keys("d03ab89")
time.sleep(2)
driver.find_element(By.NAME, "continue").click()
time.sleep(5)
driver.find_element(By.NAME, "finish").click()
time.sleep(2)

#logout
#driver.find_element(By.ID, "react-burger-menu-btn").click()
#driver.find_element(By.CLASS_NAME, "bm-item menu-item").click()
#time.sleep(5)

driver.quit()