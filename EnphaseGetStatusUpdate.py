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
print(driver.title)

driver.find_element('id', 'user_email').send_keys('youremailaddress')
driver.find_element('id', 'user_password').send_keys('yourpassword')
time.sleep(2)
driver.find_element('id', 'submit').click()

time.sleep(5)
try:
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id='page-wrapper']/div[2]/div[2]/div/div/div[2]/div[2]"))).click()
    print ("XPATH Elements Loaded!")
except TimeoutException:
    print ("Loading took too much time!")

print ("______________________________________________________________________________________________________________")

# Print Status of Full Backup Profile
time.sleep(3)
try:
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id='page-container']/div[2]/div[2]/div/div[5]/div[3]/div/div[1]")))
    print ("Full Backup, Status Loaded!")
except TimeoutException:
    print ("Loading took too much time!")
obj = driver.find_element('xpath', "//div[@id='page-container']/div[2]/div[2]/div/div[5]/div[3]/div/div[1]")
print("Your Backup Profile Status. We are Looking for the word (active)\n", obj.text)

print("_______________________________________________________________________________________________________________")

# Print Status of Self Consumption Profile
time.sleep(3)
try:
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id='page-container']/div[2]/div[2]/div/div[5]/div[2]/div/div[1]")))
    print ("Self Consumption, Page Container Loaded!")
except TimeoutException:
    print ("Loading took too much time!")
obj = driver.find_element('xpath', "//div[@id='page-container']/div[2]/div[2]/div/div[5]/div[2]/div/div[1]")
print("Self Consumption Status\n", obj.text)

driver.quit()
