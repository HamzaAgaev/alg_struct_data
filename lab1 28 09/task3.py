import numpy as numpy
import timeit

def inverse3x3 (matrix): # Обратная матрица 3x3

    def determinant2x2 (minor): # Детерминант матрицы 2x2

        return minor [0][0] * minor [1][1] - minor [0][1] * minor [1][0]

    def determinant3x3 (mx): # Детерминант матрицы 3x3

        main_diag = mx [0][0] * mx [1][1] * mx [2][2] + mx [0][1] * mx [1][2] * mx [2][0] + mx [1][0] * mx [2][1] * mx [0][2]
        pob_diag = mx [2][0] * mx [1][1] * mx [0][2] + mx [1][0] * mx [0][1] * mx [2][2] + mx [2][1] * mx [1][2] * mx [0][0]

        return main_diag - pob_diag

    rows_len = len (matrix [0]) # Кол-во столбцов и строк исходной матрицы
    columns_len = len (matrix)

    matrix_det = determinant3x3 (matrix) if rows_len == 3 and columns_len == 3 else 0 # Детерминант исходной матрицы

    if rows_len == 3 and columns_len == 3 and matrix_det != 0: # Если строк и столбцов по 3 и у итоговой матрицы детерминант не 0

        result_matrix = [ # Итоговая матрица с нулями
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        for row_ind in range (3): # Проходимся по строкам итоговой матрицы
            
            for el_ind in range (3): # Проходимся по каждому элементу строки

                matrix_copy = [row.copy () for row in matrix] # Создаем копию итоговой матрицы
                matrix_copy.pop (row_ind) # Удаляем строку, где есть наш проверяемый элемент

                for del_ind in range (2): # Проходимся по двум оставшимся строкам копии
                    
                    matrix_copy [del_ind].pop (el_ind) # Удаляем из них элемент, которые находятся под el_ind

                # В итоге получаем минор элемента

                if (row_ind + el_ind) % 2 == 0: alg_dop_coef = 1 # Если в сумме индексы элемента четные, то коэф = 1, иначе -1 
                else: alg_dop_coef = -1

                result_matrix [row_ind][el_ind] = determinant2x2 (matrix_copy) * alg_dop_coef / matrix_det # В соответствующую ячейку записываем алгебраическое дополнение элемента матрицы, деленное на детерминант исходной

        return result_matrix

    else:

        return []



def inverse_numpy (matrix):

    Matrix = numpy.array (matrix)
    return numpy.linalg.inv (Matrix)



print ("Введите строки матрицы 3x3 (через Enter), указывая все элементы через пробел: ")

matr_1st = []

for i in range (3):

    inp_matr_str = input ()
    matr_1st.append (list (map (int, inp_matr_str.split ())))

print (inverse3x3 (matr_1st))



setup_code_1 = """
import numpy as numpy

def inverse3x3 (matrix):

    def determinant2x2 (minor):

        return minor [0][0] * minor [1][1] - minor [0][1] * minor [1][0]

    def determinant3x3 (mx):

        main_diag = mx [0][0] * mx [1][1] * mx [2][2] + mx [0][1] * mx [1][2] * mx [2][0] + mx [1][0] * mx [2][1] * mx [0][2]
        pob_diag = mx [2][0] * mx [1][1] * mx [0][2] + mx [1][0] * mx [0][1] * mx [2][2] + mx [2][1] * mx [1][2] * mx [0][0]

        return main_diag - pob_diag

    rows_len = len (matrix [0])
    columns_len = len (matrix)

    matrix_det = determinant3x3 (matrix) if rows_len == 3 and columns_len == 3 else 0 # Детерминант исходной матрицы

    if rows_len == 3 and columns_len == 3 and matrix_det != 0:

        result_matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        for row_ind in range (3):
            
            for el_ind in range (3):

                matrix_copy = [row.copy () for row in matrix]
                matrix_copy.pop (row_ind)

                for del_ind in range (2):
                    
                    matrix_copy [del_ind].pop (el_ind)

                if (row_ind + el_ind) % 2 == 0: alg_dop_coef = 1
                else: alg_dop_coef = -1

                result_matrix [row_ind][el_ind] = determinant2x2 (matrix_copy) * alg_dop_coef / matrix_det 

        return result_matrix

    else:

        return []
"""

main_block_1 = f"""
inverse3x3 ({matr_1st})
"""

setup_code_2 = """
import numpy as numpy

def inverse_numpy (matrix):

    Matrix = numpy.array (matrix)
    return numpy.linalg.inv (Matrix)
"""

main_block_2 = f"""
inverse_numpy ({matr_1st})
"""

sumtime1 = 0
sumtime2 = 0

for i in range (10):
    time1 = timeit.timeit (setup = setup_code_1, stmt = main_block_1, number = 100)
    time2 = timeit.timeit (setup = setup_code_2, stmt = main_block_2, number = 100)
    sumtime1 += time1
    sumtime2 += time2
    print (time1, time2)

print (sumtime2 / sumtime1)