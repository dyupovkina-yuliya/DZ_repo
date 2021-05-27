#2 Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time_in_sec = input("Введите время в секундах: ")
hour_time = int(time_in_sec) // 3600
min_time = int(time_in_sec) % 3600 // 60
sec_time = int(time_in_sec) % 3600 % 60
print(hour_time, ":", min_time, ":", sec_time)

