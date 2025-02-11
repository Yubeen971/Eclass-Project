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
    question = quiz["Q #"].loc[quiz.index[x]]
    qStem = quiz["Q Text"].drop_duplicates().loc[quiz.index[x]]
    qNumbers.append(question)
    questions.append(qStem)

numberOfQuestions = list(set(qNumbers))
uniqueQuestions = list(set(questions))

for y in range(0, len(numberOfQuestions), 1):
    listAstley = []

    numAnswers = qNumbers.count(numberOfQuestions[y])
    answersPerQuestion.append(numAnswers)

    for z in range(0, numAnswers, 1):
        answerChoices.append(quiz["Answer"].iloc[quiz.index[z]])

print(answersPerQuestion)
print(answerChoices)
print(questions)