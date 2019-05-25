def main():
    print("      Taxi Taxi\n~~~Trip Calculator~~~")

    km = float(input("Enter distance travelled in KM:\n>>> "))
    
    taxi_fare(km)
    
def taxi_fare(km):
    '''Calculate a taxi fare'''
    distance = 7.1428571428571 # 1km ÷ 140 m (7.14...... km)
    set_fee = 4.00
    fee = .25 # per 140 m

    fare = ((distance * km) * fee) + set_fee
    if fare % 5 == 0:
        print("Total: $%.2f" % fare)
    elif fare % 5 != 0:
        fare = round(fare, 1)
        print("Total: $%.2f" % fare)
    print("\nYou Travelled: %.2f KM" % km)

main()