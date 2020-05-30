import pandas as pd
import os
import warnings
import sys

warnings.filterwarnings("error")
path = input("Enter the folder path:")

def mergeTables(path):
    path = path.replace("\\", "/")
    print(path)
    directory = os.listdir(path)
    if len(directory) == 0:
        sys.exit("Empty directory \nPROCESS HAS BEEN ABORTED")
    df_big = pd.DataFrame()
    for excel in directory:
        if (".xlsx" not in excel) or (".xls" not in excel):
            continue
        print(excel)
        try:
            df = pd.read_excel(path + "/" + excel, )
        except:
            print("Make sure that every file is excel-like type (e.g.: .xlsx)")
            print("PROCESS HAS BEEN ABORTED")
            break
        try:
            df_big = df_big.append(df, ignore_index=True)
        except:
            print("Make sure that column names and number of columns at the every file are coherent")
            print("PROCESS HAS BEEN ABORTED")
            break
    df_big.to_csv(path + "/_ALL.csv", sep=";")
    print("SUCCESS")
    return df_big

mergeTables(path=path)