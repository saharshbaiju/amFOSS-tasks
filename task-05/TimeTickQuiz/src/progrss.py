# import time
# import progressbar

# def progress_bar():
#     bar = progressbar.ProgressBar(widgets=[progressbar.Bar()])
#     for i in bar(range(1000)):
#         time.sleep(0.015)

# progress_bar()

# time_tick_quiz.py

import requests
import html
import random
import threading
import time
import json
import pyfiglet

CATEGORY_URL = "https://opentdb.com/api_category.php"
QUESTION_URL = "https://opentdb.com/api.php"
TIME_LIMIT = 15  # seconds per question

# ------------------ api functionss ------------------

def fetch_categories():
    response = requests.get(CATEGORY_URL)
    data = response.json()
    for i in data['trivia_categories']:
        print(f"{i['name']}  - {i['id']} ")
    print()
    print()
    print()


def fetch_questions(difficulty,type,category):
    params = {"amount" : 10,"difficulty": difficulty,"type": type,"category":category}
    response = requests.get(QUESTION_URL,params=params)
    questions = response.json()
    return questions


# ------------------ design fucntions ------------------
def intro():
    result = pyfiglet.figlet_format("TimeTickQuiz")
    print(result)

intro()
fetch_categories()

# ------------------ user input selection ------------------

def select_category():
    print("""Select category from the following..
If you want mixed category question type  = '0'""")
    categ_select = int(input('Select the category by Id:'))
    if categ_select == 0:
        categ_select = None
    return categ_select
        

def select_difficulty():
    difficulty = input("Select difficulty between - {easy,medium,hard,any} : ").lower()
    if difficulty == 'any':
        difficulty = None

    return difficulty

def select_question_type():
    select = input("Select - {multiple,boolean} : ").lower()
    return select





#timer input function without progress bar

# def timed_input(timeout=15):
#     import time
#     import progressbar

#     answer = [None]
#     def progress_bar():
#         bar = progressbar.ProgressBar(widgets=[progressbar.Bar()])
#         for i in bar(range(1000)):
#             time.sleep(0.015)
        
#     def ask():
#         if type == 'boolean':
#             answer[0] = input('Enter True/False : ')
#         elif type == 'multiple':
#             answer[0] = ('Choose correct option from the above options: ')

#     t = threading.Thread(target=ask)
#     t.daemon = True
#     t.start()

#     t.join(timeout)
    

#     if t.is_alive():
#         print("\n Time's up!")
#         return None
#         pass
#     else:
#         return answer[0]



cat = select_category()
diff = select_difficulty()
typ = select_question_type()

def timed_input(timeout=15):
    answer = [None]

    def ask():
        if typ == 'boolean':
            answer[0] = input('Enter True/False : ')
        elif typ == 'multiple':
                    try:
                        answer[0] = int(input('Choose correct option from the above options: '))
                    except ValueError:
                        answer[0] = None

    t = threading.Thread(target=ask)
    t.daemon = True
    t.start()
    t.join(timeout)

    if t.is_alive():
        print("\n Time's up!")
        return None
    else:
        return answer[0]

# # ------------------ quiz logicc ------------------

questionslist = []
questionorg = None
score = 0  

def ask_question():
    
    global questionslist,questionorg,score,typ
    questions = fetch_questions(diff,typ,cat)
    questionorg = questions
    if len(questions['results']) == 0:
        print('No questions available on this configruation')

    if len(questions['results']) < 10 and len(questions['results']) > 0 :
        print(f"Only {len(questions['results'])} questions available, not 10.")
        print('STARTING WITH AVAILABLE QUESTIONS')
        for i in questions['results']:
            questionslist.append([i]['question'])

        
    elif len(questions['results']) == 10:
        print('10 Questions available ..')
        i = 9
        while i >= 0:
            questionslist.append(questions['results'][i]['question'])
            i -=1
    
    
    
    
        
        if typ == 'boolean':
            for i in range(len(questionslist)):
                print(f"Q{i}) {questionslist[i]}")
                answer = timed_input()
                if answer == None:
                    continue

                for j in questions['results']:
                    if j['question'] == questionslist[i]:
                        correct_ans = j['correct_answer']
                        correct_answer = correct_ans.strip().lower()
                        if correct_answer == answer.lower():
                            print('Correct answer ... Well done')
                            score +=1
                            print(f"Your current score is {score}/10")
                        else:
                            print('Incorrect answer')
                            print(f"Your current score is {score}/10")


        elif typ == 'multiple':
            for i in range(len(questionslist)):
                option = list()
                print(f"Q{i}) {questionslist[i]}")
                for j in questions['results']:
                    if j['question'] == questionslist[i]:
                        incorrect_ans = j['incorrect_answers']
                        correct_ans = j['correct_answer']
                        correct_answer = correct_ans.strip().lower()
                        list_options = incorrect_ans + [correct_answer]
                        num = 1
                        for k in range(4):
                            index = random.sample(range(1, 11), 3)
                            option.append(list_options[k])
                            print(f'{num}: {list_options[k]}')
                            num +=1
                answer = timed_input()
                if answer == None:
                    continue
                for j in questions['results']:
                    if j['question'] == questionslist[i]:
                        correct_ans = j['correct_answer']
                        correct_answer = correct_ans.strip().lower()
                        in_answer = option[answer-1]
                        if in_answer == correct_answer:
                            score += 1
                            print('Correct answer ... Well done')
                            print(f"Your current score is {score}/10")
                        else:
                            print('Incorrect answer')
                            print(f"Your current score is {score}/10")


def select_quiz_options(categories):
    if categories == 'boolean':
        print("""
                Enter your answer
                True
                or
                False
                """)
    elif categories == 'multiple':
        pass


# ------------------ main fucntion ------------------

def main():
    ask_question()
    print(f'Your final score is {score}/10')
    


if __name__ == "__main__":
    main()

