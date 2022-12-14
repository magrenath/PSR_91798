
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
