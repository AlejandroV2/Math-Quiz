game_list = f"You put {userInput}. The answer is {right_answer}"
game_history = f"Round: {numberRounds} - {game_list}"

history_check = yes_or_no("\nDo you want to see your game history")
if history_check == "yes":
    for item in game_history: