import pandas as pd
import numpy as np

df = pd.read_csv("Data/Raw_data.csv")  


# Clean column names: remove whitespace, put lower case and replace space by underscore
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Drop unused columns
df.drop(columns=['unnamed:_0', 'url', 'id', 'monthlycost', 'hasbalcony', 'accessibledisabledpeople',
                 'bathroomcount','roomcount','hasattic','hasbasement','hasdressingroom',
                'diningroomsurface','hasdiningroom','floorcount','streetfacadewidgth',
                'floodzonetype','heatingtype','hasheatpump','hasvoltaicpanels',
                'hasthermicpanels','kitchensurface','kitchentype','haslivingroom',
                'livingroomsurface','gardenorientation','hasairconditioning',
                'hasarmoreddoor','hasvisiophone','hasoffice','hastoiletcount',
                'hasfireplace','terracesurface','terraceorientation',
                'gardensurface','parkingcountindoor','parkingcountoutdoor', 'toiletcount',
                'hasphotovoltaicpanels', 'streetfacadewidth','buildingconstructionyear',
                'facedecount', 'landsurface'], inplace=True, errors='ignore') 

# Drop unused rows
df.dropna(subset=["price",'bedroomcount','habitablesurface', 'buildingcondition', 'epcscore'], inplace=True) #3998 found and empty columns others


# Replace empty booleans with False
df.fillna({'hasgarden':'False', 'hasswimmingpool': 'False', 'hasterrace': 'False',
           'haslift':'False'}, inplace=True)

# Remove duplicates excluding 'zimmo code'
original_dupl = len(df)
df = df.drop_duplicates()
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

# Categories to convert to BOOLEAN
bool_cols = ['haslift', 'hasgarden', 'hasswimmingpool', 'hasterrace']
for col in bool_cols:
    df[col] = df[col].str.lower().map({'true': True, 'false': False}).astype('boolean')

# Categories to convert to INT
int_cols = ['bedroomcount', 'habitablesurface', 'price'] 
for col in int_cols:
    df[col] = df[col].astype(int)

# Categories to convert to STR
cat_cols = ['type', 'subtype', 'province', 'locality', 'buildingcondition','epcscore']
for col in cat_cols:
    df[col] = df[col].astype('string').str.strip().str.lower().str.replace("_", " ")

df.info()

# Save cleaned data
df.to_csv('Data/Cleaned_data.csv', index=False)
print(f"String values modified by whitespace stripping: {modified_count}")
