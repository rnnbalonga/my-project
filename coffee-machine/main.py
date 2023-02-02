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

ingredients = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def main():

    #Print user prompts and capture user input. 
    drink = get_input()

    
    #Create a Report if user asks for one.
    if drink == "report":
        report()
        main()
    else:

        #Check if there are enough ingredients to create a drink.
        can_make_drink = check_ingredients(drink)

        if can_make_drink:            
            drink_cost = MENU[drink]['cost']
            amount_paid = get_coins(drink)

            while amount_paid < drink_cost:
                print (f"Sorry, insufficient amount. Please pay ${drink_cost - amount_paid} more.")
                if input("Do you want to continue with your order? (Type y/n): ").lower() == 'y':    
                    additional_payment = add_coins(drink, amount_paid)
                    amount_paid += additional_payment
                    check_coins(amount_paid, drink)
                else:
                    main()
            
            add_profit(amount_paid)
            

            if amount_paid > drink_cost:
                change = round(give_change(drink_cost, amount_paid),2)

                print(f"Your change is ${change}")
            

            make_drink(drink)
            print("Enjoy your drink!")
            main()
        else:
            if input("Do you want to continue with your order? (Type y/n): ").lower() == 'y':
                main()
            else:
                main()

def get_input():
    """
    This function will collect the user's input: either a drink or a report. Will return the value of the 'user_input'.
    """
    print("Welcome to Nike's Coffee Machine! What would you like to have? Espresso, Latte, or Cuppaccino?")
    print("(You can also print a report by typing 'report')")
    user_input = input("Type Here (E, L, or C): ").lower()
    
    if user_input == "e":
        return "espresso"
    elif user_input == "l":
        return "latte"
    elif user_input == "c":
        return "cappuccino"
    elif user_input == "report":
        return "report"

def report():
    """
    If user_input is 'report' print the amount of remaining ingredients
    """
    print(f"Remaining water: {ingredients['water']}")
    print(f"Remaining coffee: {ingredients['coffee']}") 
    print(f"Remaining milk is: {ingredients['milk']}")
    print(f"Profit: ${ingredients['money']}")
   

def check_ingredients(drink):
    """
    If user selects one of the drinks (espresso, latte, or cappuccino), this function will trigger. This function will check if there are enough ingredients to create drink. 
    Returns True or False.
    """

    #Update Value of ingredients
    current_water = ingredients["water"]
    current_coffee = ingredients["coffee"]
    current_milk = ingredients["milk"]


    #Gets the required ingredients from the dictionary MENU
    need_water = MENU[drink]['ingredients']['water']
    need_coffee = MENU[drink]['ingredients']['coffee']

    #For Espresso's missing milk ingredient
    if 'milk' in MENU[drink]['ingredients']:
        need_milk = MENU[drink]['ingredients']['milk']
    else:
        need_milk = 0

    
    if current_water > need_water and current_milk > need_milk and current_coffee > need_coffee:
        
        return True
    else:
        if current_water < need_water:
            print("Sorry, not enough water.")
        elif current_milk < need_milk:
            print("Sorry, not enough milk.")
        elif current_coffee < need_coffee:
            print("Sorry, not enough coffee.")
        return False   

def make_drink(drink):
    """
    Will update the values of the 'ingredients' dictionary if can_make_drink == True AND amount paid is enough.
    """

    #Update Value of ingredients
    current_water = ingredients["water"]
    current_coffee = ingredients["coffee"]
    current_milk = ingredients["milk"]

    #Gets the required ingredients from the dictionary MENU
    need_water = MENU[drink]['ingredients']['water']
    need_coffee = MENU[drink]['ingredients']['coffee']

    #For Espresso's missing milk ingredient
    if 'milk' in MENU[drink]['ingredients']:
        need_milk = MENU[drink]['ingredients']['milk']
    else:
        need_milk = 0

    ingredients['water'] = current_water - need_water
    ingredients['coffee'] = current_coffee - need_coffee
    ingredients['milk'] = current_milk - need_milk

    return


def get_coins(drink):
    """
    This function gets the coins inserted by the user. Will only run if variable 'can_make_drink' is == TRUE. Returns the total amount of user's given coins.
    """
    print(f"A {drink} costs ${MENU[drink]['cost']}.")
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * .25
    dimes = int(input("How many dimes?: ")) * .1
    nickels = int(input("How many nickels?: ")) * .05
    pennies = int(input("How many pennies?: ")) * .01

    total_payment = round(quarters + dimes + nickels + pennies, 2)

    return total_payment

def add_coins(drink, amount_paid):
    """
    This function gets the coins inserted by the user and will add to the sum of total_payment.
    """
    #Not optimal imo but easiest to execute.

    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * .25
    dimes = int(input("How many dimes?: ")) * .1
    nickels = int(input("How many nickels?: ")) * .05
    pennies = int(input("How many pennies?: ")) * .01

    additional_payment = round(quarters + dimes + nickels + pennies, 2)
    new_total_payment = amount_paid + additional_payment

    print(f"add_coins = {new_total_payment}")

    return additional_payment

def check_coins(amount_paid, drink): 
    """
    Checks whether the customer's payment is enough to buy the drink. Returns TRUE or FALSE.
    """
    drink_cost = MENU[drink]['cost']

    if amount_paid >= drink_cost:
        return True
    else:
        add_more_coins = drink_cost - amount_paid
        return False

def add_profit(amount_paid):
    """
    This function will add the payment made by the user to the profit in the 'ingredients' dictionary. 
    """
    profit = amount_paid
    ingredients['money'] += profit

    return 

def give_change(drink_cost, amount_paid):
    change = amount_paid - drink_cost

    return change
        


main()


    