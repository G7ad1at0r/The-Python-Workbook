def main():
    print("The Shipping Calculator\n")

    quantity = int(input("Enter the number of items to be shipped:\n>>> "))
    
    ship_calc(quantity)

def ship_calc(quantity):
    '''Shipping calculator'''
    item = 10.95
    additional_item = 2.95
    cost = 0
  
    if quantity == 1:
        cost = 10.95
        print(f"\nYour Total For Shipping {quantity} Item Is: $%.2f" % cost)
    elif quantity >=2:
        cost = 10.95 + ((quantity - 1) * 2.95)
        print(f"\nYour Total Shipping For {quantity} Items Is: $%.2f" % cost)
    else:
        print("INVALID, Please Try Again")  
        
main()