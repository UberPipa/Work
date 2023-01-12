from VITYAZ.steps.step_2 import del_col

def clean_df(df): # Делает DF, где все составы без дублирований
    df = df.drop_duplicates(subset=["N_sostava"], keep='last') # удаляем дубликаты и не нужные столбцы
    del_col(df, 'N_camera') # Вызвали функцию
    return df