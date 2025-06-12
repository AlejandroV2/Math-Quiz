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
def int_check(to_check):
    while True:
        error = "Please enter an integer that is 1 or more."

        # check for infinite mode
        if to_check == "":
            return "infinite"
        try:
            response = int(to_check)

            # checks that the number is more than / equal to 13
            if response < 1:
                # print(error)
                return "invalid"
            else:
                return response

        except ValueError:
            print(error)


def The_instructions():
    print(""" 
➕✖️➖ Instructions ➕✖️➖

Tell me what type of math question you want
+ for addition
- for subtraction
and x for multiplication
and i will print out one for you

you can press enter to pick infinite mode 
and answer as many questions you want
you can finish by typing "done"
and see how well you did

Good Luck!!

    """)


# Ask the user if they want instructions or not.
want_instructions = yes_or_no("Do you want instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    The_instructions()

# Asks how many questions the user wants.
while True:
    num_input = input("How many questions do you want to answer? ")
    if num_input == "":  # What the user needs to type for infinite.
        print("You chose infinite mode")
        total_questions = float('inf')  # Infinite mode enabled
        break
    try:
        total_questions = int(num_input)
        if total_questions > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Please enter a valid integer.")

# Questions history list
question_history = []


# The addition question generator
def add():
    firstNum = random.randint(9, 50)
    SecondNum = random.randint(9, 99)
    print(f"Question {numberRounds}")
    while True:
        try:
            right_answer = int(input(f"What's {firstNum} + {SecondNum}? "))
            break
        except ValueError:
            print("Please enter a valid number.")
    correct_answer = (right_answer == firstNum + SecondNum)
    # Saves to history
    question_history.append((f"{firstNum} + {SecondNum}", right_answer, firstNum + SecondNum, correct_answer))
    return correct_answer


# The multiplication question generator
def multiply():
    FirstNum = random.randint(1, 25)
    SecondNum = random.randint(1, 10)
    print(f"Question {numberRounds}")
    while True:
        try:
            right_answer = int(input(f"What's {FirstNum} x {SecondNum}? "))
            break
        except ValueError:
            print("Please enter a valid number.")
    correct_answer = (right_answer == FirstNum * SecondNum)
    # Saves to history
    question_history.append((f"{FirstNum} x {SecondNum}", right_answer, FirstNum * SecondNum, correct_answer))
    return correct_answer


# The subtraction question generator
def subtract():
    FirstNum = random.randint(10, 100)
    SecondNum = random.randint(5, FirstNum)
    print(f"Question {numberRounds}")
    while True:
        try:
            right_answer = int(input(f"What's {FirstNum} - {SecondNum}? "))
            break
        except ValueError:
            print("Please enter a valid number.")
    correct_answer = (right_answer == FirstNum - SecondNum)
    # Saves to history
    question_history.append((f"{FirstNum} - {SecondNum}", right_answer, FirstNum - SecondNum, correct_answer))
    return correct_answer


playerScore = 0
numberRounds = 1
questions_answered = 0
while True:

    # Stop if user reaches max questions <<<
    if questions_answered >= total_questions:
        print("You've reached the maximum number of questions.")
        userInput = "done"
    else:
        userInput = input("What kind of question do want (type 'done' to finish): ")
        print()

    # What the user needs to type to get the question they want
    if userInput == "+":
        # Tell the user whether they got it right or wrong
        if add():
            print("Good job! You got it right. ")
            print()
            playerScore += 1
        else:
            print("Sorry! You got it wrong. ")

        numberRounds += 1
        questions_answered += 1
    # What the user needs to type to get the question they want
    elif userInput == "-":
        # Tell the user whether they got it right or wrong
        if subtract():
            print("Good job! You got it right. ")
            print()
            playerScore += 1
        else:
            print("Sorry! You got it wrong. ")

        numberRounds += 1
        questions_answered += 1
    # What the user needs to type to get the question they want
    elif userInput == "x":
        # Tell the user whether they got it right or wrong
        if multiply():
            print("Good job! You got it right. ")
            print()
            playerScore += 1
        else:
            print("Sorry! You got it wrong. ")
            print()
        numberRounds += 1
        questions_answered += 1
    # Exit code for user

    # Also displays how much the user got right
    elif userInput == "done":
        print(f"You got {playerScore} out of {numberRounds - 1} questions")
        # Ask user whether they want to see the history
        if yes_or_no("Do you want to see your question history? ") == "yes":
            print("\n🤑🤑Questions history🤑🤑:")
            for i, (q, user_ans, correct_ans, result) in enumerate(question_history, 1):
                outcome = "🤑Correct🤑" if result else "🤣Incorrect🤣"
                print(f"{i}. {q} = {correct_ans} | You: {user_ans} → {outcome}")
        print("Thanks for playing!!")
        break


    else:
        print("Invalid input. Please enter +, -, x, or 'done'.")