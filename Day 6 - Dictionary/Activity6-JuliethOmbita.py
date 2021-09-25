# Activity 6: Dictionaries

car = {"Brand": "Ford", "Model" : "Mustang", "Year" : 1964}
print (f"Dictionary car {car}")
print(f"\vThe car model is: {car['Model']}\v")

print("\t \t DICTIONARY METHODS:\v")
#1. clear() I supposed that it's goint to removes all the elements from the dictionary 
print(f"1. This is the result of the clear() method: {car.clear()}\v")

#2. copy() I suspect it's going to provide a copy of the dictionary 
car = {"Brand": "Ford", "Model" : "Mustang", "Year" : 1964}
carCopy = car.copy()
print(f"2. This is the original dictionary: {carCopy}")
print(f"   This is the result of the copy() method: {carCopy}\v")
    
# 3. fromkeys() - Returns a dictionary with the specified keys and value. 
print(f"3. This is the result of fromkeys() method {dict.fromkeys(car)}")

# Example 2. Create a new dictionary with keys from coordinates and values set of values.
coordinates = {"x", "y", "z"}
values = {3,5,6} 
direction = dict.fromkeys(coordinates,values)
print(f"   This an additional example of the fromkeys() method, when values appended to keys: {direction}\v")

# 4. get() It returns the value of the specified key 
print(f"4. This is the result of get method: {car.get('Brand')}\v")

# 5. Items() Returns a list containing a tuple for each key value pair 
print(f"5. This is the result of items method: {car.items()}\v")

# 6. keys() I think it will returns a list of keys 
print(f"6. This is the result of keys method: {car.keys()}\v")

# 7. pop() pop out an specified key value pair
print(f"7. This is the result of pop method, poping 'Brad' out of the dictionary: {car.pop('Brand')}")
print(f"   This is the resulting dictionary: {car}\v")

# 8. popitem() This method removes the last inserted key-value pair 
car["Type"]="Sports car"
print(f"8. This is the dictionary before using the popitem method: {car}")
print(f"   This is the result of get method: {car.popitem()}")
print(f"   This is the dictionary after using the popitem method: {car}\v")

# 9. setdefault() This method returns the value of the specified key. If the key does not exist it'll set a default value. 
print("9. This is the result of setdefault method:")
print(f"   Using the Model key: {car.setdefault('Model', None)}")
print(f"   Using the Color key: {car.setdefault('Color', None)}\v")

# 10. update() This method adds the items key:value from other dictionary car2 into dictionary car. 
car2 = {"Type":"Sports car", "Color":"Red"}
car.update(car2)
print(f"10. This the dictionary updated: {car}\v")
# car.update(car2)
# print(car)

# 11. values() Returns a list of all the values in the dictionary
print(f"11. This is the result of values method: {car.values()}\v")
