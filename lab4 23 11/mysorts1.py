import math

def qsort(array: list) -> list:    
    if len(array) <= 1:
        return array    
    left = []
    right = []
    point = array[0]
    for i in range(1, len(array)):
        if array[i] < point:
            left.append(array[i])
        else:
            right.append(array[i])

    return qsort(left) + [point] + qsort(right)

# def new_qsort(array: list, start: int, end: int) -> list:
#     if end - start <= 1:
#         return array
#     s = start
#     for i in range(start + 1, end):
#         if array[i] <= array[s]:
#             array = array[:start] + [array[i]] + array [start:i] + array[i+1:]
#             s += 1       
#     array = new_qsort(array, start, s)
#     array = new_qsort(array, s+1, end)

#     return array

def combsort(array: list) -> list:
    factor = 1/(1-pow(math.e, -((1+math.sqrt(5))/2)))
    step = len(array)-1
    disorder = False
    while step > 1 or disorder:
        disorder = False
        for i in range(len(array)-step):
            if array[i] > array[i+step]:
                array[i], array[i+step] = array[i+step], array[i]
                disorder = True
        if step != 1: 
            step = int(step // factor)
    
    return array