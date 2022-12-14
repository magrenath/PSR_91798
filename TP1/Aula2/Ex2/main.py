from myfunctions import isPerfect

def main():
    maximum_number = 50     # maximum number to test

    print("Testing for perfect numbers!")

    for value in range(1, maximum_number + 1):
        print("Analyzing number" + str(value))
        if isPerfect(value):
            print(str(value) + " is perfect!")
        else:
            print(str(value) + " is not perfect")

if __name__ == "__main__":
    main()