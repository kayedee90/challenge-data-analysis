import pandas as pd

# Load the CSV file
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
           'haslift':'False', 'hasgarden':'False', 'hasswimmingpool': 'False'}, inplace=True)

print(df.isna().sum()* 100 /len(df))

"""
# fill missing boolean values
df.fillna({'hasattic': 'False', 'hasbasement': 'False', 'hasdressingroom': 'False',
           'hasdiningroom': 'False', 'haslift': 'False', 'hasheatpump': 'False',
           'hasphotovoltaicpanels': 'False', 'hasthermicpanels': 'False',
           'haslivingroom': 'False', 'hasgarden': 'False', 'hasairconditioning':'False',
           'hasarmoreddoor':'False', 'hasvisiophone':'False', 'hasoffice':'False',
           'hasswimmingpool': 'False', 'hasfireplace': 'False', 'hasterrace': 'False'})

# Convert data types boolean
bool_cols = [
    'hasattic', 'hasbasement', 'hasdressingroom', 'hasdiningroom',
    'haslift', 'hasheatpump', 'hasphotovoltaicpanels', 'hasthermicpanels',
    'haslivingroom', 'hasgarden', 'hasairconditioning',
    'hasarmoreddoor', 'hasvisiophone', 'hasoffice', 'hasswimmingpool',
    'hasfireplace', 'hasterrace'
]

for col in bool_cols:
    df[col] = df[col].map({'True': True, 'False': False}).astype('boolean')


# fill missing numeric values

df.fillna({
    'bedroomcount': 1,'bathroomcount': 1,'roomcount': 1,
    'buildingconstructionyear': df['buildingconstructionyear'].mode()[0],
    'facedecount': df['facedecount'].mode()[0],'floorcount': df['floorcount'].mode()[0],
    'parkingcountindoor': 0,'parkingcountoutdoor': 0,'toiletcount': df['toiletcount'].mode()[0],
    
}, inplace=True)

#'habitablesurface':df['habitablesurface'].median(), 'diningroomsurface':df['diningroomsurface'].median(),
#'streetfacadewidth', 'kitchensurface', 'landsurface', 'livingroomsurface', 'gardensurface', 'terracesurface'

# Convert numeric float columns
float_cols = [
    'habitablesurface', 'diningroomsurface',  'streetfacadewidth', 'kitchensurface', 
    'landsurface', 'livingroomsurface', 'gardensurface', 'terracesurface'
]

for col in float_cols:
    df[col] = pd.to_numeric(df[col])

# Convert numeric int columns

int_cols = ['bedroomcount', 'bathroomcount', 'postcode', 'roomcount', 'buildingconstructionyear', 'facedecount', 
'floorcount', 'parkingcountindoor', 'parkingcountoutdoor', 'toiletcount', 'price'] 

for col in int_cols:
    df[col] = df[col].astype(int)

# Categories to string
cat_cols = ['type', 'subtype', 'province', 'locality', 'buildingcondition', 'floodzonetype', 'heatingtype', 'kitchentype', 'gardenorientation', 'terraceorientation', 'epcscore']
for col in cat_cols:
    df[col] = df[col].astype('string').str.strip().str.lower().str.replace("_", " ")

# Add price per m²
df['price_per_m2'] = df['price'] / df['habitablesurface']

"""
# Remove unrealistic values
#df = df[df['price'] < 3_000_000]
#df = df[df['habitablesurface'] < 1000]
"""

df.info()
print(df.columns[df.isna().sum()>0])

"""
# Save the cleaned data
#df.to_csv("/Data/immoweb-dataset/cleaned_real_estate.csv", index=False)

#print("Dataset cleaned and saved as cleaned_immo_dataset.csv")
"""
"""
