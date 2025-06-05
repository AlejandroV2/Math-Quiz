import random







ur_score = 0

for x in range(10):
    num1 = random.randint(1, 23)
    num2 = random.randint(9, 15)
    print("what is",num1, "x",num2,"=")
    you_answer = int(input(""))
    answer = num1 * num2
    if you_answer == answer:
        print("ok lol")
        ur_score +=1
    else:
        print("KeYS")
        num1 = random.randint(1, 23)
        num2 = random.randint(11, 99)
        print("what is",num1, "+",num2,"=")
        you_answer = int(input(""))
        answer = num1 + num2
        if you_answer == answer:
            print("ok lol")
            ur_score +=1
        else:
            print("KeYS")

print(f"You got {ur_score} right")
