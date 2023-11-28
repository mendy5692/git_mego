import random
import guessing_game_grafics
def level():
    level_choice = input("Do you want to play on hard or easy level? (hard/easy) ").lower()
    if level_choice[0] == "h":
        return 5
    elif level_choice[0] == 'e':
        return 10
    else:
        print("The difficulty level you selected is incorrect.")

def guessing_check(num_choice):
    for i in range(level()-1,-1,-1):
        num_guess = int(input("\nEnter a number: "))
        if num_guess < num_choice:
            print(f"Wrong answer!\n{guessing_game_grafics.crying_face}\nthe number you entered is less than the number drawn.\nYou have {i} attempts left")
        elif num_guess > num_choice:
            print(f"Wrong answer!\n{guessing_game_grafics.crying_face}\nthe number you entered is greater than the number drawn.\nYou have {i} attempts left")
        else:
            print(f"you won!!\nCorrect answer!\n{guessing_game_grafics.laughing_face}\nthe number you entered is the number drawn!!!")
            break
        if i == 0:
            print(f"\ngame over!\nYou couldn't guess the number. The number drawn is: {num_choice}")

print(guessing_game_grafics.logo)
guessing_check(random.randint(0,100))


