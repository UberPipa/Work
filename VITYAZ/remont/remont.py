
def read_remont(): # Возвращает список ремонтных
    remont = []
    with open('./remont.txt') as file:
        for i in file:
            remont.append(int(i.strip()))
    return remont