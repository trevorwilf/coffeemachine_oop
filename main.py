from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

from coffee_maker import CoffeeMaker
from menu import MenuItem, Menu
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
coffee_menu = Menu()
coffee_money = MoneyMachine()


serving_customers = True

coffee_menu.get_items()

while serving_customers:
    options = coffee_menu.get_items()
    my_drink = ""

    my_drink = coffee_menu.find_drink(input(print(f"What would you like to drink {options}: ")))

    if (isinstance(my_drink, MenuItem)):
        #check the resources
        if coffee_machine.is_resource_sufficient(my_drink):
            # process money
            if coffee_money.make_payment(my_drink.cost):
                coffee_machine.make_coffee(my_drink)
        else:
            print("Not enough resources, please service the machine")



    turnoff = input("Would you like to turn off the machine (y/n): ")
    if (turnoff == 'y'):
        serving_customers = False

    printreports = input("Would you like to print the reports (y/n): ")
    if (printreports == 'y'):
        coffee_machine.report()
        coffee_money.report()
