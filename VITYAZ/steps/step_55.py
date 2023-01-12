def total_in_the_sphere(df_сount_cam): # Выводит количество сколько всего заведено в Сферу
    a = '🔸Всего заведено в Сферу: ' + str(len(df_сount_cam.index)) + ' шт.'
    return a
# 🔸Всего заведено в Сферу: 392 шт.


def count_rem(remont_list): # Выводит количество сколько в ремонте
    a = '🛠Всего в ремонте: ' + str(len(remont_list)) + ' шт.'
    return a
# 🔸Всего заведено в Сферу: 392 шт.
# 🛠Всего в ремонте: 62 шт.



import pandas as pd

def all_good(df, remont, inputDate): # Выводит количество сколько работает 100%
    df = df[(df.N_sostava.isin(remont)) == False]  # Проверяем вхождение ремонтных составов и удаляем их
    df = pd.DataFrame(df)  # 1 - Убираем строкти со значением Null во всём df, включая широту и долготу
    df = df.dropna() # 2 - Убираем строкти со значением Null во всём df, включая широту и долготу
    df = df.loc[df['last_time_check_on_camera'] >= inputDate]  # Отсеиваем по дате
    df['real_сount_cam'] = df.groupby('N_sostava')['N_sostava'].transform('size')  # Делаем количесво (Флаги!), сколько есть камер на самом деле
    df = df.drop_duplicates(subset=["N_sostava"], keep='last')  # Делает DF, где все составы без дублирований
    df = df.loc[df['сount_cam'] == df['real_сount_cam']]  # Удаляет те, где не совпадают флаги
    a = '✅Полностью рабочие составы: ' + str(len(df)) + ' шт.'
    return a
# 1 Берём все составы
# 2 Убираем ремонтные | Убираем Нулл | отсеиваем по времени
# 3 Проверяем по флагам на доступность всех камер

# 🔸Всего заведено в Сферу: 392 шт.
# 🛠Всего в ремонте: 62 шт.
# ✅Полностью рабочие составы: 160 шт.




# Находит все проблемные трамваи
def trable_tram(df, remont, inputDate):
    df = df[(df.N_sostava.isin(remont)) == False] # Ищем те трамваи, у которых есть какие либо проблемы
    # Выбираем проблемные трамваи
    df = df[
            (df['last_time_check_on_camera'].isnull()) |
            (df['last_lat_on_camera'].isnull()) |
            (df['last_lon_on_camera'].isnull()) |
            (df['last_time_check_on_camera'] < inputDate)
            ]
    df['real_сount_cam'] = df.groupby('N_sostava')['N_sostava'].transform('size')  # Делаем количесво (Флаги!), сколько есть камер на самом деле
    return df

# Проблемные это:
# 1) Время больше нормы
# 2) Нет гео
# 1) Нет детекций




# Находит полностью не доступные
def full_trable_tram(trable_tram):
    full_trable_tram = trable_tram.loc[trable_tram['сount_cam'] == trable_tram['real_сount_cam']]  # Удаляет те, где не совпадают флаги

    full_trable_tram = full_trable_tram.drop_duplicates(subset=["N_sostava"],keep='last')  # Делает DF, где все составы без дублирований

    list_full_trable_tram = list(full_trable_tram['N_sostava'])  # Делаем список с составами
    list_full_trable_tram = list(str(i) for i in list_full_trable_tram)  # Делаем строку
    a = '❌Не доступны ' + str(len(full_trable_tram)) + ' шт: ' + ', '.join(list_full_trable_tram)
    return a

# Проблемные это:
# Где 6 из 6 камер не доступны