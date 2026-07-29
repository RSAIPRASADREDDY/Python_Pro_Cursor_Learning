"""
Numpy Project: Working with Files - Beginner to Advanced

This project guides you through common practices of using Numpy for file I/O, as well as performing advanced data manipulations. You'll learn how to:

- Read and write data from/to text and CSV files using Numpy
- Practice basic and advanced data operations
- Manipulate, filter, and save data (including generating files of even numbers)
"""

import numpy as np

# ---------- Beginner Level: Loading and Saving Arrays ----------

# 1. Save a numpy array to a text file, and then read from it
arr = np.arange(1, 11).reshape(2,5)
# print(arr)
np.savetxt("array_data.txt", arr, fmt='%d')
print("Saved 1D array to array_data.txt")

# with open("array_data.txt", "r") as f:
#     for line in f:
#         print(line.strip())


loaded_arr = np.loadtxt("array_data.txt")
# print("Loaded array from text file:", loaded_arr)


# 2. Save and load 2D arrays
arr2d = np.arange(1, 13).reshape(3, 4)
np.savetxt("array2d_data.csv", arr2d, delimiter=',')
print("Saved 2D array to array2d_data.csv")

loaded_arr2d = np.loadtxt("array2d_data.csv", delimiter=',')
print("Loaded 2D array from CSV file:\n", loaded_arr2d)



# ---------- Intermediate Level: Using np.genfromtxt and np.save ----------

# 3. Saving array in binary ("npy") format and loading it
np.save("array_data.npy", arr2d)
loaded_npy = np.load("array_data.npy")
print("Loaded from npy file:\n", loaded_npy)

# 4. Handling CSV files with missing values
with open("test_missing.csv", "w") as f:
    f.write("1,2,3\n4,,6\n7,8,9")
arr_with_nan = np.genfromtxt("test_missing.csv", delimiter=',')
print("Loaded CSV with missing values:\n", arr_with_nan)

# ---------- Advanced Level: Data Filtering and File Generation ----------

# 5. Advanced filtering: Find and save only even numbers from a file
# Let's reuse arr, save only the even numbers to 'even_data.txt'
even_mask = arr % 2 == 0
even_arr = arr[even_mask]
np.savetxt("even_data.txt", even_arr, fmt='%d')
print("Even numbers saved to even_data.txt:", even_arr)

# Read back and confirm
even_loaded = np.loadtxt("even_data.txt")
print("Even data loaded:", even_loaded)

# 6. Practice: Read a random file, sort, deduplicate, and save results
random_data = np.random.randint(1, 100, 20)
np.savetxt("random_data.txt", random_data, fmt='%d')
print("Random data generated and saved:", random_data)

loaded_random = np.loadtxt("random_data.txt", dtype=int)
sorted_unique = np.unique(np.sort(loaded_random))
np.savetxt("sorted_unique_data.txt", sorted_unique, fmt='%d')
print("Sorted unique data saved to sorted_unique_data.txt:", sorted_unique)

# 7. BONUS: Saving and loading structured arrays
dtype = [('name', 'U10'), ('score', int)]
data = np.array([('Alice', 90), ('Bob', 85), ('Charlie', 88)], dtype=dtype)
np.savetxt("students.csv", data, fmt='%s,%d')
loaded_struct = np.genfromtxt("students.csv", delimiter=',', dtype=None, encoding=None)
print("Structured data loaded from CSV:\n", loaded_struct)

