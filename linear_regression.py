import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Given dataset
data = np.array([
    [2400, 41200],
    [2650, 50100],
    [2350, 52000],
    [4950, 66000],
    [3100, 44500],
    [2500, 37700],
    [5106, 73500],
    [3100, 37500],
    [2900, 56700],
    [1750, 35600]
])

# Separate spending and income
spending = data[:, 0].reshape(-1, 1)
income = data[:, 1]

# Create and fit the linear regression model
regression_model = LinearRegression()
regression_model.fit(spending, income)

# Predict income for new spending values
new_spending = np.array([[3500], [5300]])
predicted_income = regression_model.predict(new_spending)

# Print predicted income for new spending values
for i in range(len(new_spending)):
    print(f"Predicted income for spending {new_spending[i][0]}: ${predicted_income[i]:,.2f}")

# Plotting the dataset and regression line
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.scatterplot(x=spending.flatten(), y=income)
sns.scatterplot(x= new_spending.flatten(),y = predicted_income)
sns.lineplot(x=spending.flatten(), y=regression_model.predict(spending), color='red')
plt.title('Scatter Plot of Spending vs Income with Regression Line')
plt.xlabel('Spending')
plt.ylabel('Income')
plt.show()
