##      Activity 9 - Functions list values

# 1. Write a function that given a list will print out all the values in that list

def printList(myList):  #This funtion print a list
    print("This funtion every item of a list using a loop:")
    j=0
    for i in myList:
        j += 1
        print(f"{j}. {i}")
    print("\v")

# 2. Write a function that takes in one integer as a parameter and will print out your name as many times as specified by the argument

def printName(numTimes=2):  #This funtion print my name a specific number of times. 
    print(f"This funtion print my name a {numTimes} number of times:")
    for i in range(numTimes):
        print(f"{i+1}. Julieth")

myList = ["Apple","Kiwi","Orange","Passionfruit"]
printList(myList)

printName(4)