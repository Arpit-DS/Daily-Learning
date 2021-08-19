# -*- coding: utf-8 -*-
"""
Topic: Python Lists And List Functions

Created on Tue Aug 17 10:22:34 2021

@author: ARPIT
"""
kitchen=["Spoon","Plates","Fork","Mats","Lid","Utensils","Crockery","Bowl"]
electronics=["Oven","Washing Machine","TV","Fridge","Air Conditioner","Air Purifier"]
bathroom=["Soap","Washing Powder","Lufa","Harpic","Floor Cleaner","Toilet brush","Containers",
          "Soap Case"]
print(kitchen)
print(electronics)
print(bathroom)

number=[1,2,3,5,7,8,9,15,16,17,10,11,12]
print(number)
print(number[5])
print(number.sort()) #This will show None
number.sort()
print(number)

number.reverse()
print(number)

#Slicing returns List
print(number[:8])
print(number[3:])

#Extended Slice
# Thumb Rule: In case of Negative Slicing, Dont take offset value less than -1. For Example -2 in below
print(number[::-2])

numbers=[10,20,40,50,60,80,30,25,35]
print(numbers[::-2]) #It will give output [35, 30, 60, 40, 10] but in next case
#The above code it first reverses the order and then put an offset of -2.
print(numbers[1::-3]) #Output is [20]. 
print(numbers[1:5:-3]) #Output will give blank list []

print(len(numbers)) # Length of the List
print(max(numbers)) # Maximum of Numbers
print(min(numbers)) #Minimum of Numbers

#Append: Add numbers in list at the End
kitchen.append(electronics)
print(kitchen)

#Insert: When we wanth to insert number at the specific index. For Example
numbers.insert(5, 95)
numbers.remove(number)
print(numbers)

#Pop: 
    
    
    

# tuples

number[1]=98
print(number)

#Mutable: can Change eg: List
#immutable: Cannot Change eg:Tuples

Tup=(5,6,7,8,9)
print(Tup)

Tup[1]=1
print(Tup) #Cannot change the Position 1 value
#If we are using Tuple we need to give extra comma so that it can be recognized as Tuple
Tup=(1,)
print(Tup)


a=1
b=8

temp=a
a=b
b=temp
print(a,b)

a,b=b,a
print(b)
print(a)

















