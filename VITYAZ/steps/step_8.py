import pandas as pd


def join_del_sort_df(df1, df2): # Склеиваем, удаляет дубликаты и сортирует дата фреймы
    frames = [df1, df2] # Делаем переменную с 2мя df
    frames = pd.concat(frames) # соединяем их
    frames = frames.drop_duplicates()  #.reset_index(drop=True) # удаляем дубликаты
    frames = frames.sort_values(by='N_sostava', ascending=False) # сортируем
    return frames