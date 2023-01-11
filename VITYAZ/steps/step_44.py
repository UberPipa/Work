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