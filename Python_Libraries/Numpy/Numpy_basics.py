##This is a basic Numpy tutorial from Krish Naik's Udemy Course channel

from configparser import ExtendedInterpolation
import numpy as np

#print(dir(np))
# exit()


## create array using numpy
##create a 1D array
#arr1=np.array([1,2,3,4,])
arr1=np.array((1,2,3,4,))
# print(arr1)
# print(type(arr1))
# print(arr1.shape)
# print(arr1.reshape(4,1))

#a1=np.array([1,2,3,4,5])
#a1=np.array([[0,9,8,],[98,97,96]])
#a1=np.array([[0,9,8,],[98,97,96],[1,2,3]])
a1=np.array([[0,9,8,],[98,97,96],[1,2,3],[30,50,67]])


# print(type(a1))
# print("Shape of the array:",a1.shape)
# print("Number of dimensions:",a1.ndim)
# print("Size of the array:",a1.size)
# print("Data type of the array:",a1.dtype)
# print("Item size of the array:",a1.itemsize)
# print("Number of bytes in the array:",a1.nbytes)
# print("Real part of the array:",a1.real)


## 1 d array
arr2=np.array([1,2,3,4,5])
# print("Shape of the array:",arr2.shape)
# arr2.reshape(1,5)  ##1 row and 5 columns
# print(arr2.shape)
# print(arr2)

##2 D
arr2=np.array([[1,2,3,4,5]])
arr2.shape
# print(arr2.shape)
# print(arr2)



## 2d array
arr2=np.array([[1,2,3,4,5],[2,3,4,5,6]])
# print(arr2)
# print(arr2.shape)



a3=np.arange(0,10,2)
# print(a3)
# print(np.arange(0,10,2).reshape(5,1))

# print(np.ones((3,2)))

# ## identity matrix
# print(np.eye(3))


## Attributes of Numpy Array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# print("Array:\n", arr)
# print("Shape:", arr.shape)  # Output: (2, 3)
# print("Number of dimensions:", arr.ndim)  # Output: 2
# print("Size (number of elements):", arr.size)  # Output: 6
# print("Data type:", arr.dtype)  # Output: int32 (may vary based on platform)
# print("Item size (in bytes):", arr.itemsize)  # Output: 8 (may vary based on platform)


### Numpy Vectorized Operation
arr1=np.array([1,2,3,4,5,])
arr2=np.array([10,20,30,40,50])

### Element Wise addition
# print("Addition:", arr1+arr2)

# ## Element Wise Substraction
# print("Substraction:", arr1-arr2)

# # Element-wise multiplication
# print("Multiplication:", arr1 * arr2)

# # Element-wise division
# print("Division:", arr1 / arr2)







## Universal Function
arr=np.array([2,3,4,5,6])
## square root
# print(np.sqrt(arr))

# ## Exponential
# print(np.exp(arr))

# ## Sine
# print(np.sin(arr))

# ## natural log
# print(np.log(arr))



## array slicing and Indexing

arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print("Array : \n", arr)

# print(arr.shape)
# print(arr.reshape(4,3))
# print(arr.reshape(2,6))
# print(arr.reshape(6,2))
# print(arr.reshape(3,4))


# print(arr[1:,2:])
#print(arr[0:2,:2])
# print(arr[1:,1:3])
# print(arr[0:2,2:])
#print(arr[1:2,1:3])
# print(arr[2:,3:])




# print(arr[0][0])
# print(arr[0:2,2:])


#arr[1:,2:]

## Modify array elements
# arr[0,0]=100
# print(arr)



# arr[1:]=100
# print(arr)


# ------- PRACTICE: Array Creation -------
# 1D array
a1 = np.array([10, 20, 30])
print("1D array:", a1)

# 2D array
a2 = np.array([[1, 2], [3, 4]])
print("2D array:\n", a2)

# Zeros, Ones, arange, linspace
z = np.zeros((2,3))
print("Zeros array:\n", z)


o = np.ones((3,2))
print("Ones array:\n", o)

ar = np.arange(0, 10, 2)
print("np.arange:", ar)


ls = np.linspace(0, 1, 5)
print("np.linspace:", ls)


# ------- PRACTICE: Array Data Types -------
arr_float = np.array([1.3, 2, 3], dtype=float)
print("Array with float dtype:", arr_float)


arr_int = arr_float.astype(int)
print("Converted to int:", arr_int)

# ------- PRACTICE: Array Copy vs. View -------
original = np.array([1,2,3])
view = original.view()
copy = original.copy()
original[0] = 99
print("Original:", original)
print("View:", view)
print("Copy:", copy) # Remains unchanged

# ------- PRACTICE: Array Math Operations -------
arr1 = np.array([1, 2, 3])
arr2 = np.array([10, 20, 30])

add = arr1 + arr2
print("Addition:", add)

mult = arr1 * arr2
print("Multiplication:", mult)

div = arr2 / arr1
print("Division:", div)

# ------- PRACTICE: Numpy Aggregate Functions -------
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Sum (entire):", np.sum(arr))
print("Sum (axis=0):", np.sum(arr, axis=0))
print("Sum (axis=1):", np.sum(arr, axis=1))
print("Max:", np.max(arr))
print("Min:", np.min(arr))
print("Argmax:", np.argmax(arr))
print("Argmin:", np.argmin(arr))

# ------- PRACTICE: Fancy Indexing & Boolean Masking -------
arr = np.array([10, 21, 32, 43, 54])

# Boolean mask for even numbers
mask = arr % 2 == 0
print("Original array:", arr)
print("Even elements: ", arr[mask])


# Fancy indexing: select with list of indices
idx = [0, 1, 4]
print("Elements at 0,2,4:", arr[idx])

# ------- PRACTICE: Broadcasting -------
arr1 = np.array([[1],[2],[3]])
print("Array 1:\n", arr1)
print("Array 1:\n", arr1.shape)
arr2 = np.array([10,20,30,4])
print("Array 2:\n", arr2)
print("Array 2:\n", arr2.shape)
result = arr1 + arr2
print("Broadcasted addition:\n", result)


# ------- PRACTICE: Flatten, Ravel -------
mat = np.array([[1,2,3],[4,5,6]])
print("Flatten method:", mat.flatten())
print("Ravel method:", mat.ravel())

# ------- PRACTICE: Stacking Arrays -------
a = np.array([1,2,3])
b = np.array([4,5,6])
print("Vertical Stack:\n", np.vstack((a, b)))
print("Horizontal Stack:\n", np.hstack((a, b)))

# ------- PRACTICE: Split Arrays -------
mat = np.arange(16).reshape((4,4))
print("Original matrix:\n", mat)
print("Split vertically:", np.vsplit(mat,2))
print("Split horizontally:", np.hsplit(mat,2))

# ------- PRACTICE: Random Module -------
rand = np.random.rand(4)
print("Random rand:", rand)

randint = np.random.randint(1, 10, (2,3))
print("Random integers (2x3):\n", randint)

# Set seed for reproducibility
np.random.seed(42)
print("Random with seed:", np.random.rand(2))

# ------- PRACTICE: Sorting & Unique -------
arr = np.array([3,1,2,6,4,2,1])
print("Sorted:", np.sort(arr))
print("Unique:", np.unique(arr))












### statistical concepts--Normalization
##to have a mean of 0 and standard deviation of 1
data = np.array([1, 2, 3, 4, 5])

# Calculate the mean and standard deviation
mean = np.mean(data)
std_dev = np.std(data)
print("Mean:", mean)
print("Standard Deviation:", std_dev)


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




