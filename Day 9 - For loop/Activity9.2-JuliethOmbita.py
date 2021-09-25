##      Activity 9.2 - Creation of max method using Loop

def maxNum(myList):
    maxNumb = 0
    for i in range(len(myList)):
        if myList[i]>maxNumb:       #This condition line finds the bigest number.
            maxNumb = myList[i]
    print (maxNumb)

myList = [6,1909,9,3,9]
maxNum(myList)