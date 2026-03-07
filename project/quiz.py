# Module
def get_questions():
    return [
        ["What is the capital of France?", "paris"],
        ["What is 12 x 12?", "144"],
        ["What programming language is this quiz written in?", "python"],
        ["What nutrient helps with building muscle?", "protein"],
        ["How many months have 28 days?", "12"]
    ]

def check_answers(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True
    else:
        return False

def get_result(score, total):
    if score == total:
        return "Perfect score! Keep up the great work!"
    elif score == 4:
        return "Amazing job! Keep grinding!"
    elif score == 3:
        return "Great effort! Keep learning!"
    elif score <= 2:
        return "Good job, time to lock in!"

def sign_off(name, score, total):
    return "Thanks for playing " + name + ". You scored " + str(score) + " out of " + str(total) + "!"

# Main code
import quiz

def user_quiz(name):
    print()
    score = 0
    questions = quiz.get_questions()
    total = len(questions)
    for question in questions:
        user_answer = input(question[0] + "\n > ").lower()
        correct_answer = question[1]
        
        if quiz.check_answers(user_answer, correct_answer):
            score += 1
            print("Correct!")
        else:
            print("Wrong! The correct answer was " + str(correct_answer) + ".")
            
    print("\n" + quiz.get_result(score, total))            
    print(quiz.sign_off(name, score, total))
        
name = input("Welcome to the General Knowledge Quiz! \nEnter your name to get started: ")
while name == "":
    name = input("Make sure to enter your name: ")

user_quiz(name)
