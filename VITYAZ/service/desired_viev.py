from datetime import *
import pandas as pd


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
    df[col] = df[col].fillna(0)  # Меняем NaN на 0
    df[col] = df[col].astype(int) # Делаем int

def sort(df, col): # сортирует столбец
    df = df.sort_values(by=col, na_position='first')



