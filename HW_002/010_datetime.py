# модуль datetime
# # № 1
# # дата и врремя в данный момент
# from datetime import datetime
# dt_now = datetime.now() # берет с компьютера
# print(dt_now)
#
# dt2 = datetime(2015, 5, 16, 8, 3, 44) # можно задать дату и время самостоятельно
#
# # математические действия
# delta = dt_now - dt2
# print (delta)
#
# dt3 = dt2 + delta
# print(dt3)
#


# # № 2
# from datetime import date, timedelta
# dt = date(2000, 1, 1)
# print(dt)
#
# delta = timedelta(days = 1)
# print(delta)
# print(dt - delta)
# print(dt + delta)

#
# # № 3 вывод даты на экран
from datetime import datetime
dt_now = datetime.now()
print(dt_now.strftime('%d.%m.%Y %H:%m')) # srtftime - задает формат даты. сохранить дату, как строку
print(dt_now.strftime('%Y-%m-%d'))
print(dt_now.strftime('%A %d %B %Y')) # вывод даты ввиде текста
#
# # (НЕ РАБОТАЕТ!!!!) выведем дату и время на русском
# import locale # locale - локальные языковые настройки даты
# locale.setlocale(locale.LC_TIME, "ru_RU") # указываем, что locale - русская
# print(dt_now.strftime('%A %d %B %Y'))

# получение даты из строки
date_string = '12/23/2010'
date_dt = datetime.strptime(date_string, '%m/%d/%Y') # strptime - полуение даты из строки
print(date_dt)
