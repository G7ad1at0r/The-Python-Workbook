from PyWorkbookEX092 import prime

    
def next_prime(n):
    '''Determine if a number is prime. if not fint the next highest prime number'''    
    prime(n)
    
    print()
    
    if prime(n) == True:
        print(f"{n} is already a prime number.")
    while prime(n) == False:
        n += 1
        if prime(n) == True:
            print(f"The next prime number is: {n}")

def main():
        
    print("The Next Prime\n")
   
    n = int(input("Enter A Integer:\n>>> "))
        
    next_prime(n)

if __name__ == "__main__":
    main()