#Create a program to create a line graph for two different array using matplotlib.

import numpy as np
import matplotlib.pyplot as plt

# Create sample data (you can replace these arrays with your own data)
x_values = np.linspace(0, 10, 100)  # Generate 100 points between 0 and 10
y1_values = np.sin(x_values)       # Example function 1 (sine wave)
y2_values = np.cos(x_values)       # Example function 2 (cosine wave)

# Create the line graph
plt.figure(figsize=(8, 6))  # Set figure size (optional)
plt.plot(x_values, y1_values, label='sin(x)', color='b', linestyle='--')
plt.plot(x_values, y2_values, label='cos(x)', color='r', linestyle='-')

# Customize the plot
plt.title('Line Graph of sin(x) and cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()