from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

print(answersPerQuestion)
print(answerChoices)
print(uniqueQuestions)

driver = webdriver.Chrome()

driver.get("https://docs.google.com/forms/u/0/") # goes into the form homepage to create new forms
timeLimit = 60 #the program will run for 60 seconds until it stops and exits
x = 0
#The following for loop prints a countdown timer to the console.
for y in range(timeLimit, x, -1):
    if (y != 1):
        print("Wait for " + str(y) + " seconds")
        time.sleep(1)
        y -= 1
    if (y == 1):
        print("Wait for " + str(y) + " second")
# element = driver.find_element(By.CLASS_NAME, "Hvn9fb.zHQkBf")
# element.click()
# element.send_keys("I found this element!")

#xpath for "create forms" button
link = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[1]/img") 
link.click()
# time.sleep(10)
