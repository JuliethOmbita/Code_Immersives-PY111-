
# FIZZBUZZ

# Print the numbers between 1 and 100 (inclusive)
#          1.  If the number is divisible (able to divide) by 3 -> Print "fizz" instead of the number.
#          2.  If the number is divisible by 5 (able to divide) -> Print "buzz" instead of the number.
#          3.  If the number is divisible by BOTH 3 and 5 (able to divide) -> Print "fizzbuzz" instead of the number
#          4. If the number is not divisible by either 3 or 5 (able to divide) -> Print the number itself.


# 1. Print in a list
def fitbuzz():
    first = "fizz"
    second = "buzz"
    # Emty list for the outcome
    fizzbuzzList = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzzList += [first + second]
        elif i % 3 == 0:
            fizzbuzzList += [first]
        elif i % 5 == 0:
            fizzbuzzList += [second]
        else:
            fizzbuzzList += [i]
    return fizzbuzzList


print(
    f"This is the outcome of the activity fitbuzz in a list: \n{fitbuzz()}\v")


# 2. Print out list

def fitbuzz():
    first = "fizz"
    second = "buzz"
    fizzbuzzList = []
    for i in range(0, 101):
        if i % 3 == 0:
            print(first)
        elif i % 5 == 0:
            print(second)
        elif i % 3 == 0 and i % 5 == 0:
            print(first + second)
        else:
            print(i)


print(fitbuzz())
