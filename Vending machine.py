#Flavourflow Vending machine.

print("\nWelcome to Flavorflow vending machine !!!") #welcome message 

import time
time.sleep(2) #function to add transition between text

items = { 
    "\nMenu\n" : { "Chips\n"
        "A1": {"item":"Doritos" , "price":4 , "stock":15},
        "A2": {"item":"Lays" , "price":3 , "stock":10},
        "A3": {"item":"Pringles" , "price":4 , "stock":9},
        "A4": {"item":"Takis" , "price":3 , "stock":10},
        "A5": {"item":"JoloChip" , "price":5 , "stock":5},
    "---------------------------------------------------------\n"
    "Chocolates\n"
        "B1": {"item":"Twix" , "price":3 , "stock":20},
        "B2": {"item":"Hershey" , "price":4 , "stock":15},
        "B3": {"item":"Galaxy" , "price":4 , "stock":16},
        "B4": {"item":"Kitkat" , "price":3 , "stock":9},
        "B5": {"item":"Maltesers" , "price":3 , "stock":17},

    "---------------------------------------------------------\n"
    "Drinks\n"
        "C1": {"item":"7Up" , "price":3 , "stock":14},
        "C2": {"item":"Water" , "price":1 , "stock":11},
        "C3": {"item":"Coffee" , "price":2 , "stock":13},
        "C4": {"item":"Pepsi" , "price":3 , "stock":10},
        "C5": {"item":"Tea" , "price":1 , "stock":16},
    "---------------------------------------------------------\n"
    
    "Snacks\n"
        "D1": {"item":"Petzels" , "price":4 , "stock":9},
        "D2": {"item":"Oreo" , "price":4 , "stock":16},
        "D3": {"item":"Pop-Tarts" , "price":4 , "stock":10},
        "D4": {"item":"Popcorn" , "price":3 , "stock":13},
        "D5": {"item":"Reeses" , "price":3 , "stock":10},
     },

}

#print menu of the items
def print_menu(item):
    for category, category_items in item.items():
        print(category + ":")
        for code, item in category_items.items():
            print(f'{code}: {item["item"]} ({item["price"]:.2f} dhs)')
            print()

#Function to get valid code from user
def get_code(item):
    while True:
        code= input ("Enter code: ")
        #To check the given code is valid or not.
        for category, category_items in item.items():
            if code in category_items:
                return code 
        print("Invalid code. Please try again.")

#Function to get correct amount from the user 
def get_money(item, code):
    #search for items in menu.
    for category, category_items in item.items():
        if code in category_items:
            item= category_items[code]
            break
        else:
            print(f'Invaild Code "{code}".')
            return
        
    while True:
            money=float(input("Enter money:"))
            #to check if money is enough 
            if money > item["price"] or money==item["price"]:
                return money
                dispense_item(item , code , money)
            print(
                f'Not enough money, Please insert {item["price"]- money :.2f}dhs more.'
            )
    
#Function to dispense item and calculate change.
def dispense_item(item , code, money):
    for category, category_items in item.items():
        if code in category_items:
            item= category_items[code]
            break
        else:
          print(f'Invalid code "{code}".')
          return

#To check if items in stock   
    if item["stock"] > 0:
        #dispense item and calculate
        print(f'\ndispensing {item["item"]}.....')
        change = money - item["price"]
        item["stock"]-= 1
        print(f"Returning {change: .2f} DHS......\n")
    else:
        print(f'\nError: {item["name"]} is out of stock')

#Main Program
while True:
    #print menu of the items
    print_menu(items)
    #To get valid code from the user.
    code = get_code(items)
    #To get valid amount of money from user.
    money = get_money(items, code)
    #Dispense item and calculate change
    dispense_item(items , code , money)

#Prompt user to continue or exit 
    while True:
        response= input("\n Would you like to make another purchase? (yes/no)")
        if response.lower() == "yes":
            break
        elif response .lower()=="no":
            rating = int(input("\nHow would you like to rate our service from 1-5 -->"))
            print("\nThank you for using Flavorflow vending machine.Have a great day !!!")
            exit()
        else:
            print("Invaild response. Please Try again.")




















            
