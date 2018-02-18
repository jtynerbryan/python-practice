def shopping():
    shopping_list = []
    help = "(type 'SHOW' to see your cart, 'HELP' for help and 'DONE' to finish) "
    while True:
        item = input(f"What would you like to add to your shopping list? {help} ")
        if item == 'HELP':
            print(help)
        elif item == 'SHOW':
            print (f"Your car contains {(', ').join(shopping_list)}")
        elif item == 'DONE':
            break
        else:
            shopping_list.append(item)
            print(f"{item} added to the cart")

    shopping_list = (', ').join(shopping_list)
    print(f'You bought {shopping_list}')

shopping()
