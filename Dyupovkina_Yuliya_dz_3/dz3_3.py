'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух
аргументов.
'''

def summ_max(num1, num2, num3):
    num_list = [num1, num2, num3]
    maxi_1 = max(num_list)
    num_list.remove(maxi_1)
    maxi_2 = max(num_list)
    res = maxi_1 + maxi_2
    print(res)
    return

summ_max(num1=float(input('Enter number 1: ')), num2 = float(input('Enter number 2: ')), num3 = float(input('Enter number 3: ')))


