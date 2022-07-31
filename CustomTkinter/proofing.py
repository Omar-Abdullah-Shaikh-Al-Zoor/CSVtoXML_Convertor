import csv

import pandas as pd
import re



def num_csv(csv_path,field):
    csvFile = csv_path
    df = pd.read_csv(csvFile)
    field_ = str(df[field])
    if not field_.isdigit():
            return field + " field does not contain numbers only"
    return field + " field contains numbers only"



def str_csv(csv_path,field):
    csvFile = csv_path
    df = pd.read_csv(csvFile)
    field_ = df[field]

    for x in (field_):
        if x is str:
            pass
        else:
            return field + " does not contain string values only"
    return field + " contains string values only"

path_file="D:/Python_Projects/WorkProjects/my_file.csv"
result = num_csv("D:/Python_Projects/WorkProjects/my_file.csv","number")
print(result)