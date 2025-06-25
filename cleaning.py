import pandas as pd
import numpy as np

df = pd.read_csv("Data/Raw_data.csv")  

# Clean column names: remove whitespace, lower case, replace space by underscore
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

# Drop rows with missing critical values
df.dropna(subset=["price",'bedroomcount','habitablesurface', 'buildingcondition', 'epcscore'], inplace=True)

# Replace empty booleans with False
df.fillna({'hasgarden':'False', 'hasswimmingpool': 'False', 'hasterrace': 'False',
           'haslift':'False'}, inplace=True)

# Remove duplicates
original_dupl = len(df)
df = df.drop_duplicates()
duplicates_removed = original_dupl - len(df)

# Strip whitespace from string columns and count modifications
modified_count = 0
for column in df.columns:
    if df[column].dtype == "object":
        original = df[column].astype(str)
        cleaned = original.str.strip()
        modified_count += (original != cleaned).sum()
        df[column] = cleaned

print(f"Duplicates removed: {duplicates_removed}")
print(f"String values modified by whitespace stripping: {modified_count}")

# Convert boolean-like columns from string to boolean, then to int
bool_cols = ['haslift', 'hasgarden', 'hasswimmingpool', 'hasterrace']
for col in bool_cols:
    df[col] = df[col].str.lower().map({'true': True, 'false': False}).astype('boolean')
df[bool_cols] = df[bool_cols].astype(int)

# Convert certain columns to int
int_cols = ['bedroomcount', 'habitablesurface', 'price'] 
for col in int_cols:
    df[col] = df[col].astype(int)

# Convert categories to string and normalize text
cat_cols = ['type', 'subtype', 'province', 'locality', 'buildingcondition','epcscore']
for col in cat_cols:
    df[col] = df[col].astype('string').str.strip().str.lower().str.replace("_", " ")

# Calculate price per square meter
df['price_per_m2'] = round(df['price'] / df['habitablesurface'], 2)

# Drop extreme values based on type, subtype, habitablesurface, and price_per_m2
df = df[
    ((df['type'] == 'apartment') & (df['habitablesurface'] < 5000)) |
    ((df['type'] == 'house') & (df['habitablesurface'] < 10100))
]

df = df[
    ((df['subtype'] == 'house') & (df['price_per_m2'] < 20000)) |
    (df['subtype'] != 'house')
]

df = df[
    ((df['subtype'] == 'villa') & (df['price_per_m2'] < 20000)) |
    (df['subtype'] != 'villa')
]

df.info()

# Save cleaned and filtered data
df.to_csv('Data/Cleaned_data.csv', index=False)
print("Data cleaning and filtering complete.")
print(df['buildingcondition'].unique())
print(df['buildingcondition'].value_counts())