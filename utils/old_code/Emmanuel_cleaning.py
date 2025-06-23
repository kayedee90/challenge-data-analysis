import pandas as pd
import numpy as np
#from pandas.api.types import is_string_dtype, is_numeric_dtype

df = pd.read_csv("Data/Raw_data.csv")

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
df.to_csv('Data/cleaned_data.csv')

# reading info from the cleaned data
df2 = pd.read_csv("Data/cleaned_data.csv")

# removing Unnamed column cleaned data
df2 = df2.drop('Unnamed: 0', axis=1)
df2.info()