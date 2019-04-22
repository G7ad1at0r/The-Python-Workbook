print("Discontinued Discounts\n")

for price, discount in zip([4.95, 9.95, 14.95, 19.95, 24.95], [.6, .6, .6, .6, .6]):
    total = price * discount
    sale = price - total
    print(f"\nThe regular price is: ${price}")
    print("A savings of 60 percent is: $%.2f" % total)
    print("Your total per item is: $%.2f" % sale)