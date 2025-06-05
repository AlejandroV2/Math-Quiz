import operator
import random


def snoitcurtsni(question):
    """Checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check the user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def snoitcurtsni_eht():

    print(""" 
    So basically
    
    i ask u questions
    
    and you answer them
    
    and try to get as much as u can
    """)

def question_type():
    operators = {
        '+': operator.add,
        '-': operator.sub,
        'x': operator.mul,
        '÷': operator.truediv
    }



want_instructions = snoitcurtsni("u wan ?snoitcurtsni")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    snoitcurtsni_eht()

# as user how much rounds they want
number = int(input("how many question do you want: "))


# players score
ur_score = 0
whats_round = 0
for i in range (number):



        # The maths question
        num1 = random.randint(1, 23)
        num2 = random.randint(9, 15)
        print("Question", whats_round + 1)
        print(f'What is {num1} {question_type} {num2}')
        you_answer = int(input(""))
        answer = num1, question_type, num2
        whats_round += 1
        if you_answer == answer:
            print("ok lol")
            print()
            ur_score += 1
        else:
            print("KeYS")
            print()
        

