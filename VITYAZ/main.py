import a as a
import numpy as np
from pandas import read_csv

from VITYAZ.remont.remont import read_remont
from VITYAZ.service.desired_viev import *
from VITYAZ.service.range_date import *
from VITYAZ.steps.step_1 import *
from VITYAZ.steps.step_2 import *

# Читаем и делаем df
df_csv = read_csv("test.csv")
df = pd.DataFrame(df_csv)

############################################ Приводим в надлежащий вид
# Удаляем архивные по условию
df.drop(df[df['status'] == '-'].index, inplace = True)

# Парсим столбец
pars_col(df, 'vendor', 0)
pars_col(df, 'name_tram', -3)
pars_col(df, 'N_sostava', -2)
pars_col(df, 'N_camera', -1)

# Переделываем в datetime и избавляемся от миллисекунд в last_time_check_on_camera
str_to_data(df, 'last_time_check_on_camera')

# удаляем не нужные столбцы
# del_col(df, 'camera')
# del_col(df, 'status')

# упорядочеваем столбцы
df = df[['vendor', 'name_tram', 'N_sostava', 'N_camera', 'last_time_check_on_camera', 'last_lat_on_camera', 'last_lon_on_camera']]

# меняем на str на int
str_to_int(df, "N_sostava")
str_to_int(df, "N_camera")

# меняем на float на int
float_to_int(df, "last_lat_on_camera")
float_to_int(df, "last_lon_on_camera")

# сортировка массива по одному столбцу
sort(df, 'last_time_check_on_camera')
# Удаление 1го попавшегося дубликата
df = df.drop_duplicates(subset=['N_camera', "N_sostava"], keep='last')

# Двойная сортировка массива по N_sostava затем N_camera
df = df.sort_values(by=['N_sostava', 'N_camera'])

# Делаем флаг для cоставов с количесвом камер для каждого состава
df['сount_cam'] = df.groupby('N_sostava')['N_sostava'].transform('size')

# Считывает и хранит ремонтные составы
remont = read_remont()

df_сount_cam = all_count_cam(df) # Делает df с общим количесвом составов без дублирования
############################################

############################################ Работа с датой
# Вызываем функцию из модуля и выбираем дату
# inputDate = (data_check())
# Конверируем строку в дату и снова в строку
# inputDate = str(datetime.strptime(str(inputDate), '%Y-%m-%d').date())
# Текущая дата
today = date.today()
# inputDate = datetime.strptime(str('2022-12-19'), '%Y-%m-%d').date()
inputDate = '2022-12-19'
#inputDate = datetime.datetime.strptime(inputDate, '%Y-%m-%d') # На всякий случай если не будет робить
############################################

############################################ Вывод данных
print('‼️Свежая статистика по трамваям Витязь ', '\n')

step_1 = total_in_the_sphere(df_сount_cam) # вывод сколько всего в сфере трамваев - step_1
print(step_1)

step_2 = count_rem(remont) # вывод сколько всего ремонтных - step_2
print(step_2)










# Ищем полностью не доступные камеры
# Not_available = (df['last_time_check_on_camera'].isnull()) | (df['last_time_check_on_camera'] < inputDate)
# Not_available = df.loc[Not_available]


# Новый df с составами у который проблемы с геоданными
# geo_problem = df.query('(last_lat_on_camera==0 or last_lat_on_camera==90 or last_lat_on_camera==-90) or (last_lon_on_camera==0 or last_lon_on_camera==90 or last_lon_on_camera==-90)')
# # удаляем дубликаты и не нужные столбцы
# geo_problem = geo_problem.drop_duplicates(subset=["N_sostava"], keep='last')
# del_col(geo_problem, 'N_camera')
# del_col(geo_problem, 'last_time_check_on_camera')

# #### Определение диапазона дат
# # Вызываем функцию из модуля и выбираем дату
# inputDate = (data_check())
# # Конверируем строку в дату
# inputDate = datetime.strptime(str(inputDate), '%Y-%m-%d').date()
# # Текущая дата
# today = date.today()




##################

all_good = df[(df.N_sostava.isin(remont)) == False] # Проверяем вхождение ремонтных составов и удаляем их

all_good = pd.DataFrame(all_good) # Убираем строкти со значением Null во всём df, включая широту и долготу
all_good = all_good.dropna()

all_good = all_good.loc[all_good['last_time_check_on_camera'] >= inputDate] # Отсеиваем по времени

# Отсеиваем по флагам




# 'last_lat_on_camera', 'last_lon_on_camera'
# 1 Берём все составы
# 2 Убираем ремонтные | Убираем Нулл | отсеиваем по времени
# 3 Проверяем по флагам на доступность всех камер





#all_good = all_good['last_time_check_on_camera'].notnull() # Удаляем те, где NaT
#all_good = df.loc[all_good]

with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
      print(all_good)

print(all_good.nunique())


# Показывает тип данных
all_good = all_good.dtypes['last_lon_on_camera']