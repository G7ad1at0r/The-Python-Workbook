print("The Faces of Money\n")

money = int(input("Enter The Dollar Amount:\n>>> $"))

if money == 1:
    print("The one dollar banknote features George Washington.")
elif money == 2:
    print("The two dollar banknote features Thomas Jefferson.")    
elif money == 5:
    print("The five dollar banknote features Abraham Lincoln.")  
elif money == 10:
    print("The ten dollar banknote features Alexander Hamilton.") 
elif money == 20:
    print("The twenty dollar banknote features Andrew Jackson.")    
elif money == 50:
    print("The fifty dollar banknote features Ulysses S. Grant.")  
elif money == 100:
    print("The one hundred dollar banknote features Benjamin Franklin.")    
else:
    print("The banknote in that denomination is not available.")