print("The Game Of Roulette\n")
print("Odds 36 : 1 ")
print("Odd / Even 1 : 1")
print("Red / Black 1 : 1")
print("High / Low 2 : 1\n")

from random import randrange

your_bet = int(input("Enter Your Bet:\n>>> "))
your_number = int(input("Enter You Number:\n>>> "))
your_color = input("Enter (r) for Red or (b) for Black:\n>>> ")
your_even_odd = input("Enter (e) for Even or (o) for Odd:\n>>> ")
your_high_low = input("Enter (h) for High (19-36) or (l) for Low (1-18):\n>>> ")
print("\n**** THE SPIN RESULTS ****")

# the wheel
number = randrange(0, 38)
#number = 37 #test for 37
if number == 37:
    print("The spin result is 00")
else:
    print("The spin result is %d" % number)

# 37 or 00 payout $0
if number == 37:
    print("Payout: $0.00")
else:
    print("Payout:", number)

# color payout red (1 3 5 7 9) ///Red Payout .. Could be all one line\\\
if number % 2 == 1 and number >= 1 and number <= 9:
    print("Payout Color: Red")
    color = "r"
# red (12 14 16 18)
elif number % 2 == 0 and number >= 12 and number <= 18:
    print("Payout Color: Red")
    color = "r"
# red (19 21 23 25 27)
elif number % 2 == 1 and number >= 19 and number <= 27:
    print("Payout Color: Red")
    color = "r"
# red (30 32 34 36)
elif number % 2 == 0 and number >= 30 and number <= 36:
    print("Payout Color: Red")
    color = "r"
# 00 and 0 $0.00
elif number == 0 or number == 37:
    print("Payout: $0.00")
    color = "00"
# black
else:
    print("Payout Color: Black")
    color = "b"

# even or odd payout
if number >= 1 or number <= 36:
    if number % 2 == 0:
        even_odd = "e"
        print("Payout Even")
    elif number <= 0 or number == 37:
        print("Payout: $0.00")
        even_odd = "00"
    else:
        even_odd = "o"
        print("Payout Odd")
        
# high low payout
if number == 37:
    high_low = "00"
elif number <= 18:
    print("Payout: 1 - 18")
    high_low = "l"
elif number <= 36:
    print("Payout: 19 - 36")
    high_low = "h"
    
print("****** YOUR CHOICES ******")
print("Your number is:", your_number)
print("Your bet is:", your_bet)
print("Your color is:", your_color.title())
print("Your Even or Odd is:", your_even_odd.title())
print("Your High or Low is:", your_high_low.title())
print("****** YOUR RESULTS ******")

if number == your_number:
    prize_1 = (your_bet * 36) + your_bet
    print("Congrats You Win: $%.2f" % prize_1)
elif number == 37:
    print("Sorry You Lose: $0.00")
    prize_1 = 0
else:
    print("Sorry No Match: $0.00")
    prize_1 = 0

if your_color == color:
    prize_2 = (your_bet * 2)
    print("Congrats You Win: $%.2f" % prize_2)
elif number == 37:
    print("Sorry You Lose: $0.00")
    prize_2 =0
else:
    print("Sorry No Match: $0.00")
    prize_2 = 0

if your_even_odd == even_odd:
    prize_3 = (your_bet * 2)
    print("Congrats You Win: $%.2f" % prize_3)
elif even_odd == 37:
    print("Sorry You Lose: $0.00")
    prize_3 = 0
else:
    prize_3 = 0
    print("Sorry No Match: $0.00")

if high_low == 37:
    print("Sorry You Lose: $0.00")
    prize_4 = 0
elif your_high_low == high_low:
    prize_4 = (your_bet * 2) + your_bet
    print("Congrats You Win: $%.2f" % prize_4)
else:
    prize_4 = 0
    print("Sorry No Match: $0.00") 

prize_total = prize_1 + prize_2 + prize_3 + prize_4
print("Total Prize: $%.2f" % prize_total)
print("**************************")

print("\nThanks For Playing!")