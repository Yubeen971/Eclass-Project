This is a simple tool to relocate quizzes from the service D2L to Google Forms for easier access to educators

Note: The creators of this program are not affiliated with D2L or Google

How to use:
1. On a D2L linked website, download your quiz information as a csv file. The file name should include "Question Details -"
2. Download and install Python along with the libraries pandas and selenium if not already installed. Refer to the Links section lower down to install the necessary dependencies.
3. Navigate to the main.py or matchquestions.py file depending on what type of quizzes you want to navigate to. For multiple choice and multiple select questions, run main.py. For matching questions, run matchquestions.py. 
4. Look for the line labeled "quiz = pd.read_csv". Follow the information in the comment on this line
5. Run either file specified in step 3
6. If prompted, sign into your google account. You have 30 seconds to do this or the program will not run properly. Your information will not be saved into the program
7. After sign in, the program should create a new google form and fill in the question fields automatically. In the event that not everything was transferred, fill in the missing information manually.

Links: 

Python Install: https://www.python.org/

Library Installs (Enter given commands in Command Prompt once Python is installed):

Pandas: https://pypi.org/project/pandas/

Selenium: https://pypi.org/project/selenium/