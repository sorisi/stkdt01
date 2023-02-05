import pandas as pd
import glob
import os
import numpy as np


location = 'sori-nov.xlsx'
excel_files = glob.glob(location)


print(pd.options.display.max_rows) 
print(pd.options.display.max_columns)



df1 = pd.DataFrame()

for excel_file in excel_files:
    sheet = excel_file
    #df2 = pd.read_excel(excel_file)
    df1 = pd.concat([df1], ignore_index=True)

print(df1)

# create mon - fri application





