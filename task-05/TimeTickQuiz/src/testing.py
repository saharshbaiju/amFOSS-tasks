# # time_tick_quiz.py

# import requests
# import html
# import random
# import threading
# import time
# import json
# import pyfiglet

# CATEGORY_URL = "https://opentdb.com/api_category.php"
# QUESTION_URL = "https://opentdb.com/api.php"
# TIME_LIMIT = 15  # seconds per question

# # ------------------ api functionss ------------------

# def fetch_categories():
#     response = requests.get(CATEGORY_URL)
#     data = response.json()
#     for i in data['trivia_categories']:
#         print(f"{i['name']}  - {i['id']} ")

    
# # fetch_categories()


# def fetch_questions(amount,difficulty,type,category):
#     params = {"amount":amount, "difficulty": difficulty,"type": type,"category":category}
#     response = requests.get(QUESTION_URL,params=params)
#     questions = response.json()
#     return questions
# # ------------------ design fucntions ------------------
# def intro():
#     result = pyfiglet.figlet_format("TimeTickQuiz")
#     print(result)

# intro()
# fetch_categories()

# # ------------------ user input selection ------------------

# def select_category():
#     categ_select = int(input('Select the category by Id:'))
#     return categ_select
        

# def select_difficulty():
#     difficulty = input("Select difficulty between - {easy,medium,hard} : ").lower()
#     return difficulty

# def select_question_type():
#     select = input("Select - {multiple,boolean} : ").lower()
#     return select


# cat = select_category()
# diff = select_difficulty()
# typ = select_question_type()
# # ------------------ quiz logicc ------------------

# questionslist = []

# def ask_question():
#     questions = fetch_questions(10, diff, typ, cat)
#     if len(questions['results']) < 10:
#         print(f"Only {len(questions['results'])} questions available, cannot fetch 10.")
#         return
    
#     global questionslist
#     i = 9
#     while i >= 0:
#         questionslist.append(questions['results'][i]['question'])
#         i -= 1
# print(questionslist)

# def select_quiz_options(categories):
#     if categories == 'boolean':
#         print("""
#                 Enter your answer
#                 True
#                 or
#                 False
#                 """)
#     elif categories == 'multiple':
        
#         pass




# # ------------------ main fucntion ------------------

# def main():
#     ask_question()

    

# if __name__ == "__main__":
#     main()

import time
import progressbar

for i in progressbar.progressbar()(range(100)):
    time.sleep(0.15)