'''
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма.
Например, прибыль — выручка больше издержек, или убыток —
издержки больше выручки. Выведите соответствующее
сообщение.
Если фирма отработала с прибылью, вычислите рентабельность
выручки. Это отношение прибыли к выручке. Далее запросите
численность сотрудников фирмы и определите прибыль фирмы
в расчете на одного сотрудника.
'''
receipt = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
prof = receipt - costs
if receipt > costs:
    print('Прибыль -', prof)
    margin = (prof /  receipt) * 100
    print('Рентабельность -', margin, '%')
    numb_empl = int(input('Введите численность сотрудников фирмы: '))
    marg_empl = prof / numb_empl
    print('Прибыль на одного сотрудника -', marg_empl)
elif receipt < costs:
    print('Убыток -', prof)