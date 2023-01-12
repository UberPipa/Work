from pandas import read_csv
from VITYAZ.steps.step_1 import *
from VITYAZ.steps.step_2 import *
from VITYAZ.steps.step_3 import *
from VITYAZ.steps.step_4 import *
from VITYAZ.steps.step_5 import *
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
df = df[(df['N_sostava'].isin(df_remont['N_sostava'])) == False] # Хранит все составы без ремонтных, удаляет ремонтные

# Step_4
df_all_bed_cam = df[(df['last_time_check_on_camera'].isnull()) | (df['last_time_check_on_camera'] < inputDate)]  # Получаем камеры, частично или полностью без детекций
df_all_bed_tram, count_all_bed_tram = clean_df(df_all_bed_cam) # Делает чистый df без дублирования и считает его длинну, возвращает в 2 переменные


# Step_5
df_full_all_bed_cam = real_flag(df_all_bed_cam) # Присваивает новые флаги с реальным количеством камер
df_full_all_bed_cam = df_full_all_bed_cam.loc[df_full_all_bed_cam['сount_cam'] == df_full_all_bed_cam['real_сount_cam']]  # оставляем полностью не доступные
df_full_all_bed_tram, count_full_all_bed_tram = clean_df(df_full_all_bed_cam)  # Делает чистый df без дублирования и считает его длинну, возвращает в 2 переменные

# Step_6
df_bed_cam = df_all_bed_cam.loc[df_all_bed_cam['сount_cam'] != df_all_bed_cam['real_сount_cam']]  # Берём df_full_all_bed_cam с флагами камер и минусуем не доступные df_full_all_bed_tram
df_bed_tram, count_bed_tram = clean_df(df_bed_cam)  # Делает чистый df без дублирования и считает его длинну, возвращает в 2 переменные




parampam = df_bed_tram # Печатает

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
      print('*********   Полностью не робит - ' + str(count_full_all_bed_tram))
      print('*********   Робит частично - ' + str(count_bed_tram))
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