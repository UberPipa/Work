def all_count_cam(df): # Делает DF, где все составы без дублирований
    df_сount_cam = df[['N_sostava', 'сount_cam']]
    # удаляем дубликаты и не нужные столбцы
    df_сount_cam = df.drop_duplicates(subset=["N_sostava"], keep='last')
    return df_сount_cam