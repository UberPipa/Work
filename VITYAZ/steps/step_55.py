# Находит полностью не доступные
def full_trable_tram(trable_tram):
    full_trable_tram = trable_tram.loc[trable_tram['сount_cam'] == trable_tram['real_сount_cam']]  # Удаляет те, где не совпадают флаги

    full_trable_tram = full_trable_tram.drop_duplicates(subset=["N_sostava"],keep='last')  # Делает DF, где все составы без дублирований

    list_full_trable_tram = list(full_trable_tram['N_sostava'])  # Делаем список с составами
    list_full_trable_tram = list(str(i) for i in list_full_trable_tram)  # Делаем строку
    a = '❌Не доступны ' + str(len(full_trable_tram)) + ' шт: ' + ', '.join(list_full_trable_tram)
    return a

# Проблемные это:
# Где 6 из 6 камер не доступны