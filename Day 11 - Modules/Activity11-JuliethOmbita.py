import random

#           Activities 11 - Modules

# ================================ Activities 11.1 ================================

# 1. This function take in an integer as a parameter, create a list of the size passed in as an argument and populate the list with random numbers between 0-1023. Using the getrandbits() method of the random module,


print("\v\v----------- Activities 11 - Modules ----------- \v\v")


def randomList(sizeList=5):  # Define the funtion with a defauld value.
    myList = []  # Define the list that will be populate with random numbers
    for i in range(sizeList):  # This for iterates through the list appending the new random value
        myList += [random.getrandbits(10)]
    print(f"\v11.1. The input size is: {sizeList}.")
    print(f"    The resulted list of random number is: {myList}\v")


randomList(5)


# ================================ Activities 11.2 ================================

# 2. This function that will generate a random list and takes in a number as a parameter. This number will be the size of the list and the values passed into, will be in the range 20 and 78, excluding of the 78.


def randomRange(sizeList=5):
    myList = []
    for i in range(sizeList):
        myList += [random.randrange(20, 78)]
        myList.sort()
    print(f"\v11.2. The input size is: {sizeList}.")

    print(
        f"  The resulted list of random number in the range 20 and 78, excluding of the 78 is: {myList}\v")


randomRange(19)
