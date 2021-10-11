
# ==================== Activity 12 ====================

import statistics

'''
==================== Activity 12.3 ====================

This funtion gets the average value of the original exam grades.
    Sol: For this solution I use the .mean() method and the funtion average(list) to find the average of the original exam grades.

'''


def average(listGrad):
    return statistics.mean(listGrad)


examsGrades = [1, 3, 5, 9, 87, 58, 39, 3]
print("\v Activity 12.3 \v")
print(
    f"The original exam greades list is {examsGrades}. \nThe average value of the original exam grades is: {average(examsGrades)}")


'''
==================== Activity 12.4 ====================

This funtion will return me back a list of booleans out of a list of grades. 
    - Grade < 55 => Boolen False. 
    - Grade >= 55 => Boolen True.

'''


def booleansList(listNum):
    for i in range(len(listNum)):
        if listNum[i] < 55:
            listNum[i] = False
        else:
            listNum[i] = True
    return listNum


listNum = [10, 50, 51, 52, 53, 55, 56, 57]
print("\v Activity 12.4 \v")
print(
    f"This is the list of students who passed and failed in booleans: \n{booleansList(listNum)}")


'''
==================== Activity 12.5 ====================

How many people passed the class?

This funtion print a message of how many ppl passed or failed the class.
    - Passed the class => 55+.
    - Failed the class < 55.
 
'''


def aproGrades(listNum):
    aproved = 0
    failed = 0
    for i in range(len(listNum)):
        if listNum[i] < 55:
            failed += 1
        else:
            aproved += 1
    return failed, aproved


grades = [10, 50, 51, 52, 53, 55, 56, 57]
print("\v Activity 12.5 \v")
print(f"""In the class: 
        - {aproGrades(grades)[0]} people failed. 
        - {aproGrades(grades)[1]} people pased.\v""")
