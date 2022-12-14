
# To run the code, add at the terminal, after the path, "--maximum_number x" or "-mn x" where x is the desired number

from myfunctions import isPerfect
import argparse

def main():

    # To interpret an input parameter which will be the maximum limit for how for to look for prime numbers
    parser = argparse.ArgumentParser(description = "Test for PSR.")
    # Method to add arguments
    parser.add_argument('-mn','--maximum_number', type = int, required = True, help = "The maximum number until which we check if numbers are perfect")

    # Creates the object
    args = vars(parser.parse_args())
    maximum_number = args["maximum_number"]

    
    print("Testing for perfect numbers!")

    for value in range(1, maximum_number + 1):
        print("Analyzing number" + str(value))
        if isPerfect(value):
            print(str(value) + " is perfect!")
        else:
            print(str(value) + " is not perfect")

if __name__ == "__main__":
    main()