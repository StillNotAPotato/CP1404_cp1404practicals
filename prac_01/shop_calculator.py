def main():
    total_cost = 0
    # inputs
    number_of_items = int(input("Number of items: "))

    while number_of_items < 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))

    for number_of_item in range(number_of_items):
        price_of_item = float(input("Price of item: "))
        # print('this is item:', number_of_item+1, price_of_item)
        total_cost += price_of_item

    if total_cost > 100:
        total_cost *= 0.9

    print("Total price of ", number_of_items, 'items is ${:.2f}'.format(total_cost))


main()
