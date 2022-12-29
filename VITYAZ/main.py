from pandas import read_csv
from desired_viev import *
from range_date import *

# Читаем и делаем df
df_csv = read_csv("test.csv")
df = pd.DataFrame(df_csv)

############################################ Приводим в надлежащий вид
# Парсим столбец
pars_col(df, 'vendor', 0)
pars_col(df, 'name_tram', -3)
pars_col(df, 'N_sostava', -2)
pars_col(df, 'N_camera', -1)

# Переделываем в datetime и и збавляемся от миллисекунд в last_time_check_on_camera
str_to_data(df, 'last_time_check_on_camera')

# удоляем не нужные столбцы
del_col(df, 'camera')
del_col(df, 'status')

# упорядочеваем столбцы
df = df[['vendor', 'name_tram', 'N_sostava', 'N_camera', 'last_time_check_on_camera', 'last_lat_on_camera', 'last_lon_on_camera']]

# меняем на int
str_to_int(df, "N_sostava")
str_to_int(df, "N_camera")
str_to_int(df, "last_lat_on_camera")
str_to_int(df, "last_lat_on_camera")

# сортировка массива
sort(df, 'last_time_check_on_camera')

# Удаление 1го попавшегося дубликата
df = df.drop_duplicates(subset=['N_camera', "N_sostava"], keep='last')

# Двойная сортировка массива по N_sostava затем N_camera
df = df.sort_values(by=['N_sostava', 'N_camera'])

# Считывание ремонтных составов и запись в список remont
remont = (read_remont())

# Проверяем вхождение ремонтных составов и удаляем их
df = df[(df.N_sostava.isin(remont)) == False]
############################################

############################################ Работа с датой
# Вызываем функцию из модуля и выбираем дату
#inputDate = (data_check())
# Конверируем строку в дату
#inputDate = datetime.strptime(str(inputDate), '%Y-%m-%d').date() !!!!!!!!! удалить после отладки
# Текущая дата
today = date.today()
inputDate = datetime.strptime(str('2022-12-19'), '%Y-%m-%d').date()
############################################

############################################ Работа с данными
# Ищем не доступные камеры
full_out = df.query('last_time_check_on_camera < inputDate')


# Новый df с составами у который проблемы с геоданными
geo_problem = df.query('(last_lat_on_camera==0 or last_lat_on_camera==90 or last_lat_on_camera==-90) or (last_lon_on_camera==0 or last_lon_on_camera==90 or last_lon_on_camera==-90)')
# удоляем дубликаты и не нужные столбцы
geo_problem = geo_problem.drop_duplicates(subset=["N_sostava"], keep='last')
del_col(geo_problem, 'N_camera')
del_col(geo_problem, 'last_time_check_on_camera')






# #### Определение диапазона дат
# # Вызываем функцию из модуля и выбираем дату
# inputDate = (data_check())
# # Конверируем строку в дату
# inputDate = datetime.strptime(str(inputDate), '%Y-%m-%d').date()
# # Текущая дата
# today = date.today()


# Ищем те, у которых гео данные отсутвуют и добавляем их в список







# вывод DF
with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
     print(full_out)

# with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
#       print(geo_problem)





# Подсчёт уникальных вхождений
# print(geo_problem.nunique())


# Нужно определить что выбивается за рамки недели относительно сегодняшнего дня и получить сколько:
#                   1) Всего заведено;
#                   2) Всего в ремонте;
#                   3) Не доступны частично или полность(Включая геоданные)
#                   4) Сколько полностью доступны.
