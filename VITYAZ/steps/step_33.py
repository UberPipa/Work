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