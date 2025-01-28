from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def GenerateRandomDelay():
    val = random.randrange(1, 5)
    delay = val / 10
    return delay

driver = webdriver.Firefox() # Supported browsers include Chrome, Firefox, and Safari

driver.get("https://instruction.gwinnett.k12.ga.us/d2l/lms/quizzing/user/quiz_submissions_attempt.d2l?isprv=&qi=4030818&ai=44497764&isInPopup=0&cfql=0&fromQB=0&fromSubmissionsList=1&ou=4971124") # get the URL (protocol needs to be specified)

print("Once you get to the sign in page, enter your information as normal. Don't worry. This information will not be saved")
time.sleep(60)

input_element = driver.find_element(By.ID, "ctl_10")

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ctl_10")))

input_element.send_keys(Keys.CONTROL + "C")

time.sleep(GenerateRandomDelay())

link = driver.find_element(By.ID, "ctl_14")

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ctl_14")))

link.send_keys(Keys.CONTROL + "C")

time.sleep(60)

driver.quit() # close program