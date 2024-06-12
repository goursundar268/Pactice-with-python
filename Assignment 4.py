# Write a program in matplotlib for creating a Pie chart.

import matplotlib.pyplot as plt

# Sample data (you can replace these with your own data)
labels = ['Apples', 'Bananas', 'Oranges', 'Grapes']
sizes = [30, 25, 20, 15]  # Percentages (sum should be 100)

# Create the Pie chart
plt.figure(figsize=(8, 6))  # Set figure size (optional)
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['r', 'g', 'b', 'y'])
plt.title('Fruit Distribution')

# Show the plot
plt.axis('equal')  # Equal aspect ratio ensures a circular pie chart
plt.show()