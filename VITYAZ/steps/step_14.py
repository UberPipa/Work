



def col_in_str_plus_cam(df_tram, df_cam): # Возвращает строку составов без номеров камер
    df_tram = list(df_tram['N_sostava'])  # Делаем список с составами
    all_sost = []  # список для всех составов
    for item in df_tram:  # шагаем по списку с составами
        for sost in df_cam['N_sostava']:  # шагаем по списку
            if sost == item:
                index = df_cam.index[df_cam.N_sostava == sost]  # Получаем индекс
                index = index.tolist()  # оборачиваем в лист
                list_cam = []  # временный список для хранения камер
                for i in index:  # находим по индексу номера камер
                    cam = df_cam.loc[i, 'N_camera']  # находим по индексу номера камер
                    list_cam.append(str(cam))  # добавляем в список камеры поочерёдно
                list_cam = ','.join(list_cam)  # делаем строку для вывода для каждого списка камер
                each_sost = f'{sost}({list_cam})'  # переменная для строки со всеми составами
                all_sost.append(each_sost)  # добавляем каждый состав в список
    temp = []  # временный спиоск
    [temp.append(x) for x in all_sost if x not in temp]  # удаляем дубликаты списка
    temp = ', '.join(temp)  # делаем строку
    all_sost = temp  # присваиваем
    return all_sost