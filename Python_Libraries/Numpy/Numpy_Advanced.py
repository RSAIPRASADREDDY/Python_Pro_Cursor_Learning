'''
I'll create a comprehensive NumPy tutorial that covers everything from beginner to advanced level. 
Let me start by creating a structured tutorial with practical examples.

Ran tool
# Complete NumPy Tutorial: From Beginner to Advanced

## Table of Contents
1. [Introduction and Installation](#introduction-and-installation)
2. [Basic Array Operations](#basic-array-operations)
3. [Data Types and Array Creation](#data-types-and-array-creation)
4. [Indexing and Slicing](#indexing-and-slicing)
5. [Mathematical Operations](#mathematical-operations)
6. [Array Manipulation and Reshaping](#array-manipulation-and-reshaping)
7. [Statistical Functions](#statistical-functions)
8. [Linear Algebra](#linear-algebra)
9. [Broadcasting](#broadcasting)
10. [Advanced Operations](#advanced-operations)
11. [Performance Optimization](#performance-optimization)
12. [Practical Examples](#practical-examples)

---

## Introduction and Installation

Ran tool
### What is NumPy?

**NumPy** (Numerical Python) is the fundamental package for scientific computing in Python. It provides:
- **N-dimensional arrays** (ndarray)
- **Mathematical functions** for array operations
- **Linear algebra** capabilities
- **Random number generation**
- **Integration with C/C++ and Fortran**

### Installation
'''
#```python
# Install NumPy
#pip install numpy

# Or with conda
#conda install numpy

# Import NumPy
import numpy as np


# Python lists vs NumPy arrays
import time
# print(help(dir(time)))
# exit()

# Python lists
python_list = list(range(10))
start_time = time.time()    #Give us the current time in seconds
result = [x * 2 for x in python_list]
python_time = time.time() - start_time

# print("Python list time:", python_list)
# #print(time.time())
# print(result)
# print(python_time)



# NumPy arrays
numpy_array = np.arange(1000000)
#print("Numpy array:", numpy_array)
start_time = time.time()
result = numpy_array * 2
numpy_time = time.time() - start_time



# print(f"Python list time: {python_time:.4f} seconds")
# print(f"NumPy array time: {numpy_time:.4f} seconds")
# print(f"NumPy is {python_time/numpy_time:.1f}x faster!")




## Basic Array Operations

### Creating Arrays



import numpy as np

# 1. From Python lists
arr1 = np.array((1, 2, 3, 4, 5))
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
#arr3 = np.array([[1], [42], [7], [23], [1],5.5])   #np.array() can accept heterogeneous input, but it prefers one dtype — mixed data gets cast or stored as object
#print(arr1)
# print(arr2)
#print(arr3)

# 2. Using built-in functions
zeros = np.zeros((3, 4))          # Array of zeros
ones = np.ones((2, 3))            # Array of ones
full = np.full((2, 2), -1)         # Array filled with value
eye = np.eye(3)                   # Identity matrix
random = np.random.random((2, 3)) # Random array

# print(zeros)
# print(ones)
# print(full)
# # print(eye)
# print(random)
# print("--------------------------------")


# 3. Using arange and linspace
range_arr = np.arange(0, 10, 2)   # [0, 2, 4, 6, 8]
linspace_arr = np.linspace(0, 1, 3)  # [0, 0.25, 0.5, 0.75, 1]

# print("Array shapes:")
# print(f"arr1 shape: {arr1.shape}")
# print(f"arr2 shape: {arr2.shape}")
# print(f"arr2 dimensions: {arr2.ndim}")
# print(f"arr2 size: {arr2.size}")
# print(range_arr)
# print(linspace_arr)



# Array properties
arr = np.array([[1, 2, 3], [4, 5, 6]])

# print(f"Shape: {arr.shape}")           # (2, 3)
# print(f"Dimensions: {arr.ndim}")       # 2
# print(f"Size: {arr.size}")             # 6
# print(f"Data type: {arr.dtype}")       # int64
# print(f"Item size: {arr.itemsize}")    # 8 bytes
# print(f"Total bytes: {arr.nbytes}")    # 48 bytes



## Data Types and Array Creation



### Data Types


# Specifying data types
arr_int = np.array([1, 2, 3], dtype=np.int32)
arr_float = np.array([1.0, 2.0, 3.0], dtype=np.float64)
arr_complex = np.array([1+2j, 3+4j], dtype=np.complex128)
arr_bool = np.array([True, False, True], dtype=np.bool_)

# Converting data types
arr = np.array([1, 2, 3, 4])
arr_float = arr.astype(np.float32)
arr_string = arr.astype(np.str_)

# print(f"Original: {arr.dtype}")
# print(f"Float: {arr_float.dtype}")
# print(f"String: {arr_string.dtype}")



### Array Creation Methods



# Different ways to create arrays
# 1. From existing data
data = [1, 2, 3, 4, 5]
arr1 = np.array(data)

# 2. From ranges
arr2 = np.arange(0, 10, 2)        # [0, 2, 4, 6, 8]
arr3 = np.linspace(0, 1, 5)       # [0, 0.25, 0.5, 0.75, 1]

# 3. Special arrays
zeros = np.zeros((3, 4))
ones = np.ones((2, 3))
empty = np.empty((2, 2))          # Uninitialized
identity = np.eye(3)              # Identity matrix
diagonal = np.diag([1, 2, 3])     # Diagonal matrix

# 4. Random arrays
random_uniform = np.random.random((2, 3))      # [0, 1)
random_normal = np.random.normal(0, 15, (2, 3)) # Normal distribution
random_int = np.random.randint(0, 10, (2, 3))  # Random integers


# print(random_uniform)
# print(random_normal)
# print(random_int)
# print(empty)
# print(identity)
# print(diagonal)



# 5. From functions
def f(x, y):
    return x + y

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
result = f(x, y)  # Vectorized operation

# print(result)



## Indexing and Slicing

### Basic Indexing



# 1D array indexing
arr = np.array([10, 20, 30, 40, 50])
# print(f"First element: {arr[0]}")
# print(f"Last element: {arr[-1]}")
# print(f"Second to fourth: {arr[1:4]}")



# 2D array indexing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(f"Element at (1, 2): {arr2d[1, 2]}")
# print(f"First row: {arr2d[0, :]}")
# print(f"Second column: {arr2d[:, 1]}")
# print(f"Subarray: {arr2d[0:2, 1:3]}")



### Advanced Indexing



# Boolean indexing
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
mask = arr > 5
# print(f"Elements > 5: {arr[mask]}")

# # Multiple conditions
# mask2 = (arr > 3) & (arr < 8)
# print(f"Elements between 3 and 8: {arr[mask2]}")

# # Fancy indexing
# indices = [0, 2, 4]
# print(f"Elements at indices {indices}: {arr[indices]}")

# # 2D boolean indexing
# arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# mask = arr2d > 5
# print(f"Elements > 5:\n{arr2d[mask]}")



### Slicing with Steps



arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# # Basic slicing
# print(f"First 5 elements: {arr[:5]}")
# print(f"Last 3 elements: {arr[-3:]}")
# print(f"Every 2nd element: {arr[::2]}")
# print(f"Reverse array: {arr[::-1]}")

# 2D slicing
arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(f"Every other row:\n{arr2d[::2]}")
# print(f"Every other column:\n{arr2d[:, ::2]}")



## Mathematical Operations



### Element-wise Operations



# Basic arithmetic
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# print(f"Addition: {a + b}")
# print(f"Subtraction: {a - b}")
# print(f"Multiplication: {a * b}")
# print(f"Division: {a / b}")
# print(f"Power: {a ** 2}")
# print(f"Modulo: {a % 3}")

# Scalar operations
# print(f"Add 5: {a + 5}")
# print(f"Multiply by 2: {a * 2}")
# print(f"Square root: {np.sqrt(a)}")



### Universal Functions (ufuncs)



arr = np.array([1, 4, 9, 16, 25])

# Mathematical functions
# print(f"Square root: {np.sqrt(arr)}")
# print(f"Exponential: {np.exp(arr)}")
# print(f"Logarithm: {np.log(arr)}")
# print(f"Sine: {np.sin(arr)}")
# print(f"Cosine: {np.cos(arr)}")

# Comparison functions
a = np.array([1, 2, 3])
b = np.array([2, 2, 4])
# print(f"Equal: {np.equal(a, b)}")
# print(f"Greater: {np.greater(a, b)}")
# print(f"Maximum: {np.maximum(a, b)}")
# print(f"Minimum: {np.minimum(a, b)}")


### Aggregation Functions



arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Basic aggregations
# print(f"Sum: {np.sum(arr)}")
# print(f"Mean: {np.mean(arr)}")
# print(f"Standard deviation: {np.std(arr)}")
# print(f"Variance: {np.var(arr)}")
# print(f"Min: {np.min(arr)}")
# print(f"Max: {np.max(arr)}")

# Along axes
# print(f"Sum along axis 0 (columns): {np.sum(arr, axis=0)}")
# print(f"Sum along axis 1 (rows): {np.sum(arr, axis=1)}")
# print(f"Mean along axis 0: {np.mean(arr, axis=0)}")

# # Other useful functions
# print(f"Product: {np.prod(arr)}")
# print(f"Cumulative sum: {np.cumsum(arr)}")
# print(f"Argmax: {np.argmax(arr)}")
# print(f"Argmin: {np.argmin(arr)}")


## Array Manipulation and Reshaping


# Reshaping
arr = np.arange(12)
# print(f"Original: {arr}")

# Reshape to 3x4
reshaped = arr.reshape(3, 4)
# print(f"Reshaped to 3x4:\n{reshaped}")

# Reshape to 2x6
reshaped2 = arr.reshape(2, 6)
# print(f"Reshaped to 2x6:\n{reshaped2}")

# Flatten
flattened = reshaped.flatten()
# print(f"Flattened: {flattened}")

# Reshape with -1 (automatic dimension)
auto_reshape = arr.reshape(3, -1)  # -1 means "calculate this dimension"
# print(f"Auto reshape (3, -1):\n{auto_reshape}")


### Array Concatenation and Splitting



# Concatenation
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 1D concatenation
concat_1d = np.concatenate([a, b])
# print(f"Concatenated 1D: {concat_1d}")

# 2D concatenation
a2d = np.array([[1, 2], [3, 4]])
b2d = np.array([[5, 6], [7, 8]])

# Along axis 0 (rows)
# concat_rows = np.concatenate([a2d, b2d], axis=0)
# print(f"Concatenated along rows:\n{concat_rows}")

# Along axis 1 (columns)
concat_cols = np.concatenate([a2d, b2d], axis=1)
# print(f"Concatenated along columns:\n{concat_cols}")

# Using vstack and hstack
vstacked = np.vstack([a2d, b2d])
hstacked = np.hstack([a2d, b2d])
# print(f"Vstacked:\n{vstacked}")
# print(f"Hstacked:\n{hstacked}")

# Splitting
arr = np.arange(12).reshape(3, 4)
split_arrays = np.split(arr, 3, axis=0)  # Split into 3 parts along axis 0
# print(f"Split arrays: {[arr.shape for arr in split_arrays]}")



### Array Transposition and Swapping


# Transposition
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# transposed = arr.T
# print(f"Original:\n{arr}")
# print(f"Transposed:\n{transposed}")

# # Swapping axes
# arr3d = np.arange(24).reshape(2, 3, 4)
# swapped = np.swapaxes(arr3d, 0, 2)  # Swap axes 0 and 2
# print("Original 3D array:\n"+ str(arr3d))
# print("Swapped 3D array:\n"+ str(swapped))
# print(f"Original shape: {arr3d.shape}")
# print(f"Swapped shape: {swapped.shape}")

# # Rolling axes
# rolled = np.rollaxis(arr3d, 2, 0)  # Move axis 2 to position 0
# #print("Rolled 3D array:\n"+ (rolled))
# print(f"Rolled shape: {rolled.shape}")







## Statistical Functions

#Ran tool
### Descriptive Statistics


# Generate sample data
np.random.seed(42)
data = np.random.normal(100, 15, 1000)  # Normal distribution
# print(np.random.seed(42))
# print(data)
# exit()


# Basic statistics
# print(f"Mean: {np.mean(data):.2f}")
# print(f"Median: {np.median(data):.2f}")
# print(f"Mode: {np.argmax(np.bincount(data.astype(int)))}")
# print(f"Standard deviation: {np.std(data):.2f}")
# print(f"Variance: {np.var(data):.2f}")
# print(f"Min: {np.min(data):.2f}")
# print(f"Max: {np.max(data):.2f}")
# print(f"Range: {np.ptp(data):.2f}")  # Peak-to-peak (max - min)

# # Percentiles
# print(f"25th percentile: {np.percentile(data, 25):.2f}")
# print(f"50th percentile: {np.percentile(data, 50):.2f}")
# print(f"75th percentile: {np.percentile(data, 75):.2f}")
# print(f"90th percentile: {np.percentile(data, 90):.2f}")

# # Quantiles
# quantiles = np.quantile(data, [0.25, 0.5, 0.75])
# print(f"Quantiles: {quantiles}")





### Correlation and Covariance

# Generate correlated data
np.random.seed(42)
x = np.random.normal(0, 1, 100)
y = 2 * x + np.random.normal(0, 0.5, 100)  # y is correlated with x

# Correlation
correlation = np.corrcoef(x, y)[0, 1]
print(f"Correlation coefficient: {correlation:.3f}")

# Covariance
covariance = np.cov(x, y)
print(f"Covariance matrix:\n{covariance}")

# Cross-correlation
cross_corr = np.correlate(x, y, mode='full')
print(f"Cross-correlation length: {len(cross_corr)}")


## Linear Algebra

### Matrix Operations


# Matrix creation
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
C = np.dot(A, B)
print(f"Matrix multiplication:\n{C}")

# Alternative syntax
C_alt = A @ B
print(f"Using @ operator:\n{C_alt}")

# Element-wise multiplication
D = A * B
print(f"Element-wise multiplication:\n{D}")

# Matrix properties
print(f"Determinant: {np.linalg.det(A):.2f}")
print(f"Trace: {np.trace(A)}")
print(f"Rank: {np.linalg.matrix_rank(A)}")


### Eigenvalues and Eigenvectors

# Eigenvalues and eigenvectors
eigenvals, eigenvecs = np.linalg.eig(A)
print(f"Eigenvalues: {eigenvals}")
print(f"Eigenvectors:\n{eigenvecs}")

# Verify: A * v = λ * v
for i in range(len(eigenvals)):
    v = eigenvecs[:, i]
    λ = eigenvals[i]
    result = A @ v
    expected = λ * v
    print(f"Eigenvalue {i}: {np.allclose(result, expected)}")


### Solving Linear Systems


# Solve linear system Ax = b
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])

# Solve using linalg.solve
x = np.linalg.solve(A, b)
print(f"Solution x: {x}")

# Verify: Ax = b
verification = A @ x
print(f"Verification (Ax): {verification}")
print(f"Original b: {b}")
print(f"Close enough: {np.allclose(verification, b)}")

# Matrix inverse
A_inv = np.linalg.inv(A)
x_alt = A_inv @ b
print(f"Solution using inverse: {x_alt}")


## Broadcasting

### Understanding Broadcasting

# Broadcasting examples
a = np.array([1, 2, 3])
b = np.array([[1], [2], [3]])

print(f"a shape: {a.shape}")
print(f"b shape: {b.shape}")

# Broadcasting in action
result = a + b
print(f"Broadcasted result:\n{result}")
print(f"Result shape: {result.shape}")

# More complex broadcasting
arr1 = np.array([[1, 2, 3], [4, 5, 6]])  # Shape: (2, 3)
arr2 = np.array([10, 20, 30])             # Shape: (3,)

result = arr1 + arr2
print(f"Broadcasting (2,3) + (3,):\n{result}")

# 3D broadcasting
arr3d = np.arange(24).reshape(2, 3, 4)
arr1d = np.array([1, 2, 3, 4])

result = arr3d + arr1d
print(f"3D broadcasting result shape: {result.shape}")


### Broadcasting Rules


# Broadcasting rules demonstration
def can_broadcast(shape1, shape2):
    """Check if two shapes can be broadcast together"""
    # Pad shorter shape with 1s on the left
    max_len = max(len(shape1), len(shape2))
    shape1_padded = (1,) * (max_len - len(shape1)) + shape1
    shape2_padded = (1,) * (max_len - len(shape2)) + shape2
    
    for s1, s2 in zip(shape1_padded, shape2_padded):
        if s1 != s2 and s1 != 1 and s2 != 1:
            return False
    return True

# Test cases
test_cases = [
    ((3,), (3,)),      # Same shape
    ((3,), (1,)),      # One is 1
    ((3,), (3, 1)),    # Different dimensions
    ((2, 3), (3,)),    # Compatible
    ((2, 3), (2,)),    # Incompatible
]

for shape1, shape2 in test_cases:
    print(f"Shapes {shape1} and {shape2}: {can_broadcast(shape1, shape2)}")



## Advanced Operations

### Rolling and Shifting



# Rolling operations
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Rolling mean (using convolution)
def rolling_mean(arr, window):
    return np.convolve(arr, np.ones(window)/window, mode='valid')

rolling_avg = rolling_mean(data, 3)
print(f"Rolling mean (window=3): {rolling_avg}")

# Shifting
shifted_right = np.roll(data, 2)
shifted_left = np.roll(data, -2)
print(f"Original: {data}")
print(f"Shifted right by 2: {shifted_right}")
print(f"Shifted left by 2: {shifted_left}")

# Rolling window operations
def rolling_window(arr, window):
    """Create rolling window view of array"""
    shape = arr.shape[:-1] + (arr.shape[-1] - window + 1, window)
    strides = arr.strides + (arr.strides[-1],)
    return np.lib.stride_tricks.as_strided(arr, shape=shape, strides=strides)

# Example: rolling sum
arr = np.array([1, 2, 3, 4, 5, 6])
windowed = rolling_window(arr, 3)
rolling_sums = np.sum(windowed, axis=1)
print(f"Rolling sums (window=3): {rolling_sums}")



### DateTime Manipulation



# Working with dates
import numpy as np

# Create datetime arrays
dates = np.array(['2023-01-01', '2023-01-02', '2023-01-03'], dtype='datetime64')
print(f"Dates: {dates}")

# Date arithmetic
one_day = np.timedelta64(1, 'D')
tomorrow = dates + one_day
print(f"Tomorrow: {tomorrow}")

# Date range
date_range = np.arange('2023-01-01', '2023-01-10', dtype='datetime64[D]')
print(f"Date range: {date_range}")

# Extract components
years = dates.astype('datetime64[Y]').astype(int) + 1970
months = dates.astype('datetime64[M]').astype(int) % 12 + 1
days = dates.astype('datetime64[D]').astype(int) % 365 + 1

print(f"Years: {years}")
print(f"Months: {months}")
print(f"Days: {days}")

# Business days
business_days = np.busday_count('2023-01-01', '2023-01-31')
print(f"Business days in January 2023: {business_days}")
### Advanced Indexing Techniques



# Advanced indexing examples
arr = np.arange(12).reshape(3, 4)
print(f"Original array:\n{arr}")

# Integer array indexing
rows = np.array([0, 1, 2])
cols = np.array([0, 1, 2])
selected = arr[rows, cols]
print(f"Selected elements: {selected}")

# Boolean array indexing
mask = arr > 5
print(f"Elements > 5: {arr[mask]}")

# Mixed indexing
row_indices = [0, 2]
col_mask = np.array([True, False, True, False])
mixed_selection = arr[row_indices][:, col_mask]
print(f"Mixed selection:\n{mixed_selection}")

# Using where
result = np.where(arr > 5, arr, 0)
print(f"Where condition:\n{result}")

# Using select
conditions = [arr < 3, arr < 6, arr < 9]
choices = [0, 1, 2]
selected = np.select(conditions, choices, default=3)
print(f"Select result:\n{selected}")



## Performance Optimization

#Ran tool
### Memory Layout and Performance



import time

# Row-major vs Column-major access
arr = np.random.random((1000, 1000))

# Row-major access (faster)
start_time = time.time()
for i in range(1000):
    for j in range(1000):
        _ = arr[i, j]
row_major_time = time.time() - start_time

# Column-major access (slower)
start_time = time.time()
for j in range(1000):
    for i in range(1000):
        _ = arr[i, j]
col_major_time = time.time() - start_time

print(f"Row-major time: {row_major_time:.4f}s")
print(f"Column-major time: {col_major_time:.4f}s")
print(f"Speedup: {col_major_time/row_major_time:.2f}x")

# Memory layout
print(f"C-contiguous: {arr.flags.c_contiguous}")
print(f"F-contiguous: {arr.flags.f_contiguous}")



### Vectorization vs Loops



# Loop-based approach
def loop_sum(arr):
    result = 0
    for i in range(len(arr)):
        result += arr[i]
    return result

# Vectorized approach
def vectorized_sum(arr):
    return np.sum(arr)

# Performance comparison
arr = np.random.random(1000000)

# Loop approach
start_time = time.time()
loop_result = loop_sum(arr)
loop_time = time.time() - start_time

# Vectorized approach
start_time = time.time()
vectorized_result = vectorized_sum(arr)
vectorized_time = time.time() - start_time

print(f"Loop time: {loop_time:.4f}s")
print(f"Vectorized time: {vectorized_time:.4f}s")
print(f"Speedup: {loop_time/vectorized_time:.2f}x")
print(f"Results equal: {np.allclose(loop_result, vectorized_result)}")


### Memory Optimization



# Memory usage analysis
def memory_usage(arr):
    return arr.nbytes / (1024 * 1024)  # MB

# Different data types
arr_int32 = np.arange(1000000, dtype=np.int32)
arr_int64 = np.arange(1000000, dtype=np.int64)
arr_float32 = np.arange(1000000, dtype=np.float32)
arr_float64 = np.arange(1000000, dtype=np.float64)

print(f"int32 memory: {memory_usage(arr_int32):.2f} MB")
print(f"int64 memory: {memory_usage(arr_int64):.2f} MB")
print(f"float32 memory: {memory_usage(arr_float32):.2f} MB")
print(f"float64 memory: {memory_usage(arr_float64):.2f} MB")

# Memory-efficient operations
# Use in-place operations when possible
arr = np.random.random(1000)
arr_inplace = arr.copy()

# Regular operation (creates new array)
result1 = arr * 2

# In-place operation (modifies existing array)
arr_inplace *= 2

print(f"Original array modified: {np.array_equal(arr, arr_inplace)}")



## Practical Examples

### Example 1: Image Processing



# Simulate image processing
def create_sample_image(height, width):
    """Create a sample grayscale image"""
    return np.random.randint(0, 256, (height, width), dtype=np.uint8)

def apply_gaussian_blur(image, kernel_size=5):
    """Apply Gaussian blur to image"""
    # Create Gaussian kernel
    kernel = np.zeros((kernel_size, kernel_size))
    center = kernel_size // 2
    sigma = 1.0
    
    for i in range(kernel_size):
        for j in range(kernel_size):
            kernel[i, j] = np.exp(-((i-center)**2 + (j-center)**2) / (2*sigma**2))
    
    kernel = kernel / np.sum(kernel)
    
    # Apply convolution (simplified)
    blurred = np.zeros_like(image, dtype=np.float32)
    h, w = image.shape
    k_h, k_w = kernel.shape
    
    for i in range(k_h//2, h - k_h//2):
        for j in range(k_w//2, w - k_w//2):
            blurred[i, j] = np.sum(image[i-k_h//2:i+k_h//2+1, j-k_w//2:j+k_w//2+1] * kernel)
    
    return blurred.astype(np.uint8)

# Example usage
image = create_sample_image(100, 100)
blurred = apply_gaussian_blur(image)
print(f"Original image shape: {image.shape}")
print(f"Blurred image shape: {blurred.shape}")



### Example 2: Financial Data Analysis


# Simulate stock price data
np.random.seed(42)
days = 252  # Trading days in a year
initial_price = 100
returns = np.random.normal(0.001, 0.02, days)  # Daily returns
prices = initial_price * np.cumprod(1 + returns)

# Calculate technical indicators
def calculate_sma(prices, window):
    """Simple Moving Average"""
    return np.convolve(prices, np.ones(window)/window, mode='valid')

def calculate_rsi(prices, window=14):
    """Relative Strength Index"""
    deltas = np.diff(prices)
    gains = np.where(deltas > 0, deltas, 0)
    losses = np.where(deltas < 0, -deltas, 0)
    
    avg_gains = np.convolve(gains, np.ones(window)/window, mode='valid')
    avg_losses = np.convolve(losses, np.ones(window)/window, mode='valid')
    
    rs = avg_gains / avg_losses
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Calculate indicators
sma_20 = calculate_sma(prices, 20)
sma_50 = calculate_sma(prices, 50)
rsi = calculate_rsi(prices)

print(f"Price range: ${prices.min():.2f} - ${prices.max():.2f}")
print(f"SMA 20: {sma_20[-1]:.2f}")
print(f"SMA 50: {sma_50[-1]:.2f}")
print(f"RSI: {rsi[-1]:.2f}")


### Example 3: Data Preprocessing for Machine Learning



# Simulate dataset
np.random.seed(42)
n_samples = 1000
n_features = 5

# Generate features
X = np.random.normal(0, 1, (n_samples, n_features))
# Add some missing values
missing_indices = np.random.choice(n_samples * n_features, 50, replace=False)
X.flat[missing_indices] = np.nan

# Generate target variable
y = 2 * X[:, 0] + 3 * X[:, 1] - X[:, 2] + np.random.normal(0, 0.1, n_samples)

def preprocess_data(X, y):
    """Preprocess data for machine learning"""
    # Handle missing values
    X_clean = X.copy()
    for i in range(X.shape[1]):
        col = X[:, i]
        if np.any(np.isnan(col)):
            # Fill with median
            median_val = np.nanmedian(col)
            X_clean[:, i] = np.where(np.isnan(col), median_val, col)
    
    # Normalize features
    X_normalized = (X_clean - np.mean(X_clean, axis=0)) / np.std(X_clean, axis=0)
    
    # Remove outliers (using IQR method)
    Q1 = np.percentile(X_normalized, 25, axis=0)
    Q3 = np.percentile(X_normalized, 75, axis=0)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outlier_mask = np.all((X_normalized >= lower_bound) & (X_normalized <= upper_bound), axis=1)
    X_clean = X_normalized[outlier_mask]
    y_clean = y[outlier_mask]
    
    return X_clean, y_clean

# Preprocess data
X_processed, y_processed = preprocess_data(X, y)
print(f"Original shape: {X.shape}")
print(f"Processed shape: {X_processed.shape}")
print(f"Missing values in processed data: {np.isnan(X_processed).sum()}")



### Example 4: Signal Processing



# Generate signal
t = np.linspace(0, 1, 1000)
frequency1 = 5
frequency2 = 20
signal = np.sin(2 * np.pi * frequency1 * t) + 0.5 * np.sin(2 * np.pi * frequency2 * t)
noise = 0.1 * np.random.normal(0, 1, len(t))
noisy_signal = signal + noise

def apply_low_pass_filter(signal, cutoff_freq, sampling_rate):
    """Apply low-pass filter using moving average"""
    window_size = int(sampling_rate / cutoff_freq)
    if window_size % 2 == 0:
        window_size += 1
    
    # Create moving average filter
    filtered = np.convolve(signal, np.ones(window_size)/window_size, mode='same')
    return filtered

def calculate_fft(signal, sampling_rate):
    """Calculate FFT of signal"""
    fft = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal), 1/sampling_rate)
    return fft, freqs

# Apply filtering
filtered_signal = apply_low_pass_filter(noisy_signal, 10, 1000)

# Calculate FFT
fft_original, freqs = calculate_fft(signal, 1000)
fft_noisy, _ = calculate_fft(noisy_signal, 1000)
fft_filtered, _ = calculate_fft(filtered_signal, 1000)

print(f"Signal length: {len(signal)}")
print(f"Sampling rate: 1000 Hz")
print(f"Filtered signal shape: {filtered_signal.shape}")
print(f"FFT shape: {fft_original.shape}")


### Example 5: Monte Carlo Simulation



def monte_carlo_pi(n_samples):
    """Estimate π using Monte Carlo method"""
    # Generate random points in unit square
    x = np.random.uniform(0, 1, n_samples)
    y = np.random.uniform(0, 1, n_samples)
    
    # Count points inside unit circle
    distances = np.sqrt(x**2 + y**2)
    inside_circle = np.sum(distances <= 1)
    
    # Estimate π
    pi_estimate = 4 * inside_circle / n_samples
    return pi_estimate

def monte_carlo_integration(func, a, b, n_samples):
    """Estimate integral using Monte Carlo method"""
    # Generate random points
    x = np.random.uniform(a, b, n_samples)
    
    # Calculate function values
    y = func(x)
    
    # Estimate integral
    integral_estimate = (b - a) * np.mean(y)
    return integral_estimate

# Example 1: Estimate π
pi_estimates = []
for n in [1000, 10000, 100000, 1000000]:
    pi_est = monte_carlo_pi(n)
    pi_estimates.append(pi_est)
    print(f"n={n}: π ≈ {pi_est:.6f} (error: {abs(pi_est - np.pi):.6f})")

# Example 2: Estimate integral of x² from 0 to 1
def f(x):
    return x**2

integral_estimates = []
for n in [1000, 10000, 100000]:
    integral_est = monte_carlo_integration(f, 0, 1, n)
    integral_estimates.append(integral_est)
    true_value = 1/3
    print(f"n={n}: ∫x²dx ≈ {integral_est:.6f} (error: {abs(integral_est - true_value):.6f})")


'''
Ran tool
## Summary

This comprehensive NumPy tutorial covers:

1. **Fundamentals**: Array creation, data types, basic operations
2. **Indexing**: Basic and advanced indexing techniques
3. **Mathematics**: Element-wise operations, universal functions, statistics
4. **Manipulation**: Reshaping, concatenation, transposition
5. **Linear Algebra**: Matrix operations, eigenvalues, solving systems
6. **Advanced Topics**: Broadcasting, rolling operations, datetime handling
7. **Performance**: Optimization techniques and memory management
8. **Practical Examples**: Real-world applications in various domains

### Key Takeaways:

- **NumPy is the foundation** for scientific computing in Python
- **Vectorization** is key to performance - avoid loops when possible
- **Broadcasting** allows operations between arrays of different shapes
- **Memory layout** affects performance significantly
- **Practice with real data** to master NumPy effectively

### Next Steps:

1. **Practice regularly** with the examples provided
2. **Work on real projects** using NumPy
3. **Explore related libraries** like Pandas, SciPy, and Matplotlib
4. **Learn advanced topics** like custom ufuncs and C extensions
5. **Contribute to open source** projects using NumPy

This tutorial provides a solid foundation for mastering NumPy. 
The key to proficiency is consistent practice and applying these concepts to real-world problems!
'''
