from random import randint

longest = 10
shortest = 7
min_ascii = 33
max_ascii = 126

def random_password():
    '''Create a random password'''
    random_lenth = randint(shortest, longest)
    
    result = ""
    
    for i in range(random_lenth):
        random_character = chr(randint(min_ascii, max_ascii))
        result = result + random_character
    
    return result

def main():
    print("The Random Pasword Generator")
    print()
    print(f"Your random password is: {random_password()}")    

if __name__ == "__main__":
    main()