from chromedriver_selection import chromeselect
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time
import random
import os

quiz = pd.read_csv("Micro Unit 1.4 CW Comparative Advantage and Trade (Vocab Matching) - Question Details.csv") # path of the csv file
quiz.drop(["Section #", "Q Title", "Bonus?", "Difficulty", "Average Score", "# Responses", "Out Of ", "Standard Deviation ", "Discrimination Index ", "Point Biserial"], axis = 1, inplace = True)

directory_name = chromeselect()[0]
service = Service(executable_path=directory_name)

answerChoices = []
qNumbers = []
answersPerQuestion = []
questions = []

uniqueQuestionName = quiz.drop_duplicates(subset=["Answer"], inplace = False)


for x in range(0, uniqueQuestionName.shape[0], 1):
    question = uniqueQuestionName.loc[uniqueQuestionName.index[x], "Q #"]
    qStem = uniqueQuestionName.loc[uniqueQuestionName.index[x], "Answer"]
    qNumbers.append(question)
    questions.append(qStem)

numberOfQuestions = list(set(qNumbers))
uniqueQuestions = list(dict.fromkeys(questions))

print(uniqueQuestions)

onlyTheFirst = (quiz["Answer"] == quiz.loc[quiz.index[0], "Answer"]).sum()
for y in range(0, onlyTheFirst, 1):

    answerChoices.append(quiz["Answer Match"].iloc[quiz.index[y]])

print("_______")
print(answerChoices)


def CheckForMacDown():
    if (chromeselect()[1] == True):
        actions.key_down(Keys.COMMAND)
    else:
        actions.key_down(Keys.LEFT_CONTROL)

def CheckForMacUp():
    if (chromeselect()[1] == True):
        actions.key_up(Keys.COMMAND)
    else:
        actions.key_up(Keys.LEFT_CONTROL)

def MakeNewQuestion():
    CheckForMacDown()
    actions.perform()
    actions.key_down(Keys.LEFT_SHIFT)
    actions.perform()
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(0.05)
    CheckForMacUp()
    actions.perform()
    actions.key_up(Keys.LEFT_SHIFT)
    actions.perform()
driver = webdriver.Chrome(service=service)

def Tab():
    actions.send_keys(Keys.TAB)
    actions.perform()
    time.sleep(0.1)

def ShiftTab():
    actions.key_down(Keys.LEFT_SHIFT)
    actions.perform()
    actions.send_keys(Keys.TAB)
    actions.perform()
    time.sleep(0.05)
    actions.key_up(Keys.LEFT_SHIFT)
    actions.perform()

def TwoNTabs(n):
    timesToTab = 0
    timesToTab = 2 * n
    for x in range(0, timesToTab, 1):
        Tab()

def TwoNPlus1Tabs(n):
    timesToTab = 0
    timesToTab = 2 * n + 1
    for y in range(0, timesToTab, 1):
        Tab()

def TwoNMinus1Tabs(n):
    timesToTab = 0
    timesToTab = 2 * n - 1
    for z in range(0, timesToTab, 1):
        ShiftTab()

actions = ActionChains(driver)
driver.get("https://docs.google.com/forms/u/0/") # goes into the form homepage to create new forms
time.sleep(30)

#xpath for "create forms" button
link = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[1]/img") 
link.click()
time.sleep(5)
element = driver.find_element(By.CLASS_NAME, "Hvn9fb.zHQkBf")
element.click()
element.send_keys("Matching Form")
time.sleep(0.3)


for lp2 in range(0, 22, 1): # Tab to Question Tab
    Tab()
    time.sleep(0.05)

actions.send_keys("Match each term with the correct statement below")
actions.perform()
Tab()
time.sleep(0.05)
Tab()
time.sleep(0.05)
Tab()
time.sleep(0.05)
Tab()
time.sleep(0.05)

for lp in range(1, len(uniqueQuestions) + 1, 1): # tab in 2n times for n < 3 and 2n + 1 times for n > 3
    actions.send_keys(uniqueQuestions[lp - 1])
    actions.perform()
    if (lp < 3):
        TwoNTabs(lp)
        actions.send_keys(Keys.SPACE)
        actions.perform()
        time.sleep(0.05)
        actions.send_keys(answerChoices[lp - 1])
        actions.perform()
        TwoNMinus1Tabs(lp)
    elif (lp >= 3):
        TwoNPlus1Tabs(lp)
        actions.send_keys(Keys.SPACE)
        actions.perform()
        time.sleep(0.05)
        actions.send_keys(answerChoices[lp - 1])
        actions.perform()
        TwoNMinus1Tabs(lp)

TwoNPlus1Tabs(len(uniqueQuestions + 1))

for lp in range(len(uniqueQuestions, len(answerChoices) + 1, 1)):
    Tab()
    Tab()
    actions.send_keys(Keys.SPACE)
    actions.perform()
    time.sleep(0.05)
    actions.send_keys(answerChoices[lp - 1])
    actions.perform()

