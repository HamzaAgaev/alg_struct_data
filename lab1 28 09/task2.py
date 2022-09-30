import numpy

def checking (matrix): # Проверка матрицы на правильность (на то, что она прямоугольная)

    columns_len = len (matrix [0]) # Высчитаываем длину строки матрицы

    for matr_str in matrix [1:]: # Проходимся по строкам матрицы
        if len (matr_str) != columns_len: # Если длина матрицы изменилась
            return False # Это - не матрица, поэтому возвращаем False
    
    return True # Если же ничего не было обнаружено, возвращаем True



def transposition_numpy (matrix):

    Matrix = numpy.array (matrix)
    return Matrix.transpose ()



def multiplying_numpy (martix_1, matrix_2):

    Matrix_1 = numpy.array (martix_1)
    Matrix_2 = numpy.array (matrix_2)

    return numpy.matmul (Matrix_1, Matrix_2)



def rank_numpy (matrix):

    Matrix = numpy.array (matrix)
    return numpy.linalg.matrix_rank (Matrix)



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

        if to_do == 1: print (transposition_numpy (matrixes [0]))
        else: print (rank_numpy (matrixes [0]))

else:

    if checking (matrixes [0]) and checking (matrixes [1]):
        print (multiplying_numpy (matrixes [0], matrixes [1]))