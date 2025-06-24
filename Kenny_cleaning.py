import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Data/Cleaned_data.csv")  

# Get dimensions
num_rows, num_columns = df.shape
shape = pd.DataFrame({'Dimension': ['Rows', 'Columns'],
                      'Count': [num_rows, num_columns]})

# Plot
ax = shape.plot(kind='bar', x='Dimension', y='Count', legend=False,
                color=['skyblue', 'orange'], edgecolor='black', logy=True)

# Add value labels
for i, count in enumerate(shape['Count']):
    ax.text(i, count, f'{count:,}', ha='center', va='bottom', fontsize=10)

plt.title('Dataset Shape (Log Scale)')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()