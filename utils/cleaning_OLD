import pandas as pd
import numpy as np



def split_type_column(df):
    def type_split(row):
        if '(' in row:
            subtype = row.split('(')[0].strip() 
            type = row.split('(')[1][:-1].strip() 
        else:
            subtype = row 
            type = row 
        return [subtype, type]
    
    df[['subtype', 'type']] = df['type'].apply(type_split).apply(pd.Series)

    df.insert(2, 'subtype', df.pop('subtype'))

df = pd.read_csv("Data/Raw_data.csv")
print("Original type: \n", df["type"])
    
split_type_column(df)
    
print("After splitting type:\n", df["type"]) 
print("After splitting subtype:\n", df["subtype"])  
df.to_csv('Data/Cleaned_data.csv', index=False)



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

# Print the cleanup summary 
print(f"Duplicates removed: {duplicates_removed}")
print(f"String values modified by whitespace stripping: {modified_count}")

# removing rows living area empty
df.rename(columns={
    "living area(mÂ²)": "living area(m²)"
}, inplace=True)
# "ground area(mÂ²)": "ground area(m²)"
df.dropna(subset=["living area(m²)", "bedroom", "bathroom", 'EPC(kWh/m²)'], inplace=True)

# removing unnecessary columns
df = df.drop('street', axis=1)
df = df.drop('number', axis=1)
df = df.drop('url', axis=1)
df = df.drop('ground area(m²)', axis=1)
df = df.drop('mobiscore', axis=1)
df = df.drop('zimmo code', axis=1)

# replace null values
    # checks null values, 
    #df.isnull().sum()

df.fillna(np.nan).replace([np.nan], [None])
df.isnull().sum()


#change float to integer price bedroom bathroom garden

df['price'] = df['price'].astype(int)
df['bedroom'] = df['bedroom'].replace('NaN', pd.NA).fillna(0).astype(int)
df['bathroom'] = df['bathroom'].replace('NaN', pd.NA).fillna(0).astype(int)
df['garage'] = df['garage'].replace('NaN', pd.NA).fillna(0).astype(int)
df['garden'] = df['garden'].replace('NaN', pd.NA).fillna(0).astype(int)
df['year built'] = df['year built'].replace('NaN', pd.NA).fillna(0).astype(int)

df.info()

# Replacing values
df['garage'] = df['garage'].fillna(0)
df['renovation obligation'] = df['renovation obligation'].fillna('False')

# dropping cleaned dataframe to a cleaned data file
df.to_csv('Data/Cleaned_data.csv', index=False)

# reading info from the cleaned data
#df2 = pd.read_csv("Data/Cleaned_data.csv")

# removing Unnamed column cleaned data
#df2 = df2.drop('Unnamed: 0', axis=1)
#df2.info()
