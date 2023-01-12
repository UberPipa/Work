from VITYAZ.steps.step_2 import del_col

def clean_df(df): # Очищает список и возвращает его и его длинну в 2 переменные
    clean_df = df.drop_duplicates(subset=["N_sostava"], keep='last') # удаляем дубликаты и не нужные столбцы
    count_df = len(clean_df) # Получаем длинну этого df
    return clean_df, count_df