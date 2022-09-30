def checking (matrix): # Проверка матрицы на правильность (на то, что она прямоугольная)

    columns_len = len (matrix [0]) # Высчитаываем длину строки матрицы

    for matr_str in matrix [1:]: # Проходимся по строкам матрицы
        if len (matr_str) != columns_len: # Если длина матрицы изменилась
            return False # Это - не матрица, поэтому возвращаем False
    
    return True # Если же ничего не было обнаружено, возвращаем True



def transposition (matrix): # Транспонирование матрицы
    
    columns_len = len (matrix [0]) # Находим длину и ширину матрицы (кол-во столбцов и строк в ней)
    rows_len = len (matrix)

    result_matrix = [] # Итоговая матрица

    for l in range (columns_len): # Проходимся по кол-ву строк итоговой матрицы
        res_matr_str = []

        for w in range (rows_len): # Проходимся по кол-ву столбцов итоговой матрицы
            res_matr_str.append (matrix [w][l]) # Берем из каждой строки соответствующий столбцу элемент и его в строку

        result_matrix.append (res_matr_str) # Помещаем строку в матрицу

    return result_matrix # Возвращаем готовую матрицу



def multiplying (matrix_1, matrix_2): # Умножение матриц

    def multiply_rows_columns (row, column): # Поэлементное умножение строки на столбец

        mul_value = 0

        for r in range (len (row)): # Умножение элемент столбца на соответствующий элемент строки
            mul_value += row [r] * column [r]

        return mul_value

    columns_len1 = len (matrix_1 [0]) # Кол-во столбцов 1-ой и строк 2-ой матриц
    rows_len2 = len (matrix_2)

    if columns_len1 == rows_len2: # Если оно равно

        rows_res_len = len (matrix_1) # Кол-во строк и столбцов итоговой матрицы
        columns_res_len = len (matrix_2 [0])
        result_matrix = []

        for res_rl in range (rows_res_len): # Заполняем в каждой строке матрицы вместо элементов нули
            res_row = [0] * columns_res_len
            result_matrix.append (res_row)
        
        for i in range (rows_res_len): # Проходимся по строкам итоговой матрицы
            for j in range (columns_res_len): # Проходимся по столбцам итоговой матрицы
                row_from_1 = matrix_1 [i] # Берем строку из 1-ой матрицы
                column_from_2 = []
                for k in range (rows_len2): # При помощи цикла проходимся по строкам 2-ой матрицы, из каждой собираем по нужному элементу для формирования столбца
                    column_from_2.append (matrix_2 [k][j])
                
                result_matrix [i][j] = multiply_rows_columns (row_from_1, column_from_2) # В ячейку итоговой матрицы, запишем результат умножения соответствующего i-той строки 1-ой матрицы на j-тый столбец 2-ой матрицы

        return result_matrix

    else:

        return []



def rank (matrix): # Определение ранга матрицы

    matrix_copy = matrix.copy ()

    for row_copy in matrix_copy: # Убираем нулевые строки
        if row_copy == [0] * len (row_copy):
            matrix.remove (row_copy)

    for row_ind in range (len (matrix)): # Проходимся по строкам 

        delit = 1 # Число, на которое мы будем делить все элементы строки
        for deli in range (len (matrix [row_ind])): # Проходимся по строке чтобы найти первое ненулевое значение
            if matrix [row_ind][deli] != 0: 
                delit = matrix [row_ind][deli] # Это число - первое ненулевое значение в строке
                break # При этом deli - индекс первого ненулевого элемента
        
        if [0] * len (matrix [row_ind]) != matrix [row_ind]: # Если же строка не состоит просто из нулей

            matrix [row_ind] = [matrix [row_ind][i] / delit for i in range (len (matrix [row_ind]))] # Делим все элементы строки на первый ненулевой элемент

            for ind in range (row_ind + 1, len (matrix)): # Для каждой следующей строки 

                coef = matrix [ind][deli] / matrix [row_ind][deli] # находим отношение элемента ind-той строки с индексом deli (с индексом первого ненулевого элемента в строке с индексом row_ind) и элемента row_ind-той строки с индексом deli
                matrix [ind] = [matrix [ind][i] - coef * matrix [row_ind][i] for i in range (len (matrix [ind]))] # для каждого элемента строки ind мы вычитаем из него соответствующий ему элемент строки row_ind, умноженный на coef 

    rank_matrix = len (matrix) # Определяем ранг матрицы как кол-во строк

    for row in matrix: # При нахождении нулевой строки вычитаем из ранга 1
        null = True
        for elem in row:
            if elem != 0:
                null = False
                break
        if null:
            rank_matrix -= 1

    return rank_matrix
    


# Ввод с функциями
to_do = int (input ("Введите 1 для транспонирования матрицы, 2 для умножения матриц, 3 для определения ранга матриц: "))

if to_do in (1, 3): count_matrix = 1
elif to_do == 2: count_matrix = 2

matrixes = []

for count in range (count_matrix):

    print (f"Введите строки матрицы {count} (через Enter), указывая все элементы через пробел (если вы закончили ввод, нажмите Enter): ")

    inp_matr_str = input ()
    matrix_one = []

    while inp_matr_str != '':

        matrix_one.append (list (map (int, inp_matr_str.split ())))
        inp_matr_str = input ()

    matrixes.append (matrix_one)

if count_matrix == 1:

    if checking (matrixes [0]):

        if to_do == 1: print (transposition (matrixes [0]))
        else: print (rank (matrixes [0]))

else:

    if checking (matrixes [0]) and checking (matrixes [1]):
        print (multiplying (matrixes [0], matrixes [1]))