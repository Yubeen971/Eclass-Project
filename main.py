from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import numpy as np
import time
import random

quiz = pd.read_csv("Consulting Test - Question Details.csv") # path of the csv file
quiz.drop(["Section #", "Q Title", "Bonus?", "Difficulty", "Average Score", "# Responses", "Out Of ", "Standard Deviation ", "Discrimination Index ", "Point Biserial"], axis = 1, inplace = True)

answerChoices = []
qNumbers = []
answersPerQuestion = []
questions = []

for x in range(0, quiz.shape[0], 1):
    question = quiz.loc[quiz.index[x], "Q #"]
    qStem = quiz.loc[quiz.index[x], "Q Text"]
    qNumbers.append(question)
    questions.append(qStem)

numberOfQuestions = list(set(qNumbers))
uniqueQuestions = list(dict.fromkeys(questions))

for y in range(0, len(numberOfQuestions), 1):
    listAstley = []

    numAnswers = qNumbers.count(numberOfQuestions[y])
    answersPerQuestion.append(numAnswers)

    for z in range(0, numAnswers, 1):
        answerChoices.append(quiz["Answer"].iloc[quiz.index[z]])

print(uniqueQuestions)

# Selenium Code Starts Here
def MakeNewQuestion():
    actions.key_down(Keys.LEFT_CONTROL)
    actions.perform()
    actions.key_down(Keys.LEFT_SHIFT)
    actions.perform()
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(0.05)
    actions.key_up(Keys.LEFT_CONTROL)
    actions.perform()
    actions.key_up(Keys.LEFT_SHIFT)
    actions.perform()
driver = webdriver.Chrome()

actions = ActionChains(driver)
driver.get("https://docs.google.com/forms/u/0/") # goes into the form homepage to create new forms
time.sleep(40)

#xpath for "create forms" button
link = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[1]/img") 
link.click()
time.sleep(5)
element = driver.find_element(By.CLASS_NAME, "Hvn9fb.zHQkBf")
element.click()
element.send_keys("Test Form")
time.sleep(0.2)

for lp2 in range(0, 22, 1): # Tab to Question 1 Field
    actions.send_keys(Keys.TAB)
    time.sleep(0.3)

for lp in range(0, len(uniqueQuestions), 1):
    actions.key_down(Keys.LEFT_CONTROL)
    actions.perform()
    actions.send_keys("A")
    actions.perform()
    actions.key_up(Keys.LEFT_CONTROL)
    actions.send_keys(uniqueQuestions[lp]) # Enter Questions in Question Field
    actions.perform()
    time.sleep(0.2)

    for tab in range(0, 4, 1):
        actions.send_keys(Keys.TAB) # Tab to Answer Choice 1
        time.sleep(0.1)

    for answer in range(0, answersPerQuestion[lp], 1):
        actions.send_keys(answerChoices[answer]) # Enter Answer Choice
        actions.perform()
        time.sleep(0.1)
        answerChoices.remove(answerChoices[lp])
        actions.send_keys(Keys.ENTER) # Add Another Answer Choice
        actions.perform()
        time.sleep(0.2)
    MakeNewQuestion()
time.sleep(5)
