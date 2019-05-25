import statistics

def main():
    print("The Median Value Of Three")

    a = float(input("Enter A Number:\n>>> "))
    b = float(input("Enter A Number:\n>>> "))
    c = float(input("Enter A Number:\n>>> "))
    
    median(a, b, c)

def median(a, b, c):
    '''find the median value'''
    values = a, b, c
    median = statistics.median(values)
    print(f"\nThe Median Value Of {values} Is:", median)
    
main()