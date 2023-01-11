import numpy as np
import pandas as pd
from pandas import read_csv

# - читаем из CVS
# - читаем ремонт
def create_df(name_df):  # читает из CVS
    name_df = read_csv("./test.csv")
    name_df = pd.DataFrame(name_df)
    return name_df

def read_remont(): #  Читает и возвращает список ремонтных составов
    remont = []
    with open('./remont.txt') as file:
        for i in file:
            remont.append(int(i.strip()))
    return remont












def del_col(df, col): # удаляет столбец
    df.pop(col)
    #print("Столбец " + col + " удалён")
    # df = df.drop(['camera'], axis=1) - !!!Альтернативный метод
def pars_col(df, name_new_col, num_split_index): # парсит столбец по образцу - ff_ngpt_tram_vitaz_31001_1
    df[name_new_col] = df.camera.str.split('_').str[num_split_index]

def str_to_data(df, col): # Переделывает в datetime и зибавляемся от миллисекунд в last_time_check_on_camera
    df[col] = pd.to_datetime(df[col])
    df[col] = df[col].dt.ceil('T') # Альтернатива 1
    # df[col] = df[col].astype("datetime64[ns]") # Альтернатива 2
    # df[col] = df[col].dt.to_period("D") # Альтернатива 2

def str_to_int(df, col): # меняет str на int
    # df[col] = pd.to_numeric(df[col], downcast='signed')
    df[col] = df[col].astype(int)

def float_to_int(df, col): # меняет float на int
    df[col] = pd.to_numeric(df[col].round(), errors='coerce').astype('Int64')
    df[col] = df[col].replace({0: np.nan})
    df[col] = df[col].replace({90: np.nan})
    df[col] = df[col].replace({-90: np.nan})
    # ПРЕДЫДУШИЙ ВАРИАНТ
    # df[col] = df[col].fillna(0)  # Меняем NaN на 0
    # df[col] = df[col].astype(int) # Делаем int

def sort(df, col): # сортирует столбец
    df = df.sort_values(by=col, na_position='first')

def all_count_cam(df): # Делает DF, где все составы без дублирований
    df_сount_cam = df[['N_sostava', 'сount_cam']]
    # удаляем дубликаты и не нужные столбцы
    df_сount_cam = df.drop_duplicates(subset=["N_sostava"], keep='last')
    return df_сount_cam