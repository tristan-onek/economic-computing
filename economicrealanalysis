import numpy as np
import matplotlib.pyplot as plt

# Define a Cobb-Douglas utility function
# U(x, y) = x^alpha * y^(1-alpha), where 0 < alpha < 1

def utility_function(x, y, alpha=0.5):
    return x**alpha * y**(1 - alpha)

# Set parameters for the utility function
alpha = 0.6
x = np.linspace(0.1, 10, 100)  # Avoid zero to prevent undefined behavior
y = np.linspace(0.1, 10, 100)

# Create a meshgrid for 3D plotting
X, Y = np.meshgrid(x, y)
U = utility_function(X, Y, alpha)

# Plot the utility function in 3D
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, U, cmap='viridis', edgecolor='none')
ax.set_title('Cobb-Douglas Utility Function')
ax.set_xlabel('Good X')
ax.set_ylabel('Good Y')
ax.set_zlabel('Utility')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

# Check convexity: A utility function is convex if the indifference curves are convex
# Let's plot indifference curves
levels = [1, 5, 10, 15, 20]

plt.figure(figsize=(10, 6))
for level in levels:
    plt.contour(X, Y, U, levels=[level], cmap='viridis')

plt.title('Indifference Curves of the Utility Function')
plt.xlabel('Good X')
plt.ylabel('Good Y')
plt.grid(True)
plt.show()

# Check continuity: The utility function should be continuous over the domain
# We'll evaluate the function at different points to verify no abrupt changes
sample_x = [1, 2, 3, 4, 5]
sample_y = [1, 2, 3, 4, 5]

for x_val, y_val in zip(sample_x, sample_y):
    utility = utility_function(x_val, y_val, alpha)
    print(f"Utility at (x={x_val}, y={y_val}): {utility:.2f}")

# Marginal utilities
# MUx = dU/dx = alpha * x^(alpha-1) * y^(1-alpha)
# MUy = dU/dy = (1-alpha) * x^alpha * y^(-alpha)

def marginal_utility_x(x, y, alpha):
    return alpha * x**(alpha - 1) * y**(1 - alpha)

def marginal_utility_y(x, y, alpha):
    return (1 - alpha) * x**alpha * y**(-alpha)

# Example: Compute marginal utilities at specific points
x_val, y_val = 3, 4
MUx = marginal_utility_x(x_val, y_val, alpha)
MUy = marginal_utility_y(x_val, y_val, alpha)
print(f"Marginal Utility w.r.t X at (x={x_val}, y={y_val}): {MUx:.2f}")
print(f"Marginal Utility w.r.t Y at (x={x_val}, y={y_val}): {MUy:.2f}")
