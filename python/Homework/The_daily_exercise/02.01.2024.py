def string_check():
    counter = 0
    string = ""
    while string != "z":
        string = input("Enter a string: ").lower()
        if string[0] == string[-1] == "x":
            counter += 1
    return counter

print(string_check())