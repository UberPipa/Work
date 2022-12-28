from datetime import *

# Текущая дата
today = date.today()
print(today)


# Вводим начальную дату
DD = input('Введите число от которого проверяются детекции: ')
MM = input('Введите месяц(например 07): ')
YY = input('Введите  год:(например 2022) ')
inputDate = YY + '-' + MM + '-' + DD


# Проверяем дату
year, month, day = inputDate.split('-')

isValidDate = True
try:
    datetime(int(year),int(month),int(day))
except ValueError :
    isValidDate = False

if(isValidDate) :
    print ("Дата подходит, выбрана " + inputDate)
else :
    print ("Усп, дата не правильная")


#print(inputDate)

