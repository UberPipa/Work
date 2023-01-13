



def col_in_str_plus_cam(df): # Возвращает строку составов без номеров камер
    df = list(df['N_sostava'])  # Делаем список с составами



    # df = list(str(i) for i in df)  # Делаем строку
    # df = ', '.join(df) # Делаем строку
    return df