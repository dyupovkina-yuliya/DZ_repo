'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''
def devision_func(x, y):
    '''
    Возвращает частное от деления.
    Аргументы:
    х - делимое,
    y - делитель
    '''
    try:
        res = x / y
    except ZeroDivisionError:
        print('0 not allowed')
        return
    return res

print(devision_func(float(input('Enter number 1: ')), float(input('Enter number 2: '))))

