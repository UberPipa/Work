from pandas import read_csv
from VITYAZ.steps.step_1 import *
from VITYAZ.steps.step_2 import *
from VITYAZ.steps.step_3 import *
from VITYAZ.steps.step_4 import *
from VITYAZ.steps.step_5 import *
from VITYAZ.steps.step_8 import *
from VITYAZ.steps.step_11 import *
from VITYAZ.steps.range_date import *
from VITYAZ.steps.step_55 import *
pd.options.mode.chained_assignment = None #Выключает предупреждения

inputDate = '2023-01-02'

# Step_1
df = create_df('df') # Читаем и делаем df
df_remont = read_remont() # Считывает и хранит ремонтные составы списком

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
df['сount_cam'] = df.groupby('N_sostava')['N_sostava'].transform('size') # Делаем флаг с количесвом камер для cоставов с количесвом камер для каждого состава
df = df[['vendor', 'N_sostava', 'N_camera', 'last_time_check_on_camera', 'last_lat_on_camera', 'last_lon_on_camera', 'сount_cam']] # упорядочеваем столбцы
df = df.sort_values(by=['N_sostava', 'N_camera']) # Двойная сортировка массива по N_sostava затем N_camera

# Step_3
clean_df_all, count_df  = clean_df(df) # Делает чистый df без дублирования и считает его длинну, возвращает в 2 переменные
count_remont = len(df_remont) # Количество ремонтных всего
df_remont = clean_df_all[(clean_df_all['N_sostava'].isin(df_remont['N_sostava'])) == True] # Хранит ремонтные составы, делается по чистому DF
df_without_remont = df[(df['N_sostava'].isin(df_remont['N_sostava'])) == False] # Хранит все составы без ремонтных, удаляет ремонтные

# Step_4
df_all_bed_cam = df_without_remont[(df_without_remont['last_time_check_on_camera'].isnull()) | (df_without_remont['last_time_check_on_camera'] < inputDate)]  # Получаем камеры, частично или полностью без детекций
df_all_bed_tram, count_all_bed_tram = clean_df(df_all_bed_cam) # Делает чистый df без дублирования и считает его длинну, возвращает в 2 переменные

# Step_5
df_full_all_bed_cam = real_flag(df_all_bed_cam) # Присваивает новые флаги с реальным количеством камер
df_full_all_bed_cam = df_full_all_bed_cam.loc[df_full_all_bed_cam['сount_cam'] == df_full_all_bed_cam['real_сount_cam']]  # оставляем полностью не доступные
df_full_all_bed_tram, count_full_all_bed_tram = clean_df(df_full_all_bed_cam)  # Делает чистый df без дублирования и считает его длинну, возвращает в 2 переменные

# Step_6
df_bed_cam = df_all_bed_cam.loc[df_all_bed_cam['сount_cam'] != df_all_bed_cam['real_сount_cam']]  # Берём df_full_all_bed_cam с флагами камер и минусуем не доступные df_full_all_bed_tram
df_bed_tram, count_bed_tram = clean_df(df_bed_cam)  # Делает чистый df без дублирования и считает его длинну, возвращает в 2 переменные

# Step_7
df_all_without_geo_cam = df_without_remont[(df_without_remont['last_time_check_on_camera'] > inputDate)] # Сортировка в рамках недели
df_all_without_geo_cam = df_all_without_geo_cam[(df_all_without_geo_cam['N_sostava'].isin(df_all_bed_cam['N_sostava'])) == False] # Проверяем df_without_geo на вхождения из списка из (df_all_bed_cam) и удаляем составы, должны получиться почти все рабочие составы, нужно будет найти только составы без гео данных
df_all_without_geo_cam = df_all_without_geo_cam[(df_all_without_geo_cam['last_lat_on_camera'].isnull()) | (df_all_without_geo_cam['last_lon_on_camera'].isnull())] # Находим трамваи без гео данных
df_all_without_geo_cam = real_flag(df_all_without_geo_cam) # Присваивает новые флаги с реальным количеством камер
df_all_without_geo_tram, count_df_all_without_geo_tram = clean_df(df_all_without_geo_cam)  # Делает чистый df без дублирования и считает его длинну, возвращает в 2 переменные
full_df_all_without_geo_cam = df_all_without_geo_cam.loc[df_all_without_geo_cam['сount_cam'] == df_all_without_geo_cam['real_сount_cam']]  # Смотрим полностью без гео позиции
full_df_without_geo_tram, count_without_geo_tram = clean_df(full_df_all_without_geo_cam)  # Делает чистый df без дублирования и считает его длинну, возвращает в 2 переменные
df_without_geo_cam = df_all_without_geo_cam.loc[df_all_without_geo_cam['сount_cam'] != df_all_without_geo_cam['real_сount_cam']] # Смотрим частично без гео позиции
df_without_geo_tram, count_df_without_geo_tram = clean_df(df_without_geo_cam)  # Делает чистый df без дублирования и считает его длинну, возвращает в 2 переменные

# Step_8
temp = join_del_sort_df(df_all_bed_tram, df_all_without_geo_tram) # Склеиваем, удаляет дубликаты и сортирует дата фреймы
df_full_good_cam = df_without_remont[~(df_without_remont['N_sostava'].isin(temp['N_sostava']))] # Исключаем косячные из df
df_full_good_tram, count_df_full_good_tram = clean_df(df_full_good_cam) # Делает чистый df без дублирования и считает его длинну, возвращает в 2 переменные

# Step_9
vl_df = df[(df['vendor'] == 'vl')] # Все составы vl
all_vl_df_tram, count_all_vl_df_tram = clean_df(vl_df) # Делает чистый df без дублирования и считает его длинну, возвращает в 2 переменные
tv_df = df[(df['vendor'] == 'tv')] # Все составы tv
all_tv_df_tram, count_all_tv_df_tram = clean_df(tv_df) # Делает чистый df без дублирования и считает его длинну, возвращает в 2 переменные

# Step_10
vl_df_remont = df_remont[(df_remont['vendor'] == 'vl')] # Все составы vl
temp, count_vl_df_remont = clean_df(vl_df_remont) # Делает чистый df без дублирования и считает его длинну, возвращает в 2 переменные
tv_df_remont = df_remont[(df_remont['vendor'] == 'tv')] # Все составы vt
temp, count_tv_df_remont = clean_df(tv_df_remont) # Делает чистый df без дублирования и считает его длинну, возвращает в 2 переменные

# Step_11
vl_df_full_all_bed_tram = df_full_all_bed_tram[(df_full_all_bed_tram['vendor'] == 'vl')] # Все составы vl
temp, count_vl_df_full_all_bed_tram = clean_df(vl_df_full_all_bed_tram) # Делает чистый df без дублирования и считает его длинну, возвращает в 2 переменные
vl_str_full_all_bed_tram = col_in_str(vl_df_full_all_bed_tram) # Переделываем столбец в строку
tv_df_full_all_bed_tram = df_full_all_bed_tram[(df_full_all_bed_tram['vendor'] == 'tv')] # Все составы tv
temp, count_tv_df_full_all_bed_tram= clean_df(tv_df_full_all_bed_tram) # Делает чистый df без дублирования и считает его длинну, возвращает в 2 переменные
tv_str_full_all_bed_tram = col_in_str(tv_df_full_all_bed_tram) # Переделываем столбец в строку

# step_12
df_available_all_cam = df_without_remont[~(df_without_remont['N_sostava'].isin(df_full_all_bed_cam['N_sostava']))]# Ищем доступные Все
df_available_all_tram, count_df_available_all_tram = clean_df(df_available_all_cam) # Делает чистый df без дублирования и считает его длинну, возвращает в 2 переменные

# step_13
vl_df_available_all_cam = df_available_all_cam[(df_available_all_cam['vendor'] == 'vl')] # Все составы vl
vl_df_available_all_tram, count_vl_df_available_all_tram = clean_df(vl_df_available_all_cam) # Делает чистый df без дублирования и считает его длинну, возвращает в 2 переменные

tv_df_available_all_cam = df_available_all_cam[(df_available_all_cam['vendor'] == 'tv')] # Все составы tv
tv_df_available_all_tram, count_tv_df_available_all_tram = clean_df(tv_df_available_all_cam) # Делает чистый df без дублирования и считает его длинну, возвращает в 2 переменные

# step_14
vl_df_bed_cam = df_bed_cam[(df_bed_cam['vendor'] == 'vl')] # Все составы vl
vl_df_bed_tram, count_vl_df_bed_tram = clean_df(vl_df_bed_cam) # Делает чистый df без дублирования и считает его длинну, возвращает в 2 переменные
tv_df_bed_cam = df_bed_cam[(df_bed_cam['vendor'] == 'tv')] # Все составы tv
tv_df_bed_tram, count_tv_df_bed_tram = clean_df(tv_df_bed_cam) # Делает чистый df без дублирования и считает его длинну, возвращает в 2 переменные





parampam = vl_df_bed_cam     # Печатает

############################################ Работа с датой
# Вызываем функцию из модуля и выбираем дату
# inputDate = (data_check())
# Конверируем строку в дату и снова в строку
# inputDate = str(datetime.strptime(str(inputDate), '%Y-%m-%d').date())
# Текущая дата
today = date.today()
# inputDate = datetime.strptime(str('2022-12-19'), '%Y-%m-%d').date()
#inputDate = datetime.datetime.strptime(inputDate, '%Y-%m-%d') # На всякий случай если не будет робить
############################################

def void(void):
      print("*" * 150)
      print(f'🔸Всего заведено в Сферу: {count_df} шт. ')
      print(f'🛠Всего в ремонте: {count_remont} шт. ')
      print(f'❌Частично или полностью без детекций: {count_all_bed_tram} шт. ')
      print(f'✅Полностью рабочие составы: {count_df_full_good_tram} шт. ')
      print(' ')

      print('‼️VisionLab')
      print(f'🔸Всего: {count_all_vl_df_tram} шт. ')
      print(f'🛠В ремонте: {count_vl_df_remont} шт. ')
      print(f'❌Не доступны: {count_vl_df_full_all_bed_tram} шт. : {vl_str_full_all_bed_tram}.')
      print(f'✅Доступны: {count_vl_df_available_all_tram} шт. – из них: ')
      print(f'**** ⚠️Детекции свежие не со всех камер: {count_vl_df_bed_tram} шт. : ')

      print(' ')
      print('‼️Tevian')
      print(f'🔸Всего: {count_all_tv_df_tram} шт. ')
      print(f'🛠В ремонте: {count_tv_df_remont} шт. ')
      print(f'❌Не доступны: {count_tv_df_full_all_bed_tram} шт. : {tv_str_full_all_bed_tram}.')
      print(f'✅Доступны: {count_tv_df_available_all_tram} шт. – из них: ')
      print(f'**** ⚠️Детекции свежие не со всех камер: {count_tv_df_bed_tram} шт. : ')


      print(' ')
      print('*********   Полностью не робит - ' + str(count_full_all_bed_tram))
      print('*********   Робит частично - ' + str(count_bed_tram))
      print('*********   Полностью без гео позиции - ' + str(count_without_geo_tram))
      print('*********   Частично без гео позиции - ' + str(count_df_without_geo_tram))
      print(' ')
      print("*" * 150)
      with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
            print(void)
      print("*" * 150)
      print(void.nunique())
      print("*" * 150)
      print(str(len(void)) + ' Len этого дерьма')
      print("*" * 150)

void(parampam)

# df
# df_remont