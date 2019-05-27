def prime(n):
    '''Determine if a number is prime'''
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("Enter A Integer:\n>>> "))
    
    prime(n)  
    
    if prime(n) == True:
        print("\n",n,"Is a prime number.")
    elif prime(n) == False:
        print("\n",n,"Is NOT a prime number.") 

if __name__ == "__main__":
    print("All Primed Up\n")        
    
    main()