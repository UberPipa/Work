from datetime import *

# Функция на проверку даты
def data_check():
    # Вводим начальную дату
    DD = input('Введите число месяца от которого проверяются детекции в формате ДД (Это число будет включено в диапазон): ')
    MM = input('Введите месяц в формате ММ: ')
    YY = input('Введите год в формате ГГГГ: ')

    # Склеиваем даты
    inputDate = YY + '-' + MM + '-' + DD

    # Проверяем формат даты
    formate = "%Y-%m-%d"
    res = True
    try:
        res = bool(datetime.strptime(inputDate, formate))
    except ValueError:
        res = False

    # Выдаём результат
    if res == True:
        print("Дата выбрана!")
        start_date = inputDate
    else:
        print("Не правильная дата, введите заново")
        data_check()
    # Возвращаем переменную
    return inputDate




# Выбранная дата
#print(datetime.strptime(str(inputDate), '%Y-%m-%d').date())
