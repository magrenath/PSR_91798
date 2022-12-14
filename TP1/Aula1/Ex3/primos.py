from colorama import Fore, Back, Style

maximum_number = 50

def isPrime(value):
    for i in range (2, value):
        remainder = value % i
        # If the remainder is zero, the division is exact and the number is not prime
        if remainder == 0:
            # Prints all divisors calculated for the prime number
            print("The divisors for wich the number " + str(value) + " is not prime are: " + str(list(range(2, i+1))))
            return False

    return True    

def main():
    print("Start to compute prime numbers up to " + str(maximum_number) + " :")

    for i in range(1, maximum_number + 1):
        if isPrime(i):
            # Prints the prime number text as bright green
            print(Style.BRIGHT + Fore.GREEN + "Number " + str(i) + "is prime" + Style.RESET_ALL)
        else:
            print("Number " + str(i) + " is not prime.")

if __name__ == "__main__":
    main()