##      Activity8.1 - Funtions. 
def comparison(num1=6, num2=5, num3=4):
    numbers=(num1, num2, num3)
    numbers = (sorted(numbers))
    numbers = tuple(numbers)
    #print(type(numbers))
    return numbers
     
print(f"\vThis is the sorted Tuple of the 3 numbers passes: {comparison(9899, 1, 5)}\v")