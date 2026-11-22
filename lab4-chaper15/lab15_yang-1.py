"""
Program: Lab 4 - Sine Wave Plot
Author: Xinyi
Purpose: Plot the sine wave and damped oscillation using matplotlib
Date: November 21, 2026

"""
import math
import matplotlib.pyplot as plt

# list for x and y
x = []
#y = []
y_damped = []

# Physical parameters
A = 1.0
gamma = 0.3
omega = 2.0


# Data
for i in range(0,100):
    x_value = round (i * 0.1 ,3)
    x.append(x_value)

    # math formula
    #y_value =round(math.sin(x_value),3) # sine wave
    y_damped_value = round(A * math.exp(-gamma * x_value) * math.cos(omega * x_value), 3) #Damped oscillation
    
    #y.append(y_value)
    y_damped.append(y_damped_value)
    

#print(x)
#print(y)

#print(len(x))
#print(len(y))

# plot graph
#plt.plot(x, y)
plt.plot(x, y_damped, color="blue", linewidth=5)

# customize Plot
#plt.title("Sine Wave")
#plt.xlabel("x")
#plt.ylabel("sin(x)")

plt.title("Damped Oscillation")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")

# save as png
plt.savefig("damped_oscillation.png")
plt.show()