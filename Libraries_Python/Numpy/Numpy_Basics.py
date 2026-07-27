##This is a basic Numpy tutorial from Krish Naik's Udemy Course channel

import numpy as np

#print(dir(np))
# exit()


## create array using numpy
##create a 1D array
arr1=np.array([1,2,3,4,])
print(arr1)
print(type(arr1))
print(arr1.shape)

exit()


## 1 d array
arr2=np.array([1,2,3,4,5])
arr2.reshape(1,5)  ##1 row and 5 columns


arr2=np.array([[1,2,3,4,5]])
arr2.shape

## 2d array
arr2=np.array([[1,2,3,4,5],[2,3,4,5,6]])
print(arr2)
print(arr2.shape)

np.arange(0,10,2).reshape(5,1)

np.ones((3,4))

## identity matrix
np.eye(3)


## Attributes of Numpy Array
arr = np.array([[1, 2, 3], [4, 5, 6]])

print("Array:\n", arr)
print("Shape:", arr.shape)  # Output: (2, 3)
print("Number of dimensions:", arr.ndim)  # Output: 2
print("Size (number of elements):", arr.size)  # Output: 6
print("Data type:", arr.dtype)  # Output: int32 (may vary based on platform)
print("Item size (in bytes):", arr.itemsize)  # Output: 8 (may vary based on platform)


### Numpy Vectorized Operation
arr1=np.array([1,2,3,4,5])
arr2=np.array([10,20,30,40,50])

### Element Wise addition
print("Addition:", arr1+arr2)

## Element Wise Substraction
print("Substraction:", arr1-arr2)

# Element-wise multiplication
print("Multiplication:", arr1 * arr2)

# Element-wise division
print("Division:", arr1 / arr2)







## Universal Function
arr=np.array([2,3,4,5,6])
## square root
print(np.sqrt(arr))

## Exponential
print(np.exp(arr))

## Sine
print(np.sin(arr))

## natural log
print(np.log(arr))



## array slicing and Indexing

arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("Array : \n", arr)

print(arr[1:,1:3])


print(arr[0][0])
print(arr[0:2,2:])


arr[1:,2:]

## Modify array elements
arr[0,0]=100
print(arr)



arr[1:]=100
print(arr)



### statistical concepts--Normalization
##to have a mean of 0 and standard deviation of 1
data = np.array([1, 2, 3, 4, 5])

# Calculate the mean and standard deviation
mean = np.mean(data)
std_dev = np.std(data)

# Normalize the data
normalized_data = (data - mean) / std_dev
print("Normalized data:", normalized_data)



data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Mean
mean = np.mean(data)
print("Mean:", mean)

# Median
median = np.median(data)
print("Median:", median)

# Standard deviation
std_dev = np.std(data)
print("Standard Deviation:", std_dev)

# Variance
variance = np.var(data)
print("Variance:", variance)




## Logical operation
data=np.array([1,2,3,4,5,6,7,8,9,10])

data[(data>=5) & (data<=8)]




