MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

machine_on = True
def report():
    """"function to print a report"""
    remaining_resources_water = resources['water']
    print(f"Water: {remaining_resources_water} ml")
    remaining_resources_milk = resources['milk']
    print(f"Milk: {remaining_resources_milk} ml")
    remaining_resources_coffee = resources['coffee']
    print(f"Coffee: {remaining_resources_coffee} ml")
    remaining_resources_money = resources['money']
    print(f"Money: $ {remaining_resources_money}")

def drink_choice():
    """"function to check user's choice + allow to turn off + repair the coffee machine"""
    client_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if client_choice in ['espresso', 'latte', 'cappuccino', 'off', 'report']:
        return client_choice
    else:
        print("Invalid choice. Please choose again.")
        return drink_choice()

def remaining_resources(client_choice):
    """"function to check remaining resources"""
    drink_ingredients = MENU[client_choice]['ingredients']
    for ingredient, required_amount in drink_ingredients.items():
        if required_amount > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        return True

    remaining_resources()
# # TODO 5. Create a function to process coins

def process_coins():
    """"function to process coins"""
    print("Please insert coins.")
    the_amount_of_quarters = int(input("how many quarters?: "))
    the_amount_of_dimes = int(input("how many dimes?: "))
    the_amount_of_nickles = int(input("how many nickles?: "))
    the_amount_of_pennies = int(input("how many pennies?: "))
    the_amount_which_client_paid = round(0.25 *(the_amount_of_quarters)+ 0.1 * (the_amount_of_dimes)+ 0.05 * (the_amount_of_nickles) + 0.01 * (the_amount_of_pennies))
    return the_amount_which_client_paid

def check_the_transaction(drink, amount_paid):
    """"function to check whether transaction is successful"""
    cost_of_the_drink = MENU[drink]['cost']
    if cost_of_the_drink >  amount_paid:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif cost_of_the_drink <= amount_paid:
        change_from_the_transaction = amount_paid - cost_of_the_drink
        print(f"Here is ${change_from_the_transaction} in change.")
        resources['money'] += cost_of_the_drink
        return True
def make_a_coffee(drink, amount_paid):
    ingredients = MENU[drink]['ingredients']
    for ingredient, amount in ingredients.items():
        resources[ingredient] -= amount
    print(f"Here is your {drink}. Enjoy!")


while machine_on:
    choice = drink_choice()  # Klient dokonuje wyboru
    if choice == 'off':
        print("The system is off - now you can repair the machine")
        machine_on = False
    elif choice == 'report':
        report()
    else:
        enough_resources = remaining_resources(choice)
        if enough_resources:
            payment = process_coins()
            transaction_successful = check_the_transaction(choice,payment)
            if transaction_successful:
                make_a_coffee(choice, payment)

