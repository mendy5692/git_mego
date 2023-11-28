import random
import guessing_game_grafics

def examination(score , num_guess , num_choice):
    for i in range(score):
        num_guess = int(input("\nEnter a number: "))
        if num_guess < num_choice:
            print(f"Wrong answer!\n{guessing_game_grafics.crying_face}\nthe number you entered is less than the number drawn.\nYou have {score - i - 1} attempts left")
        elif num_guess > num_choice:
            print(f"Wrong answer!\n{guessing_game_grafics.crying_face}\nthe number you entered is greater than the number drawn.\nYou have {score - i - 1} attempts left")
        else:
            print(f"Correct answer!\n{guessing_game_grafics.laughing_face}\nthe number you entered is the number drawn!!!")
            break
        if i == score - 1:
            print(f"\ngame over!\nYou couldn't guess the number. The number drawn is: {num_choice}")

score = 1
num_guess = 0
num_choice = random.randint(1,100)
print(guessing_game_grafics.logo)
easy_or_hard = input("Do you want to play an easy or hard game? (easy/hard) ").lower()

if easy_or_hard == "e":
    score = 10
    examination(score , num_guess , num_choice)
elif easy_or_hard == "h":
    score = 5
    examination(score, num_guess , num_choice)
else:
     print("The difficulty level you entered is not available.")



















