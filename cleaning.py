import pandas as pd
import numpy as np

df = pd.read_csv("Data/Raw_data.csv")  


# Clean column names
# from columns delete spaces begin and end, put lower case and replace space by underscore
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

# Drop unused rows# 
df.dropna(subset=["price",'bedroomcount','habitablesurface', 'buildingcondition', 'epcscore'], inplace=True) #3998 found and empty columns others


# Replace empty booleans with False
df.fillna({'hasgarden':'False', 'hasswimmingpool': 'False', 'hasterrace': 'False',
           'haslift':'False'}, inplace=True)

df.info()
print(df.isna().sum()* 100 /len(df))


# dropping cleaned dataframe to a cleaned data file
df.to_csv('Data/Cleaned_data.csv', index=False)

# reading info from the cleaned data
#df2 = pd.read_csv("Data/Cleaned_data.csv")

# removing Unnamed column cleaned data
#df2 = df2.drop('Unnamed: 0', axis=1)
#df2.info()
