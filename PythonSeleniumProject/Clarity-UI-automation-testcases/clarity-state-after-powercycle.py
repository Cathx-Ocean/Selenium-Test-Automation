import socket
import sys

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

DS378_IP = '10.1.10.203'
DS378_PORT = 17123
RELAY_CMD_ON = 'SR 2 on'
RELAY_CMD_OFF = 'SR 2 off'


def tcp_client_socket(ip_add,portno):

    # TCP connection to ds378

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_add, portno))
    except Exception as e:
        print(str(e))
        return 'Fail'
    return s


tcp_sock=tcp_client_socket(DS378_IP,DS378_PORT)
if tcp_sock == 'Fail':
    sys.exit()


driver = webdriver.Chrome()

#open url
driver.get('http://10.1.10.118/clarity/')
driver.fullscreen_window()
time.sleep(5)

#login
email = driver.find_element(By.XPATH, "//*[contains(@id, 'input-email')]")
email.send_keys("admin@cathxocean.com")
password = driver.find_element(By.XPATH, "//*[contains(@id, 'input-password')]")
password.send_keys("admin")
password.submit()
time.sleep(5)

#run workflow
driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs w--100')]").click()
time.sleep(5)
run_workflow = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___19y96bh')]").click()
time.sleep(3)
continue_workflow = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Button r1alrhcs ___1srby3n')]").click()
time.sleep(5)
run_content = driver.find_element(By.XPATH, "//*[contains(@class, 'd--flex ai--center jc--flex-start w--100')]")
run_text = run_content.text
if "Running Workflow" in run_text:
    print("Workflow is running....")
else:
    print("No workflow was running")

#status check
run_status = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Badge r1l7mb74')]")
status_text = run_status.text
if "Engine Running" in status_text:
    print("Engine status: running")
else:
    print("Engine status is not running")

time.sleep(180)
tcp_sock.send(RELAY_CMD_OFF.encode('ascii'))
time.sleep(5)
print("Camera is turned off")
tcp_sock.send(RELAY_CMD_ON.encode('ascii'))
time.sleep(60)
print("Camera is turned on")

#login
email = driver.find_element(By.XPATH, "//*[contains(@id, 'input-email')]")
email.send_keys("admin@cathxocean.com")
password = driver.find_element(By.XPATH, "//*[contains(@id, 'input-password')]")
password.send_keys("admin")
password.submit()
time.sleep(5)

#status check
run_status = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Badge r1l7mb74')]")
status_text = run_status.text
if "Engine Running" in status_text:
    print("Engine status: running")
    print("Clarity state is restored after repower when previous running time was 180s")
else:
    print("Engine status is not running")
    print("Clarity state is not restored after repower")


tcp_sock.send(RELAY_CMD_OFF.encode('ascii'))
time.sleep(5)
print("Camera is turned off")
tcp_sock.send(RELAY_CMD_ON.encode('ascii'))
time.sleep(60)
print("Camera is turned on")

#login
email = driver.find_element(By.XPATH, "//*[contains(@id, 'input-email')]")
email.send_keys("admin@cathxocean.com")
password = driver.find_element(By.XPATH, "//*[contains(@id, 'input-password')]")
password.send_keys("admin")
password.submit()
time.sleep(5)

#status check
idle_status = driver.find_element(By.XPATH, "//*[contains(@class, 'fui-Badge r1l7mb74')]")
status_text = idle_status.text
if "Engine Idle" in status_text:
    print("Engine status: idle")
    print("Clarity state is not restored after repower when previous running time was less than 180s")
else:
    print("Test failed!")

