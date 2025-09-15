import os
import json
import time


class Coffee:
    desktopPath = os.path.join(os.path.expanduser("~"))
    filePath = os.path.join(desktopPath, 'Coffee.json')

    if not os.path.exists(filePath):
        inventory = {
            'Water': 0,
            'Coffee': 0,
            'Milk': 0,
            'Sugar': 0,
            'Money': 0,
            'Cups': 0
        }
        with open(filePath, "w") as file:
            json.dump(inventory, file, indent=4)
    else:
        pass
    with open(filePath, "r") as f:
        inventories = json.load(f)
    liquid = ['Water', 'Milk']
    Menu = {1: 'Espresso', 2: 'Latte', 3: 'Capuccino', 4: 'Americano', 5: 'Mocha'}
    menu = {'Espresso': {'price': 1.80,
                         'Water': 60,
                         'Coffee': 8,
                         'Milk': 120,
                         'Sugar': 5},
            'Americano': {'price': 1.20,
                          'Water': 150,
                          'Coffee': 8,
                          'Milk': 0,
                          'Sugar': 5},
            'Latte': {'price': 1.80,
                      'Water': 60,
                      'Coffee': 8,
                      'Milk': 120,
                      'Sugar': 5},
            'Capuccino': {'price': 1.80,
                          'Water': 50,
                          'Coffee': 8,
                          'Milk': 80,
                          'Sugar': 5,
                          },
            'Mocha': {'price': 2.20,
                      'Water': 50,
                      'Coffee': 8,
                      'Milk': 120,
                      'Sugar': 15
                      }
            }
    got = True
    fill = {1: 'Water', 2: 'Coffee', 3: 'Milk', 4: 'Sugar', 5: 'Money', 6: 'Cups'}

    @staticmethod
    def top():
        menus = {'1. Espresso': 1.80,
                 '2. Latte': 1.80,
                 '3. Capuccino': 1.80,
                 '4. Americano': 1.20,
                 '5. Mocha': 2.20}
        print("-----------------------")
        print("Menu           : Prices")
        print("-----------------------")
        for key, value in menus.items():
            print(f"{key:<15}: ${value}")
        print("------------------------")
        print()

    @staticmethod
    def get():
        Coffee.top()
        name = int(input("What would you like (1-5): "))
        do = True

        if name not in Coffee.Menu.keys():
            print("Option out of bound")
            do = False
        if name in Coffee.Menu.keys():
            for key in Coffee.menu[Coffee.Menu[name]].keys():
                if key == 'price':
                    continue
                if Coffee.inventories[key] < Coffee.menu[Coffee.Menu[name]][key]:
                    print()
                    print("Sorry, Unable to make your coffee rn")
                    print("We're out of resources")
                    do = False
                    break
        while do:
            if name in Coffee.Menu.keys():

                print(f"Price : $ {Coffee.menu[Coffee.Menu[name]]['price']}")
                coin = float(input("Insert money to get coffee: "))
                if coin < Coffee.menu[Coffee.Menu[name]]['price']:
                    print("Insufficient Funds")
                    print(f"Take your $ {coin}")
                    break
                elif coin > Coffee.menu[Coffee.Menu[name]]['price']:
                    change = coin - Coffee.menu[Coffee.Menu[name]]['price']
                    print(f"Here's your change: $ {change:.2f}")
                Coffee.inventories['Money'] += Coffee.menu[Coffee.Menu[name]]['price']
                with open(Coffee.filePath, "w") as flop:
                    json.dump(Coffee.inventories, flop, indent=4)
                for key in Coffee.menu[Coffee.Menu[name]].keys():
                    if not key == 'Money' and not key == 'Cups' and not key == 'price':
                        Coffee.inventories[key] -= Coffee.menu[Coffee.Menu[name]][key]
                        with open(Coffee.filePath, "w") as flop:
                            json.dump(Coffee.inventories, flop, indent=4)
                    else:
                        continue
                Coffee.inventories['Cups'] -= 1
                with open(Coffee.filePath, "w") as flop:
                    json.dump(Coffee.inventories, flop, indent=4)
                print("Dispensing Coffee ", end="", flush=True)
                for i in range(5):
                    time.sleep(0.5)
                    print(".", end="", flush=True)
                print(" ☕")
                print("\nCoffe dispensed")
                print("Grab your coffe and have a nice day 😊")
                do = False


class Maintain(Coffee):
    pin = '12345'

    @staticmethod
    def off():
        print("Turning off Machine ", end="", flush=True)
        for i in range(7):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print(" 📴")
        print("\n")

    @staticmethod
    def refill():
        def sub():
            Coffee.inventories[Coffee.fill[ref]] += added
            with open(Coffee.filePath, "w") as fish:
                json.dump(Coffee.inventories, fish, indent=4)
            if not Coffee.fill[ref] == 'Cups' and not Coffee.fill[ref] == 'Money':
                return f"{added} {'ml' if Coffee.fill[ref] in Coffee.liquid else 'g'} of {Coffee.fill[ref]} was added to inventory"
            elif Coffee.fill[ref] == 'Money':
                return f"$ {added} was added to inventory"
            elif Coffee.fill[ref] == 'Cups':
                return f"{int(added)} cups was added to inventory"
        keys = list(Coffee.inventories.keys())
        print("-----------------------")
        print("Resources : Amount")
        print("-----------------------")
        for key in Coffee.inventories:
            if not key == 'Cups' and not key == 'Money':
                print(
                    f"{keys.index(key) + 1}. {key:<8}:   {Coffee.inventories[key]} {'ml' if key in Coffee.liquid else 'g'}")
            elif key == 'Money':
                print(f"{keys.index(key) + 1}. {key:<8}: $ {Coffee.inventories[key]} ")
            elif key == 'Cups':
                print(f"{keys.index(key) + 1}. {key:<8}:   {int(Coffee.inventories[key])} cups ")
        print()
        while True:

            ref = int(input("Which inventory would you like to refill(1-6): "))
            if ref not in Coffee.fill.keys():
                print(f"Inventory choice {ref} out of bound")
                break
            if ref in Coffee.fill.keys() and not Coffee.fill[ref] == 'Cups' and not Coffee.fill[ref] == 'Money':
                added = float(input(f"How many {'ml' if Coffee.fill[ref] in Coffee.liquid else 'g'} of {Coffee.fill[ref]} would you like to add to inventory: "))
                print("You can't add number below or equal to 0 of resources to inventory" if added <= 0 else sub())
            if Coffee.fill[ref] == 'Money':
                added = float(input(f"How much money would you like to add to inventory: "))
                print("You can't add no below or equal to 0 of resources to inventory" if added <= 0 else sub())
            elif Coffee.fill[ref] == 'Cups':
                added = int(input(f"How many cups would you like to add to inventory: "))
                print("You can't add no below or equal to 0 of resources to inventory" if added <= 0 else sub())
            jeff = input("Would you like to refill another inventory(yes/no): ")
            print()
            if not jeff == 'yes':
                break

    @staticmethod
    def check():
        print("-----------------------")
        print("Resources : Amount Left")
        print("-----------------------")
        for key, values in Coffee.inventories.items():
            if not key == 'Cups' and not key == 'Money':
                print(f"{key:<10}: {values} {'ml' if key in Coffee.liquid else 'g'}")
            elif key == 'Money':
                print(f"{key:<10}: $ {values}")
            else:
                print(f"{key:<10}: {values}")
        print("-----------------------")

    @staticmethod
    def withdraw():
        much = float(input("How much would you like to withdraw: "))
        if much > Coffee.inventories['Money']:
            print("Insufficient Funds")
        else:
            Coffee.inventories['Money'] -= much
            with open(Coffee.filePath, "w") as foil:
                json.dump(Coffee.inventories, foil, indent=4)
            print(f"$ {much} was withdrawn from inventory")

    @staticmethod
    def maintainOpt():
        passcode = input("Enter maintainer password: ")
        if passcode == Maintain.pin:
            print("---------------------")
            print("Maintainer Activities")
            print("---------------------")
            print("1. ON/OFF")
            print("2. Refill Stock")
            print("3. Check stock")
            print("4. Withdraw Money")
            while True:
                print()
                options = int(input("Enter preferred option(1-4): "))
                if options == 1:
                    Maintain.off()
                    Coffee.got = False
                    break
                elif options == 2:
                    Maintain.refill()
                elif options == 3:
                    Maintain.check()
                elif options == 4:
                    Maintain.withdraw()
                again = input("Would you like to do something else (yes/no): ")
                if not again == 'yes':
                    break
        else:
            print("Password is incorrect")
            print("Access Denied ")


def main():
    Coffee()
    print("Python virtual Coffee Machine")
    while Coffee.got:
        print()
        print("1. Get Coffe as user")
        print("2. Access resources as a maintainer")
        try:
            choice = int(input("your role please: "))
            print()
            if choice > 2 or 1 > choice:
                print("Enter number 1 or 2 please")
            elif choice == 2:
                Maintain.maintainOpt()
            elif choice == 1:
                Coffee.get()
        except ValueError:
            print("Enter numbers only please")


if __name__ == '__main__':
    main()


