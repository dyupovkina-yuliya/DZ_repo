'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
весна, лето, осень). Напишите решения через list и через dict.
'''
#month = int(input("Введите номер месяца: "))
#if month < 3:
#   print('Это зима')
#if month >=3 and month < 6:
#    print('это весна')
#if month >= 6 and month < 9:
#   print('Это лето')

my_dict = {12: 'winter', 1: 'winter', 2: 'winter', 3: 'sping', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer',
           8: 'summer', 9: 'autгmn', 10: 'autumn', 11: 'autumn'}
print(my_dict)
month = int(input('Введите месяц: '))
print(my_dict.get(month))