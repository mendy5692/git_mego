import calculator_grafics

def addition(a,b):
    return a + b

def subtraction(a,b):
    return  a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    if b != 0:
        return a / b
    else:
        return "It is impossible to divide by 0"

def calculat(a,b,c):
    if c == "a" or c == "s" or c == "m" or c == "d":
        if c == "a":
            return addition(a,b)
        elif c == "s":
            return subtraction(a,b)
        elif c == "m":
            return multiplication(a,b)
        else:
            return division(a,b)
    else:
        return "You have selected an incorrect action."


print(calculator_grafics.calculator)

num_a = float(input("Enter a number: "))
action = input("What action do you want to take?\nAddition (a)\nSubtraction (s)\nMultiplication (m)\nDivision (d)\n")
num_b = float(input("Enter a second number: "))

print(f"\nThe result is: {calculat( num_a , num_b , action.lower() )}")



#print(addition(3,5))
