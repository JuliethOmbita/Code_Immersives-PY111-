# ==================== Activity 12 ====================

import statistics

'''
==================== Activity 12.1 ====================

This funtion will receive a list of exam grades represented by integers.
    - Calculate the standard deviation of the exam grades list.
    - Return the list with all the exam values updated: Itself plus the standard deviation, if this addition goes above 100 the grade passed is 100.
'''


def standDev(listExams):
    print("\v Activity 12.1 ")
    print(
        f"\nI'm about to calculate the standard deviation using the method .stdev(). \nThis is the exam grades list: {listExams}")
    # Convert the standar deviation to a integer to avoid working w float.
    standDev = int(statistics.stdev(listExams))
    curvedList = listExams.copy()
    # Let the user know the stander deviation
    print(f"The standard deviation is: {standDev}.\v")
    # Update values of the list with the value plus std deviation. Values over 100 will be assing 100.
    for i in range(len(curvedList)):
        add = curvedList[i]+standDev
        if add >= 100:
            curvedList[i] = 100
        else:
            curvedList[i] = add
    return curvedList


print("\v==================== Activity 12.1 ====================")
examsGrades = [1, 3, 5, 9, 87, 58, 39, 3]
myList = standDev(examsGrades)
print(
    f"This is the exam values updated (Itself plus the standard deviation, but if this addition goes above 100 the grade the value passed is 100): {myList}\v")


'''
==================== Activity 12.2 ====================

This function returns the average value of the curved exam greades.
    Sol: For this solution I use the .mean() method and the funtion average(list) to find the average value of the curved exam greades.
'''


def average(listGrad):
    return statistics.mean(listGrad)


print("\v Activity 12.2 \v")
print(
    f"The curved exam greades list is {myList}. \nThe average value of the curved exam greades is: {average(myList)}.\v")
