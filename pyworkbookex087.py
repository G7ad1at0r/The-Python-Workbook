def center(phrase, width):
    '''Center a string'''
    width = 42
    fill = " "
    return(phrase.center(width, fill))

if  __name__ == '__main__':
    print("Center A String\n")

def main():
    width = 0
    phrase = input("\nEnter A String:\n>>> ")
    print("\n" * 5)
    print(center(phrase, width))

main()