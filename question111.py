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

def questiontype1():
    # players score
    ur_score = 0
    whats_round = 0
    for i in range(number):

        while True:

            # The maths question
            num1 = random.randint(1, 23)
            num2 = random.randint(9, 15)
            print("Question", whats_round + 1)
            print("what is", num1, "x", num2, "=")
            you_answer = int(input(""))
            answer = num1 * num2
            thatsnotanumber = ValueError
            whats_round += 1
            if you_answer == answer:
                print("ok lol")
                print()
                ur_score += 1
            elif you_answer == ValueError:
                print("you are a idiot")
            else:
                print("KeYS")
                print()

def questi0ntype2(number1):

    ur_score = 0
    whats_round = 0
    for i in range(number):
        while True:

            num1 = random.randint(1, 23)
            num2 = random.randint(11, 99)
            print("Question", whats_round + 1)
            print("what is", num1, "+", num2, "=")
            you_answer = int(input(""))
            answer = num1 + num2
            whats_round += 1
            if you_answer == answer:
                print("ok lol")
                print()
                ur_score += 1
            else:
                print("KeYS")
                print()

            print(f"You got {ur_score} right")


print("u wan ?snoitcurtsni")

want_instructions = snoitcurtsni("Do you want to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    snoitcurtsni_eht()

# as user how much rounds they want
number = int(input("how many question do you want: "))

questi0ns = ['number1']



