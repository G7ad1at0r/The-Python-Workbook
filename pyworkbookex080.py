print("The Coin Flip Simulation\n")

import random

def coin_toss():
 
    flip = 0  
    heads = 0
    tails = 0
    results = []

    while heads != 3 and tails != 3:
        coin = random.randint(1, 2)
                
        if coin == 1:
            print("Heads!")
            heads += 1
            tails = 0
            results.append("H")
            flip += 1
            
           
        elif coin == 2:
            print("Tails!")
            tails += 1
            heads = 0
            results.append("T")
            flip += 1
            
                
    print(results)
    print(f"Winner is {results[-1:]} in {flip} flips.\n")
 
count = 0


while count < 10:
    count += 1
    coin_toss()