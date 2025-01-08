import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Simulate data
n = 100
x = np.linspace(1, 10, n)  # Independent variable

# Create exogenous errors (independent of x)
errors = np.random.normal(0, 2, n)  # Constant standard deviation

# Generate dependent variable
y = 5 + 2 * x + errors

# Create a DataFrame for clarity
data = pd.DataFrame({"x": x, "y": y})

# Fit an OLS regression model
X = sm.add_constant(data["x"])  # Add intercept
model = sm.OLS(data["y"], X).fit()

# Print summary
print(model.summary())

# Plot residuals vs independent variable to visualize exogeneity
plt.figure(figsize=(10, 6))
plt.scatter(data["x"], model.resid, alpha=0.7, edgecolors="k")
plt.axhline(0, color="red", linestyle="--", linewidth=1)
plt.title("Residuals vs Independent Variable (x)")
plt.xlabel("Independent Variable (x)")
plt.ylabel("Residuals")
plt.show()

# Perform a test for exogeneity using Durbin-Wu-Hausman (simplified example)
from statsmodels.stats.diagnostic import het_white

# White's test for independence of residuals and explanatory variables
white_test = het_white(model.resid, X)

# Print White test results
labels = ["Test Statistic", "p-value", "F-Statistic", "F p-value"]
print(dict(zip(labels, white_test)))
