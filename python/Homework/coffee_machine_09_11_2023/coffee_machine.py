import coffee_machine_menu
import coffee_machine_grafics

# הגדרת פונקציה שתחזיר את סוג המשקה הנבחר
def tipe_drink():
    a = "m"
    while a[0] != "e" and a[0] != "l" and a[0] != "c":
        a = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
        if a[0] == "e":
            return "espresso"
        elif a[0] == "l":
            return "latte"
        elif a[0] == "c":
            return "cappuccino"
        elif a == "1234":
            return "technician"
        elif a == "off":
            print("off")
        else:
            print("error")

# הגדרת פונקצית - ניהול דוח/מילוי
def technician(tipe_drink_choice):
    if tipe_drink_choice == "technician":
        b = input("\nwhat do you want to do ?\nPrint a report. (report)\nto fill inventory. (fill)").lower()
        if b[0] == "r":
            print(coffee_machine_menu.resources)
        elif b[0] == "f":
            print(coffee_machine_menu.resources)
            coffee_machine_menu.resources["water"] += int(input("How much water do you want to add? "))
            coffee_machine_menu.resources["milk"] += int(input("How much milk do you want to add? "))
            coffee_machine_menu.resources["coffee"] += int(input("How much coffee do you want to add? "))
            print(coffee_machine_menu.resources)
        else:
            print("error")

#(אין צורך להפעיל עצמאית) -  הגדרת פונקציה שתחזיר את רכיבי המשקה שנבחר
def component(tipe_drink_choice):
    if tipe_drink_choice == "espresso":
        return coffee_machine_menu.MENU["espresso"]["ingredients"]
    elif tipe_drink_choice == "latte":
        return coffee_machine_menu.MENU["latte"]["ingredients"]
    elif tipe_drink_choice == "cappuccino":
        return coffee_machine_menu.MENU["cappuccino"]["ingredients"]

# פונקציית ניקוי רכיבים מהמלאי - (אין צורך להפעיל עצמאית)
def component_status():
    coffee_machine_menu.resources["water"] -= component(tipe_drink_choice)["water"]
    coffee_machine_menu.resources["milk"] -= component(tipe_drink_choice)["milk"]
    coffee_machine_menu.resources["coffee"] -= component(tipe_drink_choice)["coffee"]

# פונקצית בדיקה האם הרכיבים קיימים במלאי או לא ובכך לקבוע האם לאפשר הכנת משקה - (אין צורך להפעיל עצמאית)
def available(tipe_drink_choice):
    if coffee_machine_menu.resources["water"] < component(tipe_drink_choice)["water"]:
        result = "Sorry, not enough water."
    if coffee_machine_menu.resources["milk"] < component(tipe_drink_choice)["milk"]:
        result = "Sorry, not enough milk."
    if coffee_machine_menu.resources["coffee"] < component(tipe_drink_choice)["coffee"]:
        result = "Sorry, not enough coffee."
    if coffee_machine_menu.resources["coffee"] >= component(tipe_drink_choice)["coffee"] and coffee_machine_menu.resources["milk"] >= component(tipe_drink_choice)["milk"] and coffee_machine_menu.resources["water"] >= component(tipe_drink_choice)["water"]:
        result = "available"
    return result

# פונקצית הכנסת כסף ועדכון כמה ואיזה כסף קיימים - (אין צורך להפעיל עצמאית)
def get_payment(drink_type_choice):
    if available(drink_type_choice) == "available":
        more_money = "y"
        money = 0
        while more_money == "y":
            currency = input("What currency do you want to add? (penny/nickel/dime/quadr/dollar) ")
            if currency == "penny":
                coffee_machine_menu.money_have["penny"] += coffee_machine_menu.money["penny"]
                money += coffee_machine_menu.money["penny"]
            elif currency == "nickel":
                coffee_machine_menu.money_have["nickel"] +=  coffee_machine_menu.money["nickel"]
                money += coffee_machine_menu.money["nickel"]
            elif currency == "dime":
                coffee_machine_menu.money_have["dime"] +=  coffee_machine_menu.money["dime"]
                money += coffee_machine_menu.money["dime"]
            elif currency == "quadr":
                coffee_machine_menu.money_have["quadr"] +=  coffee_machine_menu.money["quadr"]
                money += coffee_machine_menu.money["quadr"]
            elif currency == "dollar":
                coffee_machine_menu.money_have["dollar"] +=  coffee_machine_menu.money["dollar"]
                money += coffee_machine_menu.money["dollar"]
            else:
                print("Sorry, the machine does not accept this type of currency.")
            more_money = input("Do you want to put in more money? (yes/no) ").lower()
        return money
    else:
        return available(drink_type_choice)

#הגדרת פונקציה שתחזיר את מחיר המשקה שנבחר - (אין צורך להפעיל עצמאית)
def costs(tipe_drink_choice):
    if tipe_drink_choice == "espresso":
        return coffee_machine_menu.MENU["espresso"]["cost"]
    elif tipe_drink_choice == "latte":
        return coffee_machine_menu.MENU["latte"]["cost"]
    elif tipe_drink_choice == "cappuccino":
        return coffee_machine_menu.MENU["cappuccino"]["cost"]

# פונקציה לחישוב כמות הכסף שהכניס לעומת מחיר המשקה והחזרת עודף במקרה הצורך
def payment_and_excess(tipe_drink_choice):
    excess = 0
    if money > costs(tipe_drink_choice):
        coffee_machine_menu.resources["money"] += costs(tipe_drink_choice)
        excess = "{:.2f}".format(money - costs(tipe_drink_choice))
        component_status()
        print(f"Your excess is {excess}\nYour drink is ready!!!\n{coffee_machine_grafics.Cup}")
    elif money < costs(tipe_drink_choice):
        print("You don't have enough money to buy the drink you chose, Take your money back.")
    else:
        coffee_machine_menu.resources["money"] += costs(tipe_drink_choice)
        component_status()
        print(f"Your drink is ready!!!\n{coffee_machine_grafics.Cup}")


while True:
    tipe_drink_choice = tipe_drink()
    technician(tipe_drink_choice)
    if tipe_drink_choice != "technician":
        money = get_payment(tipe_drink_choice)
        payment_and_excess(tipe_drink_choice)
