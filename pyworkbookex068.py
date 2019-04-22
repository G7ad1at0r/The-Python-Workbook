print("The Parity of the 8 Bit Binary Parity:\n")
# eg. 10101010 = even // 11111110 = odd
# even add "0" odd add "1" to make it even.
parity = input("Enter 8 Bits (RETURN to quit) :\n>>> ")

while parity != "":
    if parity.count("0") + parity.count("1") != 8 or len(parity) != 8:
        print("Thats not 8 Bits. Try Again!")
    else:
        ones = parity.count("1")
        
        if ones % 2 == 0:
            print("The Parity Bit should be \"0\".")
        else:
            print("The Parity Bit should be \"1\".")
        
    parity = input("Enter 8 Bits (RETURN to quit) :\n>>> ")