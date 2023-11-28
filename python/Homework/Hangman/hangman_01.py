import random
import Hangman_grafics

def check(error , word_choice , letter, botom_line):
    for i in range(0, len(word_choice)):
        if letter == word_choice[i] and botom_line[i] == "_":
            botom_line[i] = letter
            break


words_game = ["apple", "peach", "melon", "lemon", "strawberry", "banana", "plum", "olive", "date"]
hangman_grafics_level = [Hangman_grafics.hangman_1, Hangman_grafics.hangman_2,Hangman_grafics.hangman_3,Hangman_grafics.hangman_4,Hangman_grafics.hangman_5,Hangman_grafics.hangman_6, Hangman_grafics.hangman_7]
error = 0

word_choice = list(random.choice(words_game))
bottom_line = list("_" * len(word_choice))

print(Hangman_grafics.logo)

while error < 6 and bottom_line != word_choice:
    letter = input("Enter a letter: ")
    if letter not in word_choice or bottom_line.count(letter) == word_choice.count(letter):
        error += 1
        print(hangman_grafics_level[error])
    else:
        check(error , word_choice, letter, bottom_line)
    print(bottom_line)

if bottom_line == word_choice:
    print(Hangman_grafics.you_won)
else:
    print(Hangman_grafics.game_over)







