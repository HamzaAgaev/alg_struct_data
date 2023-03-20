from Dijkstra import *

stations_indexes = (("Oxford Circus", 0), ("Bond Street", 1), ("Green Park", 2), ("Piccadilly Circus", 3), ("Leicester Square", 4), ("Tottenham Court Road", 5), ("Goodge Street", 6), ("Warren Street", 7), ("Regent's Park", 8), ("Baker Street", 9), ("Holborn", 10))
London_metro = [
    [0, 1, 1, 3, infty, 2, infty, 4, 2, infty, infty],
    [1, 0, 1, infty, infty, infty, infty, infty, infty, 3, infty],
    [1, 1, 0, 2, infty, infty, infty, infty, infty, infty, infty],
    [3, infty, 2, 0, 1, infty, infty, infty, infty, infty, infty],
    [infty, infty, infty, 1, 0, 1, infty, infty, infty, infty, 2],
    [2, infty, infty, infty, 1, 0, 1, infty, infty, infty, 1],
    [infty, infty, infty, infty, infty, 1, 0, 3, infty, infty, infty],
    [4, infty, infty, infty, infty, infty, 3, 0, infty, 2, infty],
    [2, infty, infty, infty, infty, infty, infty, infty, 0, 2, infty],
    [infty, 3, infty, infty, infty, infty, infty, 2, 2, 0, infty],
    [infty, infty, infty, infty, 2, 1, infty, infty, infty, infty, 0]
]

print("Выберите станцию метро, на которой вы находитесь:")
for st in stations_indexes:
    print(f"{st[0]} - {st[1]}") 
start_station = int(input())

print("Выберите станцию метро, до которой вам надо доехать:")
for st in stations_indexes:
    print(f"{st[0]} - {st[1]}")
end_station = int(input())

path = Dijkstra(start_station, London_metro)
print(f"Как добраться от {stations_indexes[start_station][0]} до {stations_indexes[end_station][0]}:")
for st in range(len(path[1][end_station]) - 1):
    print(f"{stations_indexes[path[1][end_station][st]][0]} -> {stations_indexes[path[1][end_station][st + 1]][0]}")
print(f"Время пути: {path[0][end_station]} мин.")
# D = [[0, 7, 9, infty, infty, 14],
# [7, 0, 10, 15, infty, infty],
# [9, 10, 0, 11, infty, 2],
# [infty, 15, 11, 0, 6, infty],
# [infty, infty, infty, 6, 0, 9],
# [14, infty, 2, infty, 9, 0]]

# D = ((0, 3, 1, 3, infty, infty),
#      (3, 0, 4, infty, infty, infty),
#      (1, 4, 0, infty, 7, 5),
#      (3, infty, infty, 0, infty, 2),
#      (infty, infty, 7, infty, 0, 4),
#      (infty, infty, 5, 2, 4, 0))
