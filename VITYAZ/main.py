import pandas as pd
from pandas import read_csv
from range_date import *

df_csv = read_csv("test.csv")
df = pd.DataFrame(df_csv)

# удаляем столбец ip
# df.pop('ip')

### разбиваем столбец 'camera'
# Добавили вендора, имя трамвая, № состава, № камеры.
df['vendor'] = df.camera.str.split('_').str[0]
df['name_tram'] = df.camera.str.split('_').str[-3]
df['N_sostava'] = df.camera.str.split('_').str[-2]
df['N_camera'] = df.camera.str.split('_').str[-1]

# Переделываем в datetime и и збавляемся от миллисекунд в last_time_check_on_camera
df['last_time_check_on_camera'] = pd.to_datetime(df['last_time_check_on_camera'])
df['last_time_check_on_camera'] = df['last_time_check_on_camera'].dt.ceil('T')

# удаляем не нужные столбцы
df = df.drop(['camera'], axis=1)

# упорядочеваем столбцы
df = df[['vendor', 'name_tram', 'N_sostava', 'N_camera', 'last_time_check_on_camera', 'last_lat_on_camera', 'last_lon_on_camera']]

# меняем на int
df["N_sostava"] = pd.to_numeric(df["N_sostava"])
df["N_camera"] = pd.to_numeric(df["N_camera"])
df["last_lat_on_camera"] = pd.to_numeric(df["last_lat_on_camera"])
df["last_lat_on_camera"] = pd.to_numeric(df["last_lat_on_camera"])

# сортировка массива по time_check
df = df.sort_values(by='last_time_check_on_camera', na_position='first')

# Удаление 1го попавшегося дубликата
df = df.drop_duplicates(subset=['N_camera', "N_sostava"], keep='last')

# сортировка массива по N_sostava и N_camera
df = df.sort_values(by=['N_sostava', 'N_camera'])

# Считывание ремонтных составов и запись в список remont
remont = []
with open('remont.txt') as file:
     for i in file:
          remont.append(int(i.strip()))

# Проверяем вхождение ремонтных составов и удаляем их
df = df[(df.N_sostava.isin(remont)) == False]

# #### Определение диапазона дат
# # Вызываем функцию из модуля и выбираем дату
# inputDate = (data_check())
# # Конверируем строку в дату
# inputDate = datetime.strptime(str(inputDate), '%Y-%m-%d').date()
# # Текущая дата
# today = date.today()



test1 = '2022-06-06'
test2 = '2023-06-06'

if test1 > test2:
     print('больше')
else:
     print('меньше')



# вывод
with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
     print(df)


# Подсчёт уникальных вхождений
# print(df.nunique())


# Нужно определить что выбивается за рамки недели относительно сегодняшнего дня и получить сколько:
#                   1) Всего заведено;
#                   2) Всего в ремонте;
#                   3) Не доступны частично или полность(Включая геоданные)
#                   4) Сколько полностью доступны.
