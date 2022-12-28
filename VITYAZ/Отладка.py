import pandas as pd
from pandas import read_csv

df_csv = read_csv("test.csv")
df = pd.DataFrame(df_csv)

# Добавили № состава
df['N_sostava'] = df.camera.str.split('_').str[-2]

df = df.drop_duplicates(subset=["N_sostava"], keep='last')

# Считаем уникальные составы, которые заведены
print(df.nunique())



### Находим составы, которые потерялись
all = []
with open('All_392.txt') as file:
     for i in file:
          all.append(i.strip())

# Заносим значение столбца в список
from_df = list(df['N_sostava'])

# Условие по нахожднению и печать протеряных
for i in all:
     if i not in from_df:
          print(i)


# print(from_df)
# print(all)
# print(df['N_sostava'])


