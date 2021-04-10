# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def linearSearch(array, n, x):
    #Going through array sequencially
    for  i in range(0, n):
        if (array[i] == x):
            return i
    return -1
    
array = [2, 4, 0, 1, 9]
x = 1
n = len(array)
result = linearSearch(array, n, x)

if(result == -1):
    print("element not found")
else:
    print("element found at index:", result)
