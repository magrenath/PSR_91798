


maximum_number = 50

# A number is prime when it is only divisible by 1 and itself
def isPrime(value):
    for i in range (2, value):
        remainder = value % i
        # If the remainder is zero, the division is exact and the number is not prime
        if remainder == 0:
            return False
    # Se não houver divisão exata, o número é primo
    return True

def main():
    print("Starting to compute prime numbers up to " + str(maximum_number) + " :")

    for i in range(1, maximum_number + 1):
        if isPrime(i):
            print('Number ' + str(i) + ' is prime.')
        else:
            print('Number ' + str(i) + ' is not prime.')

if __name__ == "__main__":
    main()


# To calculate how many prime numbers less than 10000 have the digit 3, insert at the command line
    # python3 primos.py | grep "is prime" | grep "3" | wc -l