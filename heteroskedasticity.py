import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Simulate data
n = 100
x = np.linspace(1, 10, n)  # Independent variable

# Create heteroskedastic errors (variance increases with x)
errors = np.random.normal(0, x)  # Standard deviation grows with x

# Generate dependent variable
y = 5 + 2 * x + errors

# Create a DataFrame for clarity
data = pd.DataFrame({"x": x, "y": y})

# Fit an OLS regression model
X = sm.add_constant(data["x"])  # Add intercept
model = sm.OLS(data["y"], X).fit()

# Print summary
print(model.summary())

# Plot residuals vs fitted values to visualize heteroskedasticity
fitted_values = model.fittedvalues  # Predicted values
residuals = model.resid  # Residuals

plt.figure(figsize=(10, 6))
plt.scatter(fitted_values, residuals, alpha=0.7, edgecolors="k")
plt.axhline(0, color="red", linestyle="--", linewidth=1)
plt.title("Residuals vs Fitted Values")
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.show()

# Perform a Breusch-Pagan test for heteroskedasticity
from statsmodels.stats.diagnostic import het_breuschpagan

bp_test = het_breuschpagan(residuals, X)

# Print Breusch-Pagan test results
labels = ["LM Statistic", "p-value", "F-Statistic", "F p-value"]
print(dict(zip(labels, bp_test)))
