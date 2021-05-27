'''
2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные
аргументы. Осуществить вывод данных о пользователе одной строкой.
'''

def user_data(name, surname, birth_year, living_city, email, tel_numb):
    print(name, surname, birth_year, living_city, email, tel_numb)
    return

print(user_data(name='Ivan', surname='Petrov', birth_year='1917', living_city='Voronezh', email='ivan@mail.ru', tel_numb='+79851472315'))