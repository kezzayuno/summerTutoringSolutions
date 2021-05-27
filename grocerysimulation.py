# To the grocery simulation, have a resume order thing (from text file)
# Make error files for that project..
# Other project ideas: hangman, something related to line ups for queues..

def main():
    with open('products.txt', 'r') as f:
        groceryStockFile = f.readlines()
    groceryStock = organize(groceryStockFile)

    print("Welcome to the Grocery Simulator!")
    profile = register()
    choice = ''
    while choice != '4':
        choice = input("Hello, {}! What would you like to do today?\n1."
                       " Display Grocery Stock\n2. Display Shopping Cart\n3. Pay\n4. Quit\n>".format(profile[0]))
        while choice not in ['1', '2', '3', '4']:
            choice = input("Sorry, your selection is invalid. Please choose "
                           "again.\n1. Start Buying\n2. Display Shopping Cart\n3. Pay\n4. Quit\n>")
        if choice == '1':
            displayGroceryStock(groceryStock)
        elif choice == '2':
            pass
        elif choice == '3':
            pass
    print("Thank you for shopping! Have an amazing day!")

def displayGroceryStock(groceryStock):
    pass

def organize(stockFile):
    stockDict = {'fruit': {}, 'veggie': {}, 'meat': {}, 'grains': {}, 'dairy': {}, 'dairySubs': {}}
    for food in stockFile:
        foodInfo = food.rstrip().split('%')
        foodKey = foodInfo[0]
        foodName = foodInfo[1]
        foodAmountPrice = [int(foodInfo[2]), float(foodInfo[3])]
        stockDict[foodKey][foodName] =  foodAmountPrice
    return stockDict

def register():
    profile = []
    name = input("First, please enter for name: >")
    wallet = input("How much are you planning to spend today? >")
    while not wallet.isdigit():
        wallet = input("Sorry, that currency doesn't work here.\nHow much are you planning to spend today? >")
    profile.append(name)
    profile.append(float(wallet))
    return profile

main()