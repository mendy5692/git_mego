from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    # הדפס רשימה של המשקאות הזמינים וקבל מהמשתנה בחירה = מחזיר את שם המשקה שנבחר וקיים במלאי
    drink_choice = input(f"which drink you are want? ({menu.get_items()})")

    # האם מה שהמשתמש הזין קיים במלאי = מחזיר את רכיבי המשקה
    drink_choice_sure = menu.find_drink(drink_choice)

    # בדיקה האם הרכיבים של המוצר קיימים במלאי = מחזיר אמת או שקר אם קיים או לא
    check_ingredients = coffee_maker.is_resource_sufficient(drink_choice_sure)

    # בדיקה האם הכסף שהתקבל גדול מהכסף שהמוצר עולה = מחזיר עודף ואמת או שקר האם יש מספיק או לא
    money_enough = money_machine.make_payment(drink_choice_sure.cost)

    # מחסיר מהרכיבים הקיימים במלאי את הרכיבים של המשקה שנבחר = ומחזיר/מדפיס "קח את הקפה!"
    coffee_maker.make_coffee(drink_choice_sure)





