# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 16:08:34 2021

@author: ARPIT
"""
print("Hello World")

# Comments, Escape Sequence & Print Statement
print("Subscribe Now")
""" 
This is 
Multiline
Comment
"""
print("Please like the video")
print("Also Subscribe the vide")
print("Press the bell icon for more updates")


# New line character
print("Please like the video",end=", ") #after starts new line character.
""" 
end=",": means at the end of that sentence add comma before starting new line sentence.
Putting this satatement will atomaticall concat the next print statement with existing one separated by 
the conditions we have put on    

"""
print("Also Subscribe the video",end=".")
print("Press the bell icon for more updates")

#Multiple Statement in Single Print command
print("My name is Arpit", "I am 26 years old") 
"""The comma between two sentences automatically puts space between two statements"""

#Escape Character Sequence
print("C:\Arpit")
print("\nArpit") #here \n is new line escape character
print("C:\\Arpit")
print("\\nArpit")
print("C:\n""Arpit")
