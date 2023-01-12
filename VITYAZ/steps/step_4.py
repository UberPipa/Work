from VITYAZ.steps.step_3 import clean_df
# Ищем частично не доступные
def clean_df_and_count(df, inputDate): # Очищает список и возвращает его и его длинну в 2 переменные
    clean_df_all_bed = clean_df(df)  # Получаем очищенный список трамваев без детекций
    count_all_bed_cam = len(clean_df_all_bed) # Получаем длинну этого df
    return clean_df_all_bed, count_all_bed_cam










