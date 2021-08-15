# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 19:46:32 2021

@author: ARPIT
"""

"""Variables"""
var1="Hello World " #String Variable
var2=4 #Integer Variable
var3=36.5 #Float Variable
var4="Hello India"
print(var1,var2,var3)


"""Type Function"""
print(type(var1))
print(type(var2))
print(type(var3))
print(var2+var3) # It will give 40.5
print(var1+var2) # It will show an error
print(var1+var4) # It will concatenate two string Ans" Hello World Hello India"


"""Typecast: Situation when need to convert the type of variable from one type to another.
Python includes two types of type conversion.

Explicit Conversion: In Explicit Type Conversion, users convert the data type of the item to 
needed data type. We use the predefined roles such as int(), float(), str(), etc to execute 
explicit type conversion.

Implicit Conversion: This procedure does not require any user participation. Let us see an 
instance where Python boosts the conversion of a lower data type (integer) to the greater 
data type (floats) to prevent data loss.
"""
var5="50"
var6="40"
print(var5+var6)
print(type(var5+var6)) # Will come as string
#In order to change the add the variables we will typecast our variables

print(int(var5) + int(var6))
print(type(int(var5) + int(var6)))


"""Print Hello World 10 Times using 
1. New Line Character
2. Escape sequence characters """

# 1.Using New Line Character
print(10*"Hello Arpit ",end=",")

#2. Using Escape Sequence Characters
print(10*"Hello Arpit \n")


print(10*int(var5) + int(var6)) #This will result in 540
# In order to print it 10 Times we will typecast it.
print(10*str(int(var5) + int(var6))) 


"""User Input Function"""

print("Enter your Number")
ip=input()
print("You Entered ",ip)
print(ip+10) #This will show error as we can't add int and string. So in order to add 10 to input number 
#we will typecast the input number

print(int(ip)+10)

#Quiz 1: Take Input from User and Add two number
num1=int(input("Please enter your 1st Number "))
num2=int(input("Please enter your 2nd Number "))
Addition=num1+num2
print("The sum of Two User Input Numbers is ",Addition)







