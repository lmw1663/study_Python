Here's the code and analysis results in a single file, combining the best aspects of previous responses and addressing potential shortcomings:

Python
import sklearn.datasets as skdata
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # For nicer heatmap

# Download California Housing dataset (using scikit-learn)
california_housing = skdata.fetch_california_housing()

# Feature selection using SelectKBest (univariate selection)
selector = SelectKBest(chi2, k=3)
X_new = selector.fit_transform(california_housing.data, california_housing.target)
selected_feature_names = [california_housing.feature_names[i] for i in selector.get_support(indices=True)]

# Feature selection using Random Forest feature importances
rf_model = RandomForestRegressor(n_estimators=100)
scores = cross_val_score(rf_model, california_housing.data, california_housing.target, cv=5, scoring='neg_mean_squared_error')
importances = rf_model.feature_importances_
feature_importances = sorted(zip(california_housing.feature_names, importances), key=lambda x: x[1], reverse=True)

# Correlation matrix heatmap
df = pd.DataFrame(california_housing.data, columns=california_housing.feature_names)
correlation = df.corr()
plt.figure(figsize=(10, 6))
ax = sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.xlabel('Features')
plt.ylabel('Features')
plt.title('Correlation Matrix Heatmap')
plt.show()

# Analysis summary

print("**Feature Selection Results**")

print("\nUnivariate Selection (SelectKBest):")
print("Selected features:", selected_feature_names)

print("\nFeature Importance Scoring (Random Forest):")
print("Top 3 most important features:")
for name, importance in feature_importances[:3]:
    print(name, importance)

print("\nCorrelation Matrix Heatmap:")
print("Visualize the heatmap to identify potential multicollinearity.")