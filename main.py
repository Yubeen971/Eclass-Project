from selenium import webdriver
import pandas as pd

# driver = webdriver.Chrome() # Supported browsers include Chrome, Firefox, and Safari

# driver.get("url") get the URL (protocol needs to be specified)

dataFrame = pd.read_csv("Consulting Test - Question Details.csv") # Include the name of each csv file here

specifiedFrame = dataFrame[["Q #", "Q Text", "Answer", "Answer Match"]]

print(specifiedFrame)
