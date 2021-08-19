# -*- coding: utf-8 -*-
"""
Topic: String Slicing And Other Functions In Python
Created on Mon Aug 16 23:14:05 2021

@author: ARPIT
"""
"""
                     A r p i t       i s               a           g  o  o  d         b  o  y
                     0 1 2 3 4   5   6 7     8         9   10     11 12 13 14   15   16 17 18
                   -18-17-16-15 -14 -13-12  -11      -10   -9     -8 -7 -6 -5   -4   -3 -2 -1
"""




mystr="Arpit is a good boy"
print(mystr)
print(len(mystr))
print(mystr[0])
print(mystr[0:5])
print(mystr[0:19])

print(mystr[78]) # Will show error
print(mystr[0:78]) #Will not show error

#Print by skipping one character
print(mystr[0:5:2]) # 0:start, 5:end, 2:offset
print(mystr[:5]) # In this case it will automatically consider from 0:5

print(mystr[::]) #In this case if we leave everything empty then by default it will consider as 1
print(mystr[0:19:1])


"Negative Indexing"
print(mystr[-4:-2])

"Reversing the String"
print(mystr[::-2])


print(mystr.isalnum()) #Checking for aphanumeric It will be alpha numeric if we remove spaces
print(mystr.isalpha())

print(mystr.endswith("bdoy"))
print(mystr.count("o"))

print(mystr.find("is"))
print(mystr.lower())

print(mystr.upper())
print(mystr.replace("is","are"))









