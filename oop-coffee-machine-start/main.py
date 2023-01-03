from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    machine_on = True
    
    while machine_on:
        coffee = CoffeeMaker()
        menu = Menu()
        money = MoneyMachine()

        user_input = input(f"What drink would you like to have? {menu.get_items()} (Type 'report' to get a report) (OFF): ").lower()

        if user_input == "report":
            coffee.report()
            money.report()
        elif user_input == "off":
            machine_on = False
        else:
            order = menu.find_drink(user_input)
            cost = order.cost

            if coffee.is_resource_sufficient(order):
                if money.make_payment(cost):
                    coffee.make_coffee(order)

main()