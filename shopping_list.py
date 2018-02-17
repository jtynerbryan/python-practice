def shopping():
    shopping_list = []
    item = ''
    while True:
        item = input("What would you like to add to your shopping list? type 'DONE' to finish ")
        if item == 'DONE':
            break
        else:
            shopping_list.append(item)
            print(f'{item} added to the cart')

    shopping_list = (', ').join(shopping_list)
    print(f'You bought {shopping_list}')

shopping()
