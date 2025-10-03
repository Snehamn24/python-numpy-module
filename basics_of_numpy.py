#First we need to import the numpy module

import numpy as np
print(np.__version__)#knowing the numpy module version

#numpy is used to create the ndarray using the array()

#we can pass the tuple or the list to the array() which converts them to the ndarray

arr = np.array([1,2,3,4,5,6])

print(arr)

print("Type the passed Array is  ")

print(type(arr))


#Dimension of the Arrays in ndarray

# 0 - Dimensional

arr1 = np.array(90)
print("0 Dimension array ")
print(arr1)

# 1 - Dimesional array

arr2 = np.array([10,20,30])
print("1-Dimensional Array : ")
print(arr2)

# 2 - Dimesional array which takes the single dimension array as there elements

arr3 = np.array([[10,20],[30,40]])
print("2-dimensional array ")
print(arr3)


