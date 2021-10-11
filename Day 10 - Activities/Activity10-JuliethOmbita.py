
#           Solutions Day 10
print("===============================Warm up - Activity=================================\v")
# 1. Warm up - Activity
# This funtion take in an integer as a parameter and return whether or not that number passed in is even.


def isEven(num=0):
    if (num % 2 == 0):  # if the module is equal 0, the number is even.
        return print(f"\v1. The given number is {num} and is an even number.\v")
    else:
        return print(f"\v1. The given number is  {num} is a odd number. \v")


isEven()

print("\v=================================Activity 10.3=================================\v")


# 2.Activity 10.3 Sort Funtion.

# This function will be passed in a list of numbers, its job is to determine if the list is in need of being sorted or if it already sorted and will return a boolean determining whether or not that is the case.

def isSorted(myList=[0, 6, 0, 10]):
    sortList = sorted(myList)
    print("2.")
    return print(myList == sortList)


isSorted([3, 6, 10])
#isSorted([3, 6, 0, 9, 2, 4394049, 10])
#isSorted([5, 3, 23, 6, 10])


print("\v=================================Activity 10.4=================================\v")


# 3.Activity 10.4 Palindrome Funtion.
# This function determine whether or not the String passed in is a Palindrome


def palindrome(sentence="car"):
    sentence = sentence.upper()
    myList = list(sentence)     # Conver the imput to a list
    listCopy = myList.copy()
    myList.reverse()            # Reverse the list
    if myList == listCopy:      # Compare the list and it's reverse
        print(f"\v3. The input {sentence.capitalize()} is a palindrome.\v")
    else:
        print(f"\v3. The input {sentence.capitalize()} is not a palindrome.\v")


palindrome("Racecar")
# palindrome("91819")
# palindrome("Kayak")
# palindrome("Pineaple")
# palindrome("Madam")
