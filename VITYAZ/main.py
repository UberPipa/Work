from pandas import read_csv
from VITYAZ.steps.step_1 import *
from VITYAZ.steps.step_2 import *
from VITYAZ.steps.step_3 import *

from VITYAZ.steps.range_date import *
from VITYAZ.steps.step_11 import *
from VITYAZ.steps.step_22 import *
from VITYAZ.steps.step_33 import *
from VITYAZ.steps.step_44 import *
from VITYAZ.steps.step_55 import *

# Step_1
df = create_df('df') # Читаем и делаем df
remont = read_remont() # Считывает и хранит ремонтные составы списком

# Step_2
del_arch(df) # Удаляет архивные по условию
pars_col(df, 'vendor', 0) # Парсим
pars_col(df, 'N_sostava', -2) # Парсим
pars_col(df, 'N_camera', -1) # Парсим
del_col(df, 'camera') # удаляет не нужный столбцы
del_col(df, 'status') # удаляет не нужный столбцы
del_col(df, 'РўРЎ') # удаляет не нужный столбцы
str_to_data(df, 'last_time_check_on_camera') # Переделываем в datetime и избавляемся от миллисекунд в last_time_check_on_camera
str_to_int(df, "N_sostava") # меняем на str на int
str_to_int(df, "N_camera") # меняем на str на int
float_to_int(df, "last_lat_on_camera") # меняет float на int, делает не угодные значения nan
float_to_int(df, "last_lon_on_camera") # меняет float на int, делает не угодные значения nan
df['сount_cam'] = df.groupby('N_sostava')['N_sostava'].transform('size') # Делаем флаг для cоставов с количесвом камер для каждого состава
df = df[['vendor', 'N_sostava', 'N_camera', 'сount_cam', 'last_time_check_on_camera', 'last_lat_on_camera', 'last_lon_on_camera']] # упорядочеваем столбцы
df = df.sort_values(by=['N_sostava', 'N_camera']) # Двойная сортировка массива по N_sostava затем N_camera

# Step_3
df_сount_cam = all_count_cam(df) # Делает df с общим количесвом составов без дублирования

# Step_4



# # сортировка массива по одному столбцу
# sort(df, 'last_time_check_on_camera')
# # Удаление 1го попавшегося дубликата
# df = df.drop_duplicates(subset=['N_camera', "N_sostava"], keep='last')
############################################

############################################ Работа с датой
# Вызываем функцию из модуля и выбираем дату
# inputDate = (data_check())
# Конверируем строку в дату и снова в строку
# inputDate = str(datetime.strptime(str(inputDate), '%Y-%m-%d').date())
# Текущая дата
today = date.today()
# inputDate = datetime.strptime(str('2022-12-19'), '%Y-%m-%d').date()
inputDate = '2023-01-02'
#inputDate = datetime.datetime.strptime(inputDate, '%Y-%m-%d') # На всякий случай если не будет робить
############################################

############################################ Вывод данных
# print('‼️Свежая статистика по трамваям Витязь ', '\n')
#
# step_1 = total_in_the_sphere(df_сount_cam) # вывод сколько всего в сфере трамваев - step_1
# print(step_1)
#
# step_2 = count_rem(remont) # вывод сколько всего ремонтных - step_2
# print(step_2)
#
# step_3 = all_good(df, remont, inputDate)
# print(step_3)
#
# # step_4
# trable_tram = trable_tram(df, remont, inputDate) # Получаем все трамваи с проблемами
#
# step_3 = full_trable_tram(trable_tram)
# print(step_3)


##################
print("*" * 150)
with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
      print(df)
print("*" * 150)
print(df.nunique())
print("*" * 150)
print(len(df))
print("*" * 150)
# Показывает тип данных
#trable_tram = step_3.dtypes['last_lon_on_camera']

