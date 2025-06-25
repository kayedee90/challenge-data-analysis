import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.io as pio
# Set plotly to render in browser
pio.renderers.default = "browser"

# Load the cleaned data
df = pd.read_csv("Data/Cleaned_data.csv")  

"""Visualisation of number of columns and rows"""

# Get dimensions
num_rows, num_columns = df.shape
shape = pd.DataFrame({'Dimension': ['Rows', 'Columns'],
                      'Count': [num_rows, num_columns]})

# Plot
plt.figure()
plt.bar(['Rows', 'Columns'], [num_rows, num_columns],
        color=['skyblue', 'orange'], edgecolor='black', log=True) # Use log scale for extreme outliers

for i, count in enumerate([num_rows, num_columns]):
    plt.text(i, count, f'{count:,}', ha='center', va='bottom', fontsize=10)

plt.title('Dataset Shape')
plt.ylabel('Count')
plt.show()


""" Visualisation of number properties according to surface"""
plt.figure(figsize=(10,6))
sns.histplot(df["habitablesurface"], bins=30, color='skyblue', edgecolor='black')

plt.title("Distribution of Property Surface Area")
plt.xlabel("Surface Area by m²")
plt.ylabel("Number of Properties")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

""" Static visualisation of number properties according to surface, 99th percentiel"""
# Set filter for outliers to 99th percentiel
plt.figure(figsize=(10,6))
p99 = df["habitablesurface"].quantile(0.99) #here you can adjust the filter
df_filtered = df[df["habitablesurface"] <= p99]

sns.histplot(df_filtered["habitablesurface"], bins=30, color='skyblue', edgecolor='black') 

plt.title("Distribution of Property Surface Area (<= 99th percentile)")
plt.xlabel("Surface Area by m²")
plt.ylabel("Number of Properties")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

""" Interactive visualisation of number properties according to surface, 99th percentiel, using plotly, in browser"""
fig = px.histogram(df_filtered, x="habitablesurface", color="subtype",
                   nbins=30, title="Distribution of Property Surface Area by Subtype (<= 99e percentile) - Interactive",
                   labels={"habitablesurface": "Surface Area (m²)"},
                   barmode='overlay', opacity=0.6)

fig.update_layout(xaxis_title="Surface Area (m²)", yaxis_title="Count")
fig.show()

"""Top 5 variables that influence price"""

# Map building condition categories to numerical values
condition_mapping = {
    'as new': 3,
    'just renovated': 2,
    'good': 1,
    'to be done up': 0,
    'to renovate': 0,
    'to restore': 0
}
df['building_condition'] = df['buildingcondition'].map(condition_mapping)

# Drop the original buildingcondition column
df = df.drop(columns=['buildingcondition'])

# Create a variable for all categories to drop from the heatmap
categories_to_drop = ['postcode', 'locality', 'province', 'subtype', 'type', 'region']

# Redefine the dataframe by dropping the non numerical categories
df = df.drop(columns=[column for column in categories_to_drop if column in df.columns])

# Create a variable for all numerical columns
numerical_cols = df.select_dtypes(include=['number']).columns

# Calculate and store correlation of all remaining features with price
correlations = df[numerical_cols].corr()['price'].abs().sort_values(ascending=False)

# Extract top 5 features most correlated with price
top5 = correlations.drop('price').head(5)
# Print all values
print("All variables correlated with price:")
for variable, correlation_value in correlations.drop('price').items():
    print(f"- {variable}: {correlation_value:.2f}")

# Plot full heatmap
plt.figure(figsize=(14, 12))
sns.heatmap(df[numerical_cols].corr(), annot=True, fmt=".2f", cmap='coolwarm')
plt.title("Correlation matrix of numerical variables")
plt.show()

# Print top 5 variables
print("Top 5 variables most correlated with price:")
for variable, correlation_value in top5.items():
    print(f"- {variable}: {correlation_value:.2f}")

# Create a list of the top 5 features
top5_vars = top5.index.tolist()
# Plot heatmap of top 5 variables + price
plt.figure(figsize=(8, 6))
sns.heatmap(df[top5_vars + ['price']].corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Top 5 variables that influence price")
plt.show()
