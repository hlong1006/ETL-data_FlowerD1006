import pandas as pd 
import numpy as np 
import os 
import re 
from extract import extract_all_data

def clean_numeric_column(column_series , unit_remove ):
    # -> string 
    cleaned_series = column_series.astype(str)
     
    # remove numric 
    if unit_remove :
        cleaned_series = cleaned_series.str.replace(re.escape(unit_remove),'', regex = True )
    cleaned_series = cleaned_series.str.replace('€', '', regex=False)
    cleaned_series = cleaned_series.str.replace('£', '', regex=False)
    cleaned_series = cleaned_series.str.replace(',', '', regex=False)  

    cleaned_series = cleaned_series.replace(['-','nan',''], np.nan)

    return pd.to_numeric(cleaned_series ,errors =  'coerce')  

df_ev2023, df_ev2024, df_ele = extract_all_data()
dataframes_to_clean = [df_ev2023, df_ev2024]

for df in dataframes_to_clean:
    df['Acceleration'] = clean_numeric_column(df['Acceleration'], 'sec')
    df['TopSpeed'] = clean_numeric_column(df['TopSpeed'], 'km/h')
    df['Range'] = clean_numeric_column(df['Range'], 'km')
    df['Efficiency'] = clean_numeric_column(df['Efficiency'], 'Wh/km')
    df['FastChargeSpeed'] = clean_numeric_column(df['FastChargeSpeed'], 'km/h')

    df['PriceinGermany'] = clean_numeric_column(df['PriceinGermany'], '')
    df['PriceinUK'] = clean_numeric_column(df['PriceinUK'], '')

df_combined = pd.concat([df_ev2023, df_ev2024], ignore_index=True)    

df_combined = df_combined.drop_duplicates(subset=['Name'], keep='first')

