import pandas as pd 
import os 

filecsv1 = 'data/Cheapestelectriccars_EVDatabase2023.csv'
filecsv2 = 'data/Cheapestelectriccars_EVDatabase.csv'
filecsv3 = 'data/electric_vehicles_spec_2025.csv'
def extract_all_data():
    try :
        df_ev2023 = pd.read_csv(filecsv1)
        df_ev2024 = pd.read_csv(filecsv2)
        df_ele = pd.read_csv(filecsv3)

        return df_ev2023, df_ev2024, df_ele
    except : 
        print(f"File Not Found") 
        return None , None , None
    
if __name__ == "__main__":
    print("Chạy extract.py trực tiếp để kiểm tra...")
    df_ev2023, df_ev2024, df_ele = extract_all_data()
    df = [df_ev2023 , df_ev2024 , df_ele]
    for df in df :
        if df is not None:
            print("Kiểm tra df1 thành công, 5 dòng đầu:")
            print(df.head())       


