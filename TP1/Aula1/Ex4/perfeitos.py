maximum_number = 100

def isPerfect(value):
    
    # Defines a variable to store the sum of exact divisors
    sum = 0

    for i in range(1, value): 
        # Checks if the division is exact 
         remainder = value % i         
         if remainder == 0:
            sum = sum + i
            if sum == value:
                return True
    
    return False

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(0, maximum_number + 1):
        if isPerfect(i):
            print("Number " + str(i) + " is perfect.")

if __name__ == "__main__":
    main()