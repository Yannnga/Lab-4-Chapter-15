"""
Program: Lab 4 - Sine Wave Plot
Author: Xinyi
Purpose: Plot the sine wave using matplotlib
Date: November 21, 2026

"""
import math
import matplotlib.pyplot as plt

# list for x and y
x = []
y = []

# Data
for i in range(0,100):
    x_value = round (i * 1 ,3)
    x.append(x_value)

    # math formula
    y_value =round(math.sin(x_value),3) # sine wave
    y.append(y_value)

print(x)
print(y)

print(len(x))
print(len(y))

# plot graph

# customize Plot

# save as png
