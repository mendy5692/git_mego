import os

answer = "Y"
highest_price = 0
buyer = ""

name = input("Enter your name: ")
price = int(input("Enter your price: "))

while answer[0] == "Y":
    question = input("Is there another person? (yes/no)")
    answer = question.upper()
    os.system('cls' if os.name == 'nt' else 'clear')
    if answer[0] == "Y":
        name = input("Enter your name: ")
        price = int(input("Enter your price: "))
        if price > highest_price:
            highest_price = price
            buyer = name
    else:
        break

print(f"Buyer \"{buyer}\" is the winner of the item in the amount of \"{highest_price}\" shekels.")