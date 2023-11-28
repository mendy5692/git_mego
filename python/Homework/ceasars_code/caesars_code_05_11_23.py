import ceasars_code_grafics

def chr_to_ord(word , gump):
    finale_word = ''
    for i in word:
        if ord(i) + gump > 122:
            finale_word += chr(ord(i) + gump - 26)
        else:
            finale_word += chr(ord(i) + gump)
    return finale_word

def ord_to_chr(word , gump):
    finale_word = ''
    for i in word:
        if ord(i) - gump < 97:
            finale_word += chr(ord(i) - gump + 26)
        else:
            finale_word += chr(ord(i) - gump)
    return finale_word


to_continue = "y"

print(ceasars_code_grafics.logo)

while to_continue[0].lower() == "y":

    action = input("\nwhat do you want to do?\nEncrypt content (a)\nLooking for content (b)\n")
    word = str(input("Enter a word: "))
    gump = int(input("How many skips do you want to skip? "))

    if action.lower() == "a":
        print(chr_to_ord(word.lower(), gump))
    elif action.lower() == "b":
        print(ord_to_chr(word.lower(), gump))
    else:
        print("You chose the wrong action!\n")

    to_continue = input("Do you want to continue for another word? (Yes/No) ")

print("\nYou chose to end the program!")








