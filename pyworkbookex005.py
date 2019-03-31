# more than 1 liter 25 cent depost
# less than or equal 1 liter 10 cent deposit
big_bottle = int(input("How many big bottles? \n>>> "))

small_bottle = int(input("How many small bottles? \n>>> "))  

big_refund = big_bottle * .25

small_refund = small_bottle * .10

total_refund = small_refund + big_refund

print("You have ", big_bottle, " big bottles at 25 cents each.")
print("You have ", small_bottle, " small bottles at 10 cents each.")
print("Your total refund is: \n$ %.2f" % total_refund)