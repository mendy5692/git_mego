import random
import Hangman_grafics

print(Hangman_grafics.logo)


error = 0
words_game = ["apple", "peach", "melon", "lemon", "strawberry", "banana", "plum", "olive", "date"]
hangman_grafics_level = [Hangman_grafics.hangman_1, Hangman_grafics.hangman_2,Hangman_grafics.hangman_3,Hangman_grafics.hangman_4,Hangman_grafics.hangman_5,Hangman_grafics.hangman_6, Hangman_grafics.hangman_7]

word_choice = random.choice(words_game)
bottom_line = "_" * len(word_choice)
print(word_choice)

while "_" in bottom_line and error < 7:
    letter = input("Enter a letter: ")
    place = 0

    for i in word_choice:
        if letter == i:
            bottom_line = bottom_line[:place] + letter + bottom_line[place + 1:]

            break
        place += 1


    if bottom_line != bottom_line[:place] + letter + bottom_line[place + 1:]:
        print(hangman_grafics_level[error])
        error += 1
    print(bottom_line)



if error == 7:
    print(Hangman_grafics.game_over)
    print(f"The correct word was: {word_choice}")
if "_" not in bottom_line:
    print(Hangman_grafics.you_won)
    print(f"The word copper is: {word_choice}")






