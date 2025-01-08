import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Simulate data for an economic regression analysis
n = 100
income = np.linspace(30, 100, n)  # Independent variable: income in thousands
education = np.random.normal(12, 2, n)  # Additional independent variable: years of education
errors = np.random.normal(0, 5, n)  # Error term with constant variance

# Generate dependent variable: consumption in thousands
consumption = 10 + 0.8 * income + 0.5 * education + errors

# Create a DataFrame for clarity
data = pd.DataFrame({"income": income, "education": education, "consumption": consumption})

# Fit a multiple regression model
X = sm.add_constant(data[["income", "education"]])  # Add intercept and independent variables
model = sm.OLS(data["consumption"], X).fit()

# Print summary of the regression analysis
print(model.summary())

# Plot actual vs. predicted consumption
fitted_values = model.fittedvalues  # Predicted values

plt.figure(figsize=(10, 6))
plt.scatter(data["consumption"], fitted_values, alpha=0.7, edgecolors="k")
plt.plot([data["consumption"].min(), data["consumption"].max()],
         [data["consumption"].min(), data["consumption"].max()],
         color="red", linestyle="--", linewidth=1, label="Perfect Prediction")
plt.title("Actual vs. Predicted Consumption")
plt.xlabel("Actual Consumption")
plt.ylabel("Predicted Consumption")
plt.legend()
plt.show()

# Diagnostic plot: residuals vs. fitted values
residuals = model.resid

plt.figure(figsize=(10, 6))
plt.scatter(fitted_values, residuals, alpha=0.7, edgecolors="k")
plt.axhline(0, color="red", linestyle="--", linewidth=1)
plt.title("Residuals vs Fitted Values")
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.show()

# Perform statistical tests for model adequacy
from statsmodels.stats.diagnostic import het_breuschpagan

bp_test = het_breuschpagan(residuals, X)
labels = ["LM Statistic", "p-value", "F-Statistic", "F p-value"]
print("Breusch-Pagan Test for Heteroskedasticity:")
print(dict(zip(labels, bp_test)))
