##      Activity 9.1 For loop

# This funtion sort this list. 
def printList(myList): 
    listSorted = []
    for i in range(len(myList)):
        minNum = min(myList)      
        listSorted.append(minNum) 
        myList.remove(minNum)     
    print(f"\vThis is the list sorted:{listSorted}.\v")

listNum = [6,7,9,3,0]
printList(listNum)