print("The Capitalizer\n")

def capitalize(phrase):
    '''Capitalize a string'''
    result = phrase.replace(" i ", " I ")
    
    if len(phrase) > 0:
        result = result[0].upper() + \
        result[1 : len(result)]
        
    pos = 0
    
    while pos < len(phrase):
        if result[pos] == "." or result[pos] == "!" or result[pos] == "?":
            pos = pos + 1
            
            while pos < len(phrase) and result[pos] == " ":
                pos = pos + 1
                
            if pos < len(phrase):
                result = result[0 : pos] + \
                result[pos].upper() + \
                result[pos + 1 : len(result)]
            
        pos = pos + 1
        
    return result

def main():
    phrase = input("Enter A Phrase:\n>>> ")
    capitalized = capitalize(phrase)
    print("Your Phrase Capitalized Is:\n"+ capitalized)

main()