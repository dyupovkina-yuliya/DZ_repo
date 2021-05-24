'''
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
'''
my_list = list(input('Введите: '))
new_list = list()
num = 0
for el in my_list:
    inter_list = my_list[num:num+2]
    inter_list.reverse()
    new_list.extend(inter_list)
    num = num + 2
print(new_list)

