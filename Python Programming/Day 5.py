
"""Dictionary & Its Function"""

# Dictionary maps the Key:Balue pair. 
d1 = {}
print(type(d1))

d2={"Anshu":"Dosa","Kittu":"Paneer","Rahul":"Fish"}
print(d2)
print(d2["Rahul"])

# Nested Distionary
d3={"Anshu":"Dosa","Kittu":"Paneer","Rahul":"Fish","Riya":{"B":"Bread Omlet","L":"Chawal Dal","Dinner":"Roti"}}
print(d3["Riya"]["B"])
#In Dictionary the value of any key can be dictionary, tuple, list. But the keys should be immutable.

# Adding New Item in Dictionary
d3["Akash"]="Chicken"
d3[420]="Water"
print(d3)


#Removing Items from dictionary
del d3[420]
print(d3)

## Dictionary Function

d4=d3.copy()
print(d4)
print(d4.get("Akash"))
print(d4.update({"Leena":"Choco"}))  #This will show none

# So in order to update dictionary: 
d4.update({"Leena":"Choco"})
print(d4)

print(d4.keys())
print(d4.items())



### Task 1: Create Dictionary & Take Input from User and Return meaning of word from the dictionary.

Dictionary={"Abondoned":"Leave",
"Abundant":"Plentiful",
"Admire":"Praise",
"Artful":"Crafty",
"Enormous":"Immense"}
Input=input("Enter the Word you want to get meaning :")
print(Dictionary[Input])
