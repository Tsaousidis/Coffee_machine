
from Coffee_variables import *

resources['money'] = 0
machine_off = False

def calculate_coins(quar, dim, nick, pen):
    return quar * 0.25 + dim * 0.1 + nick * 0.05 + pen * 0.01

def enough_resources(drink):
    missing_ingredients = []
    for ingredient, amount in MENU[drink]['ingredients'].items():
        if amount > resources.get(ingredient, 0):
            missing_ingredients.append(ingredient)
    if missing_ingredients:
        return f"Sorry, there is not enough {' and '.join(missing_ingredients)}."
    return True

def manipulate_resources(beverage):
    resources['money'] += MENU[beverage]['cost']
    resources['water'] -= MENU[beverage]['ingredients']['water']
    resources['coffee'] -= MENU[beverage]['ingredients']['coffee']
    if beverage != "espresso":
        resources['milk'] -= MENU[beverage]['ingredients']['milk']


while not machine_off:
    # Prompt user by asking what he wants
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    if drink == "off":
        machine_off = True
        print("Goodbye!")
    elif drink == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")
    elif drink in MENU.keys():    
        are_enough_resources = enough_resources(drink)
        if not are_enough_resources:
            print(are_enough_resources)
        else:    
            print("Please insert coins")
            while True:  # Loop until valid input is entered
                try:
                    quarter = int(input("How many quarters?: "))
                    dime = int(input("How many dimes?: "))
                    nickel = int(input("How many nickels?: "))
                    penny = int(input("How many pennies?: "))
                    
                    # Check if the input is negative
                    if quarter < 0 or dime < 0 or nickel < 0 or penny < 0:
                        print("Please enter non-negative numbers.")
                        continue  # Loop again to ask for input
                    
                    break  # Exit the loop if all inputs are valid
                    
                except ValueError:
                    print("Please enter valid numbers for coins.")

            money_inserted = calculate_coins(quarter, dime, nickel, penny)
            if money_inserted < MENU[drink]['cost']:
                print("Sorry that's not enough money. Money refunded.")
            elif money_inserted > MENU[drink]['cost']:
                money_refunded = money_inserted - MENU[drink]['cost']
                print(f"Here is ${money_refunded:.2f} in change.")
                print(f"Here is your {drink}. Enjoy!")
                manipulate_resources(drink)
            else:
                print(f"Here is your {drink}. Enjoy!")
                manipulate_resources(drink)