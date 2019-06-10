from random import randint

old_plate = 1
new_plate = 2

low_letter_ascii = 65
high_letter_ascii = 90
low_number_ascii = 48
high_number_ascii = 57

def random_plate():
    """Create a random license plate old and new style"""
    count = 0    
    plate = randint(old_plate, new_plate)
    part_a = []
    part_b = []
    
    if plate == 1:
        while count <= 2:
            count += 1
            part_a.append(chr(randint(low_letter_ascii, high_letter_ascii)))
            
            while count > 2 and count <= 5:
                count += 1
                part_b.append(chr(randint(low_number_ascii, high_number_ascii)))                
                
    elif plate == 2:
        while count <= 3:
            count += 1
            part_a.append(chr(randint(low_number_ascii, high_number_ascii)))            
            part_b.append(chr(randint(low_letter_ascii, high_letter_ascii)))
    
    return part_a + part_b        

def main():
    print("The Random License Plate Creater\n")
    
    random_plate()        
    
    print(*random_plate())
    
if __name__ == "__main__":
    main()