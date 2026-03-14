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
}

money = {
    "value": 0,
}
def coffee_machine():

    off = False
    while not off:
        
        curr_water = resources["water"]
        curr_milk = resources["milk"]
        curr_coffee = resources["coffee"]


        wants = input("What would you like? : ")
        if(wants=="off"):
            print("turning off!")
            off = True
        elif(wants=="report"):
            print(f"water : {resources['water']}")
            print(f"milk : {resources['milk']}")
            print(f"coffee : {resources['coffee']}")
            print(f"money : {money['value']}")
        else:

            req_water = MENU[wants]["ingredients"]["water"]
            if wants!="espresso":
                req_milk = MENU[wants]["ingredients"]["milk"]
            req_coffee = MENU[wants]["ingredients"]["coffee"]
            req_cost = MENU[wants]["cost"]
            na = False
            if(curr_coffee<req_coffee):
                print("sorry,not enough coffee")
                na = True
            if wants != "espresso":
                if(curr_milk<req_milk):
                    print("sorry,not enough milk")
                    na = True
            if(curr_water<req_water):
                print("sorry,not enough water")
                na = True
            
            if(not na):
                quaters = int(input("How many quaters? : "))
                dimes = int(input("How many dimes? : "))
                nikels = int(input("How many nikels? : "))
                pennies = int(input("How many pennies? : "))

                total = (0.25*quaters)+(0.1*dimes)+(0.05*nikels)+(0.01*pennies)
                if(total < req_cost):
                    print(f"sorry the cost is ${req_cost} but you only gave ${total} , money refunded!")
                    total = 0
                else:
                    print(f"here is your change ${total-req_cost}")
                    print(f"Enjoy your {wants}☕!")
                    money["value"]+=req_cost

                    resources["water"]-=req_water
                    resources["coffee"]-=req_coffee
                    if wants!="espresso":
                        resources["milk"]-=req_milk

        


coffee_machine()


