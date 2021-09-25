FirstName = "Julieth"
LastName = "Ombita"
FavColor = "golden"
FavMeal = "pasta"


#1. F-string:
print(f"1. My name is {FirstName}. My last name is {LastName}. My favorite color is {FavColor} and my favorite meal is {FavMeal}.")

#2. Argument by Position:
print("2. My name is {FirstName}. My last name is {LastName}. My favorite color is {FavColor} and my favorite meal is {FavMeal}".format(FirstName = "Julieth", LastName = "Ombita", FavColor = "silver", FavMeal = "empanadas"))

#3. Argument by Position:
print("3. My name is {0}. My last name is {1}. My favorite color is {2} and my favorite meal is {3}.".format("Julieth", "Ombita", "silver", "ajiaco"))

#4. Concatenation:
print("4. My name is " + FirstName + ". My last name is " + LastName + ". My favorite color is " + FavColor + " and my favorite meal is " + FavMeal + ".")


#Use a extra sentence to see if GIT will track the changes. 
age = 27
Sol = "I am {0} years old, and I am {nationality}.".format(age, nationality="Colombian")
print (Sol)




