import numpy as np
import pandas as pd

df = pd.read_csv("./Data/immoweb-dataset.csv")
df.info()


""" def split_type_column(df):

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

    
    
if __name__ == "__main__":

    df = pd.read_csv("./Data/Raw_data_Copy.csv")
    print("Original type: \n", df["type"])
    
    split_type_column(df)
    
    print("After splitting type:\n", df["type"]) 
    print("After splitting subtype:\n", df["subtype"])  

    df.to_csv('./Data/testOut.csv', index=False)

    

 """