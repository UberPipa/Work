import numpy as np
import pandas as pd
from pandas import read_csv

# - читаем из CVS
# - читаем ремонт
def create_df(name_df):  # читает из CVS
    name_df = read_csv("./test.csv")
    name_df = pd.DataFrame(name_df)
    return name_df

def read_remont(): #  Читает и возвращает список ремонтных составов с вендорами
    name_df = read_csv("./remont.txt", names=['rem_tram'], header=None)
    name_df = pd.DataFrame(name_df)
    return name_df















