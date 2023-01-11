import numpy as np
import pandas as pd

def del_arch(name_df): # Удаляет архивные по условию
    name_df.drop(name_df[name_df['status'] == '-'].index, inplace=True)
    return name_df
def pars_col(df, name_new_col, num_split_index): # парсит столбец по образцу - ff_ngpt_tram_vitaz_31001_1
    df[name_new_col] = df.camera.str.split('_').str[num_split_index]
def del_col(df, col): # удаляет столбец
    df.pop(col)
def str_to_data(df, col): # Переделывает в datetime и ибавляемся от миллисекунд в last_time_check_on_camera
    df[col] = pd.to_datetime(df[col])
    df[col] = df[col].dt.ceil('T')
def str_to_int(df, col): # меняет str на int
    df[col] = df[col].astype(int)
def float_to_int(df, col): # меняет float на int, делает не угодные значения nan
    df[col] = pd.to_numeric(df[col].round(), errors='coerce').astype('Int64')
    df[col] = df[col].replace({0: np.nan})
    df[col] = df[col].replace({90: np.nan})
    df[col] = df[col].replace({-90: np.nan})