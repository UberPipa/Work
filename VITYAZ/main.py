import pandas as pd
from pandas import read_csv

df_csv = read_csv("test.csv")
df = pd.DataFrame(df_csv)



print(df.head())

# with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
#     print(df)
