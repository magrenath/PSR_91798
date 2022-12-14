from readchar import readkey

# 4a -----------------------------------------------------------------------------------------------

def printAllPreviousChars():

    # reads the inserted key
    inserted_character = readkey()
    # corresponding ASCII number to the key inserted
    character_number = ord(inserted_character)

    print("Printing all chaars up to " + inserted_character)
    
    # creates the list
    characters = []

    for number  in range(32, character_number):     # 32 = space number at ASCII
        # takes the number from the ascii table and returns the corresponding character
        character = chr(number)
        # adds the key to list
        characters.append(character)

    print(characters)


# 4b -----------------------------------------------------------------------------------------------

def readCharsUpTo(stop_char):

    while True:
        print("Enter any key:")
        key = readkey()
        print("You pressed " + key)

        if key == stop_char:
            break


# 4c -----------------------------------------------------------------------------------------------

def countNumbersUpTo(stop_char):

    # Reads all the inputs and put them in the keys list
    keys = []
    while True:
        print("Enter any key:")
        key = readkey()
        print("You pressed " + key)
        
        if key == stop_char:
            break

        keys.append(key)

    #print("User pressed " + str(keys))

    # Process the list of keys and figure out which of those are numbers
    keys_numeric = []
    keys_nonnumeric = []

    for key in keys:
        if str(key).isnumeric():
            keys_numeric.append(key)
        else:
            keys_nonnumeric.append(keys)

    total_numeric = len(keys_numeric)
    total_nonnumeric = len(keys_nonnumeric)

    print("Numeric Keys are " + str(total_numeric) + " : " + str(keys_numeric))
    print("Non Numeric Keys are " + str(total_nonnumeric) + " : " + str(keys_nonnumeric))

    # dictionary from 5c that tells the order of the numeric keys inserted

    keys_dict = {}
    counter = 0
    for keys in keys:
        if key.isnumeric():
            keys_dict[counter] = key

            counter += 1

    print(keys_dict)

    #   -----------------------------------------------------------------------------------------------

def main():

    # 4a
    # printAllPreviousChars()

    # 4b
    # readCharsUpTo("x")

    # 4c
    countNumbersUpTo('x')

if __name__ == "__main__":
    main()
