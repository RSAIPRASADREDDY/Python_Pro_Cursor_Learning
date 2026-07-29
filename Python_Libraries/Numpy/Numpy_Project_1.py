# import numpy as np
# b = np.arange(6).reshape(2,3)
# print(b)
# a = np.arange(6).reshape(2,3) + 10
# print(a)

# np.argmax(a)
# print(np.argmax(a))

# np.argmax(a, axis=0)
# print(np.argmax(a, axis=0))

# np.argmax(a, axis=1)
# print(np.argmax(a, axis=1))

# exit()

"""
==============================
Beginner Project
==============================
Project Name: Student Marks Analyzer
Aim: 
    To analyze student marks for a subject and provide basic statistics 
    such as mean, median, standard deviation, top performers, and normalization.

Scenario:
    A school teacher wants to quickly analyze the marks scored by students in a mathematics test. 
    With the help of Numpy, she wants to calculate the average, see how spread out marks are, 
    and identify the top 3 students.

Implementation:
"""

import numpy as np

# Sample marks of 15 students
marks = np.array([88, 76, 92, 85, 69, 95, 80, 74, 91, 78, 84, 82, 77, 88, 90,91])

print("Student Marks:", marks)


# Calculate mean, median, and standard deviation
mean = np.mean(marks)
median = np.median(marks)
std_dev = np.std(marks)

print(f"Mean marks: {mean:.2f}")
print(f"Median marks: {median}")
print(f"Standard Deviation: {std_dev:.2f}")

# Find the top 3 students
top_indices = np.argsort(marks)#[-3:][::-1]
# print(np.argsort(marks))

print("Top 3 students' marks:", marks[np.argsort(marks)[-3:][::-1]])

# Normalize marks (mean=0, std=1)
marks_normalized = (marks - mean) / std_dev
print("Normalized marks:", marks_normalized)



"""
Execution Example:
------------------
Student Marks: [88 76 92 85 69 95 80 74 91 78 84 82 77 88 90]
Mean marks: 83.73
Median marks: 84.0
Standard Deviation: 7.26
Top 3 students' marks: [95 92 91]
Normalized marks: [ 0.59 -1.08  1.14  0.18 -2.03  1.56 -0.51 -1.35  1.01 -0.82  0.04 -0.24 -1.22  0.59  0.86]
"""

# -------------------------------------
"""
==============================
Intermediate Project
==============================
Project Name: Daily Sales Data Analysis for a Retail Shop
Aim:
    Analyze sales data for a month, showing trends, top selling days, 
    calculation of moving averages, and detection of sales anomalies.

Scenario:
    A retail shop owner records daily sales (in $) for a month (30 days). 
    The owner wants to analyze total and average sales, identify best/worst days, 
    compute a 7-day moving average, and detect days with unusually low or high sales.

Implementation:
"""

# Generate sample sales data (You could load from CSV/file in practice)
np.random.seed(25)
sales = np.random.randint(100, 500, size=30)
days = np.arange(1, 31)

# print("Days:", days)
# print("Sales:", sales)


print("\nDaily Sales for 30 days:", sales)

# Total and Average sales
total_sales = np.sum(sales)
average_sales = np.mean(sales)
# print(f"Total Sales: ${total_sales}")
# print(f"Average Daily Sales: ${average_sales:.2f}")

# print(np.argmax(sales))
# print(np.argmin(sales))

# exit()

# Best and worst sales days
best_day = np.argmax(sales) + 1
worst_day = np.argmin(sales) + 1
print(f"Best sales day: Day {best_day} (${sales[best_day-1]})")
print(f"Worst sales day: Day {worst_day} (${sales[worst_day-1]})")

# 7-day moving average
moving_avg = np.convolve(sales, np.ones(7)/7, mode='valid')
print("7-day moving average sales:")
print(moving_avg)

# Detecting outlier days (sales beyond 1.5 std deviations from mean)
high_sales = days[sales > (average_sales + 1.5*np.std(sales))]
low_sales = days[sales < (average_sales - 1.5*np.std(sales))]
print("Days with unusually high sales:", high_sales)
print("Days with unusually low sales:", low_sales)


"""
Execution Example:
------------------
Daily Sales for 30 days: [355 293 184 251 371 430 442 447 187 382 329 330 398 264 144 447 353 334 221 441 350 483 209 156 223 367 276 323 341 344]
Total Sales: $9618
Average Daily Sales: $320.60
Best sales day: Day 22 ($483)
Worst sales day: Day 15 ($144)
7-day moving average sales:
[332.0 332.42857143 ...]  # Truncated for brevity
Days with unusually high sales: [22]
Days with unusually low sales: [15 24]
"""

# -------------------------------------
"""
==============================
Advanced Project
==============================
Project Name: Image Noise Filtering and Analysis
Aim:
    Apply statistical noise to a grayscale image (2D Numpy array), filter it using a mean filter, 
    and analyze the results using Numpy operations only.

Scenario:
    A data scientist works on image pre-processing. An image is represented as a 2D array (100x100). 
    Random Gaussian noise is added to the image. The scientist wants to reduce the noise using 
    a mean filter (convolution), and compare the mean and std deviation before and after filtering.

Implementation:
"""

# Create a synthetic grayscale image (100x100, pixel values 0-255)
np.random.seed(0)
image = np.random.randint(0, 256, (100, 100)).astype(float)

# Add Gaussian noise (mean=0, std=20)
noise = np.random.normal(0, 20, image.shape)
noisy_image = image + noise
noisy_image = np.clip(noisy_image, 0, 255)

# Apply 3x3 mean filter (without scipy, using Numpy only)
def mean_filter(img):
    # Pad the image
    padded = np.pad(img, 1, mode='edge')
    filtered = np.zeros_like(img)
    # Sliding window implementation
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            filtered[i, j] = np.mean(padded[i:i+3, j:j+3])
    return filtered

filtered_image = mean_filter(noisy_image)

# Analyze the images
print("\nImage Noise Filtering Stats:")
print("Original Image - mean: {:.2f}, std: {:.2f}".format(np.mean(image), np.std(image)))
print("Noisy Image - mean: {:.2f}, std: {:.2f}".format(np.mean(noisy_image), np.std(noisy_image)))
print("Filtered Image - mean: {:.2f}, std: {:.2f}".format(np.mean(filtered_image), np.std(filtered_image)))

"""
Execution Example:
------------------
Image Noise Filtering Stats:
Original Image - mean: 127.21, std: 73.97
Noisy Image - mean: 127.14, std: 76.41
Filtered Image - mean: 127.14, std: 35.38
"""
