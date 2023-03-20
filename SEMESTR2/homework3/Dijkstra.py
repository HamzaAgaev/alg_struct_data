import math

infty = math.inf

def Dijkstra(start_ind: int, adjacency_matrix: list) -> list:       # алгоритм Дейкстры (индекс начальной вершины, матрица смежности вершин)
    global infty
    vertices_count = len(adjacency_matrix)                          # считаем кол-во вершин
    go_path = [infty] * vertices_count                           # массив текущих минимальных расстояний до вершин (индексы массива - сами вершины)
    go_path[start_ind] = 0                                          # минимальное расстояние до стартового элемента принимаем за 0
    visited = []                                                    # посещенные вершины (из которых мы считали расстояние)
    shortest_path_len = [0] * vertices_count                        # самые короткие высчитанные расстояния
    go_ind = start_ind                                              # текущая вершина графа, на которой мы находимся
    shortest_path = [[0] for i in range(vertices_count)]            # кратчайшие найденные пути

    while True:                                                     # пока у нас есть непройденные вершины (определяется при помощи has_adjacent)
        has_adjacent = False                                        # есть непройденные вершины = ложь
        adjacency_row = adjacency_matrix[go_ind]                    # строка матрицы смежности текущей вершины (от которой мы отмеряем расстояния до других вершин)
        for adjel_ind in range(vertices_count):                     # проходимся по всем вершинам
            if adjel_ind not in visited:                            # если мы не посещали такую вершину
                adjacency_elem = adjacency_row[adjel_ind]           # высчитываем расстояние от текущей вершины до такой вершины
                has_adjacent = True                                 # у нас есть непройденные вершины = правда
                this_path_len = adjacency_elem + go_path[go_ind]    # выссчитываем расстояние от такой вершины до текущей + минимальное расстояние до текущей вершины
                if this_path_len < go_path[adjel_ind]:              # если это расстояние меньше, чем найденное до этого расстояние до такой вершины
                    go_path[adjel_ind] = this_path_len              # обновляем расстояние до такой вершины
                    shortest_path[adjel_ind] = shortest_path[go_ind] + [adjel_ind]      # кратчайшее найденное расстояние определяем за расстояние до текущей вершины + такая вершина
        
        if has_adjacent:                                            # если есть непройденные вершины
            visited.append(go_ind)                                  # помещаем текущую вершину в пройденные вершины
            min_value = infty                                    # считаем путь до вершины с минимальным путем (помимо нашей текущей)
            min_ind = go_ind                                        # принимаем нашу вершину с минимальным путем как нашу текущую
            for ind in range(vertices_count):                       # проходимся по всем найденным путям
                if go_path[ind] < min_value and ind not in visited: # если расстояние до проверяемой вершины меньше, чем определенный минимальный путь (min_value) и наша вершина не была посещена
                    min_value = go_path[ind]                        # определяем наш минимальный определенный путь как расстояние до проверяемой вершины
                    min_ind = ind                                   # вершина с минимальным путем - проверяемая
            shortest_path_len[min_ind] = go_path[min_ind]           # записываем вершину с минимальным путем в минимальные найденные длины
            # shortest_path[min_ind] = shortest_path[go_ind] + [go_ind]
            go_ind = min_ind                                        # текущая вершина = минимальная найденная (с минимальным путем)
        else:                                                       # если нет непройденных вершин, выходим из цикла
            break

    return shortest_path_len, shortest_path