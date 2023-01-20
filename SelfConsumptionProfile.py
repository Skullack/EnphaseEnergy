# Enphase Automation Script Written By Skullack on 18 January 2023
# You are welcome to do anything with this script
# This script runs headless so no need to install a browser. I do advise you set schedule for the script to run.
# If using Linux please change the executable path accordingly. Also ensure you install the relevant drivers.
# This script will change your profile to SELF CONSUMPTION !!!!

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

options = Options()
options.headless = True

chrome_executable = Service(executable_path='c:\\ChromeDriver\\chromedriver.exe', log_path='NUL')
driver = webdriver.Chrome(service=chrome_executable, options=options)
driver.implicitly_wait(30)

driver.get('https://enlighten.enphaseenergy.com/')
# Ensure that the browser is actually loading
print(driver.title)

driver.find_element('id', 'user_email').send_keys('youremailaddress')
driver.find_element('id', 'user_password').send_keys('yourpassword')
time.sleep(2)
driver.find_element('id', 'submit').click()

time.sleep(5)
try:
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id='page-wrapper']/div[2]/div[2]/div/div/div[2]/div[2]"))).click()
    print ("XPATH Elements Loaded!")
except TimeoutException:
    print ("Loading took too much time!")

try:
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id='page-container']/div[2]/div[2]/div/div[5]/div[2]/div/div[2]/button"))).click()
    print ("Loaded Self Consumption Button and Activating it!")
except TimeoutException:
    print ("Loading took too much time!")

try:
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[@id='save']/span"))).click()
    print ("Activating SAVE Button!")
except TimeoutException:
    print ("Loading took too much time!")

time.sleep(5)
obj = driver.find_element('xpath', "//div[@id='page-container']/div[2]/div[2]/div/div[5]/div[2]/div/div[1]")
print(obj.text)

driver.quit()
