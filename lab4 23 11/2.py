import mysorts2
from random import randint

import timeit

while True:
    choosed = int(input("Выберите, какую сортировку вы хотите выполнить:\n1. Блочная сортировка.\n2. Пирамидальная сортировка.\n"))
    if choosed in (1, 2):
        break
    else:
        print("Вы не выбрали алготитм сортировки.")

arr = input("Введите через пробел элементы массива (Enter для случайной генерации 100 чисел от 1 до 1000):\n").split()

if arr == []:
    arr = [randint(1, 10**3) for i in range (10**2)]

arr = list(map(int, arr))

if choosed == 1:
    start = timeit.default_timer()
    print(mysorts2.bucketsort(arr))
    print(timeit.default_timer()-start)
else:
    start = timeit.default_timer()
    print(mysorts2.heapify(arr))
    print(timeit.default_timer()-start)