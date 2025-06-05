import random


# yes or no checker.

def yes_or_no(question):
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


# The instructions for the game

def The_instructions():
    print(""" 
➕✖️➖ Instructions ➕✖️➖

Tell me what type of math question you want
+ for addition
- for subtraction
and x for multiplication
and i will print out one for you

you can finish by typing "done"
and see how well you did

Good Luck!!

    """)


# Ask the user if they want instructions or not
want_instructions = yes_or_no("Do you want instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    The_instructions()


# The addition question generator
def add():
    FirstNum = random.randint(9, 50)
    SecondNum = random.randint(9, 99)
    print(f"Question {numberRounds}")
    right_answer = int(input(f"What's {FirstNum} + {SecondNum}? "))
    if right_answer == FirstNum + SecondNum:
        return True
    else:
        return False


# The multiplication question generator
def multiply():
    FirstNum = random.randint(1, 25)
    SecondNum = random.randint(1, 10)
    print(f"Question {numberRounds}")
    right_answer = int(input(f"What's {FirstNum} x {SecondNum}? "))
    if right_answer == FirstNum * SecondNum:
        return True
    else:
        return False


# The subtraction question generator
def subtract():
    FirstNum = random.randint(10, 100)
    SecondNum = random.randint(5, FirstNum)
    print(f"Question {numberRounds}")
    right_answer = int(input(f"What's {FirstNum} - {SecondNum}? "))
    if right_answer == FirstNum - SecondNum:
        return True
    else:
        return False


playerScore = 0
numberRounds = 1

while True:

    # Ask user what kind of math question they want
    userInput = input("What kind of math question do want: ")
    print()

    if userInput == "+":
        if add():
            print("Your right")
            print()
            playerScore += 1
        else:
            print("You got it wrong its ")

        numberRounds += 1

    elif userInput == "-":
        if subtract():
            print("Your right")
            print()
            playerScore += 1
        else:
            print("You got it wrong")

        numberRounds += 1

    elif userInput == "x":
        if multiply():
            print("Your right")
            print()
            playerScore += 1
        else:
            print("You got it wrong")

        numberRounds += 1
    # Exit code for user
    # Also displays how much the user got right
    elif userInput == "done":
        print(f"You got {playerScore} out of {numberRounds} questions")
        print("Thanks for playing!!")
        break
