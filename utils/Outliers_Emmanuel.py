import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
df = pd.read_csv("Data/Cleaned_data.csv")  

# Categories to convert to STR
cat_cols = ['type', 'subtype', 'province', 'locality', 'buildingcondition','epcscore']
for col in cat_cols:
    df[col] = df[col].astype('string').str.strip().str.lower().str.replace("_", " ")

#df.info()

#print(df['subtype'].value_counts())
"""
#def show_boxplots():
num_cols_cleaned =['bedroomcount','habitablesurface','price', 'price_per_m2']
list_type =['apartment', 'house']
for lt in list_type:
    for bx in num_cols_cleaned:
        fig, ax = plt.subplots(figsize=(70, 3))
        df1 = df[(df['type'].isin([lt]))]
        #df1 = df.groupby('type')['apartment'].apply(list).reset_index(name='new')
        sns.boxplot(data=df1, x='subtype', y=bx, width=0.8, palette="PRGn", ax=ax).set_title(f'Outliers per {lt}')
        ax.tick_params(axis='x', rotation=45)
        plt.show()
"""


num_cols_cleaned =['bedroomcount','habitablesurface','price', 'price_per_m2']

region_values = ['Flanders', 'Wallonia', 'Brussels']

Flanders = 'antwerp|flemish brabant|east flanders|west flanders|limburg'
Wallonia = 'hainaut|liège|luxembourg|namur|walloon brabant'
Brussels = 'brussels'
for cplt in num_cols_cleaned:
    # 75th percentile
    seventy_fifth = df[cplt].quantile(0.75)
    # 25th percentile
    twenty_fifth = df[cplt].quantile(0.25)
    # Interquartile range
    surface_iqr = seventy_fifth - twenty_fifth

    # Upper threshold
    upper = seventy_fifth + (2 * surface_iqr)
    # Lower threshold
    lower = twenty_fifth - (2 * surface_iqr)

    conditions = [
    (df["province"].str.contains(Flanders)),
    (df["province"].str.contains(Wallonia)),
    (df["province"].str.contains(Brussels))]

    df["Regions"] = np.select(conditions, region_values, default="Other")

    outliers = df[(df[cplt] < lower) | (df[cplt] > upper)]
    
    #print(outliers[["type", "Regions", "habitablesurface"]].sort_values(by="habitablesurface"))
    #print(outliers.groupby(["Regions", "subtype"]).size())

    #plt.figure(figsize=(10, 6))
    fig2, ax2 = plt.subplots(figsize=(20, 6))
    sns.countplot(data=outliers, x="subtype", hue="Regions", palette="Set3")
    plt.title(f"Number of outliers on {cplt} per region and subtype")
    plt.ylabel("Number of outliers")
    plt.xlabel("Region")
    plt.legend(title="Subtype", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    ax2.tick_params(axis='x', rotation=45)
    plt.show()

    #logy=true
#[(df['subtype'].isin(['APARTMENT']))], x='subtype', y=bx)
    
#print((df['bedroomcount']>21).loc[df['subtype']])

# showing correlation between variables
#sns.heatmap(df.corr(), annot=True)
#plt.show()

#sns.countplot(data=df, x="Regions")
#plt.show()"""

"""
#def show_boxplots():
num_cols_cleaned =['bedroomcount','habitablesurface','price', 'price_per_m2']
list_type =['apartment', 'house']
for lt in list_type:
    for bx in num_cols_cleaned:
        fig, ax = plt.subplots(figsize=(10, 3))
        df1 = df[(df['type'].isin([lt]))]
        #df1 = df.groupby('type')['apartment'].apply(list).reset_index(name='new')
        sns.boxplot(data=df1, x='subtype', y=bx, width=0.8, palette="PRGn", hue='subtype', legend=False,ax=ax).set_title(f'Outliers after caps per {lt}')
        ax.tick_params(axis='x', rotation=45)
        plt.show()
"""
