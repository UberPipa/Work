import pandas as pd
from pandas import read_csv

df_csv = read_csv("test.csv")
df = pd.DataFrame(df_csv)

# удаляем столбец ip
df.pop('ip')

### разбиваем столбец 'camera'
# Добавили вендора, имя трамвая, № состава, № камеры.
df['vendor'] = df.camera.str.split('_').str[0]
df['name_tram'] = df.camera.str.split('_').str[-3]
df['N_sostava'] = df.camera.str.split('_').str[-2]
df['N_camera'] = df.camera.str.split('_').str[-1]

# Избавляемся от миллисекунд в time_check
df['time_check'] = pd.to_datetime(df['time_check'])
df['time_check'] = df['time_check'].dt.ceil('T')

# удаляем не нужные столбцы
df = df.drop(['camera'], axis=1)

# упорядочеваем столбцы
df = df[['vendor', 'name_tram', 'N_sostava', 'N_camera', 'time_check', 'latitude', 'longitude']]

# меняем на int
df["N_sostava"] = pd.to_numeric(df["N_sostava"])
df["N_camera"] = pd.to_numeric(df["N_camera"])
df["latitude"] = pd.to_numeric(df["latitude"])
df["longitude"] = pd.to_numeric(df["longitude"])

# сортировка массива по time_check
df = df.sort_values(by='time_check')

# Удаление 1го попавшегося дубликата
df = df.drop_duplicates(subset=['N_camera', "N_sostava"], keep='last')

# сортировка массива по N_sostava и N_camera
df = df.sort_values(by=['N_sostava', 'N_camera'])

# Считывание ремонтных составов и запись в список remont
remont = []
with open('remont.txt') as file:
     for i in file:
          remont.append(int(i.strip()))

# Проверяем вхождение ремонтных составов и удоляем их
df = df[(df.N_sostava.isin(remont)) == False]

# Нужно определить что выбивается за рамки недели относительно сегодняшнего дня и получить сколько:
#                   1) Всего заведено;
#                   2) Всего в ремонте;
#                   3) Не доступны частично или полность(Включая геоданные)
#                   4) Сколько полностью доступны.




# вывод
# with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
#      print(df)
