

def getDividers(value):
    
    """"Gets the integer dividers of a number
    Args:
        value (int): a number to test
    Returns:
        list: a list of integer dividers
    """

    dividers =[]
    for i in range(1, value):
        # %  is the modulus operator which returns the remainder of an integer division
        if value % i == 0:
            dividers.append(i)

    return dividers

def isPerfect(value):
    "Returns True if the number is perfect and False otherwise"

    dividers = getDividers(value)

    if sum(dividers) == value:
        return True
    else: 
        return False

def main():
    maximum_number = 50     # maximum number to test

    print("Testing for perfecr numbers!")

    for value in range(1, maximum_number + 1):
        print("Analyzing number" + str(value))
        if isPerfect(value):
            print(str(value) + " is perfect!")
        else:
            print(str(value) + " is not perfect")

if __name__ == "__main__":
    main()