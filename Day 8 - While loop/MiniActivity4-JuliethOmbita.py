##      Mini Activity 4 - While Loops 

#1. Create a While loop that goes through the 12 days of Christmas
i=1
twelvePrest = ("A partridge in a pear tree", "Two turtle doves", "Three french hens","Four calling birds","Five gold rings","Six geese a-laying","Seven swans a-swimming","Eight maids a-milking","Nine ladies dancing","Ten lords a-leaping","Eleven pipers pipin","Twelve drummers drumming")

while (i<13):
    print(f"On the day {i} of Christmas, my true love sent to me: {twelvePrest[i-1]}")
    i=i+1


#2. Create a While loop that takes a list of integers, and gives the sum of the integers.
 
listInt = (4,5,6,7,8,9)
position = len(listInt)
i=0
sum = 0
while (i<position):
    sum = listInt[i] + sum
    i=i+1 
else: print(f"\vThe total sum of the integers is: {sum}") 

