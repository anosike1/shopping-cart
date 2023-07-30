# print the welcome address. lol
print ('Welcome to the shopping Cart Program!\n'.upper())

# create 2 lists - one for items and the other for prices
items = []
prices = []

# create a while loop which
while True:
    # ...asks the user to select either option 1,2,3,4
    select = input ('Please select one of the following:\n1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit \nPlease enter an action: ')
    # if user selects 1, he/she will be required to input an item and price
    if select == '1':
        select_item = input ('What item would you like to add? ')
        # format the price as a float since you might work with decimals
        select_price = float(input (f"What is the price of {select_item}? "))
        # the items and price will be added/appended to the item and price list
        items.append (select_item)
        prices.append (select_price)

    # if user selects 2, the content of the cart will be listed
    elif select == '2':
        print ('The contents of this shopping cart are:')
        for num, item in enumerate (items):            
            print (f"{num+1}. {item} - ${prices[num]}")

# if user selects 3, he will be asked to delete an item from the list using the number
    elif select == '3':
        dellt = input ('Which item would you like to remove? ')
        dellt = int(dellt)
        # i used .pop() to do this
        items.pop(dellt-1)
        prices.pop(dellt-1)
        # it also prints ITEM REMOVED
        print ('Item removed.')

    # option 4 sums up the cost of  the items in the list
    elif select == '4':
        # i achieved this using the sum() function
        tot = sum (prices)
        print (f"The total price of the items in the shopping cart is {tot}")

    # if the user types a different number, the loop breaks and program ends
    else:
        break