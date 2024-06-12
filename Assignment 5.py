# Write a Program to demonstrate Scipy and its functions.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import minimize
from scipy.interpolate import interp1d
from scipy.linalg import solve
from scipy.stats import norm
from scipy.special import jv

# Example 1: Numerical Integration
def my_function(x):
    return x**2

result, _ = quad(my_function, 0, 2)
print(f"Definite integral of x^2 from 0 to 2: {result:.4f}")

# Example 2: Optimization
def objective(x):
    return x**2 + 3*x + 5

min_result = minimize(objective, 0)
print(f"Minimum value of x^2 + 3x + 5: {min_result.fun:.4f} at x = {min_result.x[0]:.4f}")

# Example 3: Interpolation
x_data = np.linspace(0, 10, 5)
y_data = np.sin(x_data)
interp_func = interp1d(x_data, y_data, kind='cubic')
x_interp = np.linspace(0, 10, 100)
y_interp = interp_func(x_interp)

# Example 4: Linear Algebra
A = np.array([[2, 1], [1, 3]])
b = np.array([3, 4])
x_solution = solve(A, b)
print(f"Solution of Ax = b: x = {x_solution}")

# Example 5: Statistics
data = np.random.normal(loc=5, scale=2, size=100)
mean_value = np.mean(data)
std_dev = np.std(data)
print(f"Mean: {mean_value:.4f}, Standard Deviation: {std_dev:.4f}")

# Example 6: Special Functions
bessel_value = jv(2, 3)
print(f"Bessel function J2(3): {bessel_value:.4f}")

# Plotting
plt.plot(x_data, y_data, 'o', label='Data points')
plt.plot(x_interp, y_interp, label='Interpolated curve')
plt.xlabel('x')
plt.ylabel('y')
plt.title('SciPy Examples')
plt.legend()
plt.grid(True)
plt.show()