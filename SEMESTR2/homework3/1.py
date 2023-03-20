import greedyCoins

N = int(input("Введите вашу сдачу: "))
nominals = []
for i in range(1, 5):
    count_nominal = list(map(int, input(f"Введите кол-во {i} монет и их номинал: ").split()))
    nominals.append(count_nominal)

change_ = greedyCoins.greedyCoins(N, nominals)
print(change_)