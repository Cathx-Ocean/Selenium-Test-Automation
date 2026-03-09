import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#open url
driver.get('https://10.1.10.108')
driver.fullscreen_window()
time.sleep(5)

#login
driver.maximize_window()
user = driver.find_element(By.ID, "auth_user_email")
user.send_keys("support@cathxocean.com")
password = driver.find_element(By.ID, "auth_user_password")
password.send_keys("Euphos1250")
time.sleep(2)
password.submit()
time.sleep(5)
driver.maximize_window()
title = driver.title
print(title)
driver.save_screenshot("C:\\Users\SaikrishnaPalvalliMa\\OneDrive - Cathx Ocean Limited\\Pictures\\selenium\\img1.png")

#change acquisition settings
settings = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary.btn-large.toggle-settings").click()
time.sleep(2)
driver.save_screenshot("C:\\Users\SaikrishnaPalvalliMa\\OneDrive - Cathx Ocean Limited\\Pictures\\selenium\\img2.png")
acquisition = driver.find_element(By.CSS_SELECTOR, "div.accordion-heading").click()
time.sleep(2)
exposure_time = driver.find_element(By.ID, "value-acq_exposure_time").clear()
driver.find_element(By.ID, "value-acq_exposure_time").send_keys(5000)
time.sleep(2)
frame_rate = driver.find_element(By.ID, "value-acq_frame_rate").clear()
driver.find_element(By.ID, "value-acq_frame_rate").send_keys(25)
time.sleep(2)
gamma = driver.find_element(By.ID, "value-acq_gamma").clear()
driver.find_element(By.ID, "value-acq_gamma").send_keys(100)
time.sleep(2)
black_level = driver.find_element(By.ID, "value-acq_black_level").clear()
driver.find_element(By.ID, "value-acq_black_level").send_keys(100)
time.sleep(2)
contrast = driver.find_element(By.ID, "value-acq_contrast").clear()
driver.find_element(By.ID, "value-acq_contrast").send_keys(0)
time.sleep(2)
digital_gain = driver.find_element(By.ID, "value-acq_digital_gain").clear()
driver.find_element(By.ID, "value-acq_digital_gain").send_keys(0)
time.sleep(2)
driver.save_screenshot("C:\\Users\SaikrishnaPalvalliMa\\OneDrive - Cathx Ocean Limited\\Pictures\\selenium\\img3.png")
driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
driver.find_element(By.CSS_SELECTOR, "div.accordion-heading").click()
time.sleep(2)

#change image saving settings
driver.find_elements(By.CSS_SELECTOR, "div.accordion-heading")[2].click()
time.sleep(2)
saving_location = driver.find_element(By.ID, "value-image_saving_location").clear()
driver.find_element(By.ID, "value-image_saving_location").send_keys("10.1.10.78:/volume1/images")
time.sleep(2)
saving_password = driver.find_element(By.ID, "value-image_saving_password").clear()
driver.find_element(By.ID, "value-image_saving_password").send_keys("qanas1250")
time.sleep(2)
driver.save_screenshot("C:\\Users\SaikrishnaPalvalliMa\\OneDrive - Cathx Ocean Limited\\Pictures\\selenium\\img4.png")
driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
driver.find_element(By.CSS_SELECTOR, "div.accordion-heading").click()
time.sleep(2)

#change lens control settings
driver.find_elements(By.CSS_SELECTOR, "div.accordion-heading")[5].click()
time.sleep(2)
aperture = driver.find_element(By.ID, "value-lens_aperture").clear()
driver.find_element(By.ID, "value-lens_aperture").send_keys(1.8)
time.sleep(2)
focus = driver.find_element(By.ID, "value-lens_focus").clear()
driver.find_element(By.ID, "value-lens_focus").send_keys("100")
time.sleep(2)
driver.save_screenshot("C:\\Users\SaikrishnaPalvalliMa\\OneDrive - Cathx Ocean Limited\\Pictures\\selenium\\img5.png")