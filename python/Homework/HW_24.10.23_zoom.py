import math


# פונקציה המקבלת 3 מספרים ומחזירה את מכפלתם
def molti_num(x,y,z):
    print(x * y * z)

# פונקציה שמקבלת שני קלטים 1 של שם פרטי ושני של שם משפחה ומחזירה שם מלא
def full_name():
    first_name = input("Write your first name: ")
    family_name = input("Write your family name: ")
    print(f"your full name is: {first_name} {family_name}.")

# פונקציה שמקבלת כקלט 3 מספרים ומדפדפיסה את הגדול
def biggest_num(x,y,z):
    print(max(x,y,z))

# פונקציה המקבלת 3 שמות ומחזירה את השם הארוך ביותר
def long_name(name1, name2 , name3):
    if len(name1) > len(name2) and len(name1) > len(name3):
        print(name1)
    elif len(name2) > len(name3):
        print(name2)
    else:
        print(f"the longest name is \"{name3}\".")

# פונקציה שמקבלת מספר מהמשתמש ומדפיסה לו האם זה זוגי או לא זוגי
def even_or_odd(x):
    if x % 2 == 0:
        print(f"The number {x} is even.")
    else:
        print(f"The number {x} is odd.")

# פונקציית מחשבון לחישוב שטח מעגל לפי רדיוס
def circle_eara(x):
    print(f"The eara of the circle is {(x ** 2) * math.pi}.")
