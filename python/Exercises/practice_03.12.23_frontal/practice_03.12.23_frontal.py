'''
r - reading
w - writing
r+ - read & write
w+ - writing, creates a new file if doesn't exist
a - writing, appending, creates ...
a+ - read, write, append, creates ...
x - created only if does not exist, writing
    "exclusive creation"
'''

# זה יתחיל לקרוא מהיכן שהסמן נמצא ולכן אם שינינו קובץ בשביל לקרוא לו צריך לקרוא לו מחדש

#Hi mendy!

'''
    contents = file.read()
    print(contents)
    file.write("And your name is ... what?")

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
    
'''


def divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        print("Don't divide by 0 pleaseeee! !!! ")
    # print("Something went wrong ... ")
    except TypeError as err:
        print("a and b must both be either ints or floats!")
        print(err)

print(divide(1, 2))  # 0.5
print(divide(1, 0))  # will print None because we returned None (skipped Ln3)
print(divide('a', 2))
