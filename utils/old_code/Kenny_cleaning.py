import pandas as pd

# Load raw data
df = pd.read_csv('Data/Raw_data.csv')

# Remove duplicates excluding 'zimmo code'
original_dupl = len(df)
df = df.drop_duplicates(subset=df.columns.difference(['zimmo code'])) # Excluded zimmo code from duplicates as a double check
duplicates_removed = original_dupl - len(df)

# Count and remove whitespace
modified_count = 0

# Loop over each column in the DataFrame
for column in df.columns:
    # Check if the column contains strings
    if df[column].dtype == "object":
        # Convert all values in the column to strings
        original = df[column].astype(str)
        # Remove whitespace from each value
        cleaned = original.str.strip()
        # Count how many values were changed
        modified_count += (original != cleaned).sum()
        # Replace original column with cleaned version
        df[column] = cleaned

# Save cleaned data
df.to_csv('Data/Cleaned_data.csv', index=False)

# Print the cleanup summary 
print(f"Duplicates removed: {duplicates_removed}")
print(f"String values modified by whitespace stripping: {modified_count}")
