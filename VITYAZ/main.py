from pandas import read_csv
from VITYAZ.service.desired_viev import *
from VITYAZ.service.range_date import *
from VITYAZ.remont.remont import *
from VITYAZ.steps.step_1 import *

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

# Делаем флаг для cоставов с количесвом камера для каждого состава
df['сount_cam'] = df.groupby('N_sostava')['N_sostava'].transform('size')

# Делаем отдельный DF для составов и количества камер
df_сount_cam = df[['N_sostava', 'сount_cam']]
# удаляем дубликаты и не нужные столбцы
df_сount_cam = df_сount_cam.drop_duplicates(subset=["N_sostava"], keep='last')
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

############################################ Работа с данными
# вывод сколько всего в сфере трамваев
#total_in_the_Sphere()













# Ищем полностью не доступные камеры
# Not_available = (df['last_time_check_on_camera'].isnull()) | (df['last_time_check_on_camera'] < inputDate)
# Not_available = df.loc[Not_available]


# Считывание ремонтных составов и запись в список remont
# remont = (read_remont())
# # Проверяем вхождение ремонтных составов и удаляем их
# df = df[(df.N_sostava.isin(remont)) == False]



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

# вывод DF
# with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
#      print(full_out)



with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
      print(df)


# Подсчёт уникальных вхождений
#print(df.nunique())

# Показывает тип данных
# df = df.dtypes['last_lon_on_camera']
# with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
#       print(df)
