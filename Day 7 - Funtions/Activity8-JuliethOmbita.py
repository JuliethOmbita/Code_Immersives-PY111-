##  Activity 8 - if/else conditions

# 1.This program check the greatest number between num1, num2, num3:

num1 = 90
num2 = 69
num3 = 50
print("\v")
if (num1>num2 and num1>num3):
    print (f"This is the greatest number amoung the 3 numbers: {num1}")
elif (num2>num1 and num2>num3): 
    print (f"This is the greatest number amoung the 3 numbers: {num2}")
else: print (f"This is the greatest number amoung the 3 numbers: {num3}")
print("\v")
# 1.This program simulate the Traffic light. Through the evaluation of the trafLight variable.

#Introduce the traffic color
#trafLight= "red"
trafLight= "yellow"
#trafLight= "gren"

if (trafLight == "red"):
    print ("It's red. Stop")
elif (trafLight == "yellow"): 
    print ("It's yellow. Slow down")
else: print ("It's green. Keep going")

