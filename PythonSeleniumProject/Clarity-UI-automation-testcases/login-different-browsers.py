import time
from selenium import webdriver
from selenium.webdriver.common.by import By

a = 0

"""""

Testing UI using Chrome browser

"""
driver = webdriver.Chrome()

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
print("Login was successful using Chrome browser")

#logout
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Link ___1u1e4t5')]").click()
time.sleep(3)

clarity_logo = driver.find_element(By.XPATH, "//*[starts-with(@class, 'container wrap')]")
if clarity_logo.is_displayed():
    print("Logout successful on Chrome browser")
    a = a+1
else:
    print("Logout failed on Chrome browser")

driver.quit()

"""""

Testing UI using Edge browser

"""

driver = webdriver.Edge()

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
print("Login was successful using Edge browser")

#logout
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Link ___1u1e4t5')]").click()
time.sleep(3)

clarity_logo = driver.find_element(By.XPATH, "//*[starts-with(@class, 'container wrap')]")
if clarity_logo.is_displayed():
    print("Logout successful on Edge browser")
    a=a+1
else:
    print("Logout failed on Edge browser")

driver.quit()

"""""

Testing UI using Firefox browser

"""

driver = webdriver.Firefox()

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
print("Login was successful using Firefox browser")

#logout
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Link ___1u1e4t5')]").click()
time.sleep(3)

for clarity_logo in driver.find_elements(By.XPATH, "//*[starts-with(@class, 'container wrap')]"):
    try:
        if clarity_logo.is_displayed():
            print("Logout successful on Firefox browser")
            a=a+1
        else:
            print("Logout failed on Firefox browser")
    except Exception as e:
        print("Could not find login page as UI was not logged out", e)
        continue

print("Logout failed on Firefox browser")
driver.quit()

if a == 3:
    print("Login and logout to the UI was successful with all 3 browsers")
else:
    print("Login and logout to the UI was not successful with all 3 browsers")