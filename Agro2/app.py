import pandas as pd
import statsmodels.api as sm

# Load the data
data = pd.read_csv('Horti.csv')

# Extract year from the first column and convert it to integer
data['Year'] = data.iloc[:, 0].str.split('-').apply(lambda x: int(x[0]))

# Define the independent variable
X = data['Year']

# Add a constant term to the independent variable
X = sm.add_constant(X)

# Fruits_Pdy
y_fruits = data['Fruits_Pdy']
model_fruits = sm.OLS(y_fruits, X).fit()
print(model_fruits.summary())

# Veg_Pdy
y_veg = data['Veg_Pdy']
model_veg = sm.OLS(y_veg, X).fit()
print(model_veg.summary())

# FAM_Pdy
y_fam = data['FAM_Pdy']
model_fam = sm.OLS(y_fam, X).fit()
print(model_fam.summary())

# Plantation_Crops_Pdy
y_plantation = data['Plantation_Crops_Pdy']
model_plantation = sm.OLS(y_plantation, X).fit()
print(model_plantation.summary())

# Spices_Pdy
y_spices = data['Spices_Pdy']
model_spices = sm.OLS(y_spices, X).fit()
print(model_spices.summary())

# Total_Pdy
y_total = data['Total_Pdy']
model_total = sm.OLS(y_total, X).fit()
print(model_total.summary())
