import greedyThief

N_ = int(input("Сколько экспонатов вы хотите украсть? "))
M_ = int(input("Сколько заходов вы можете сделать? "))
K_ = int(input("Сколько килограммов вы можете унести за один заход? "))

expons = []
expon = list(map(int, input("Введите цену экспоната и его вес (0 0 чтобы завершить): ").split()))
while expon != [0, 0]:
    expons.append(expon)
    expon = list(map(int, input("Введите цену экспоната и его вес (0 0 чтобы завершить): ").split()))

# print(greedyThief.greedyThief([[5000, 27], [200, 5], [3000, 20], [2000, 3], [3000, 10]], 4, 3, 30))
print(greedyThief.greedyThief(expons, N_, M_, K_))