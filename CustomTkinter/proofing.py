import csv

import pandas as pd
import re



def num_csv(csv_path,field):
    with open(csv_path, newline='') as f:
        ereader = csv.DictReader(f)
        for row in ereader:
            if not row[field].isdigit():
                return field + " does not contain numbers only"
    return field + " field contains numbers only"



def str_csv(csv_path,field):
    with open(csv_path, newline='') as f:
        ereader = csv.DictReader(f)
        for row in ereader:
            if not row[field].isalpha():
                return field + " does not contain Letters only"
    return field + " field contains Letters only"


path_file="D:/Python_Projects/WorkProjects/my_file.csv"
result = str_csv("D:/Python_Projects/WorkProjects/my_file.csv","Name")
print(result)