def insertionsort(array):
    for i in range(1, len(array)):
        current_element = array[i]
        j = i-1
        while j >= 0 and array[j] > current_element:
            array[j+1] = array[j]
            j = j-1        
        array[j+1] = current_element
    
    return array

def bucketsort(array):
    maximum = max(array)
    length = len(array)
    interval = maximum/length
    array_nums = [[] for i in range(length)]

    for e in range(length):
        index = int(array[e]/interval)
        if index < length:
            array_nums[index].append(array[e])
        else:
            array_nums[index-1].append(array[e])

    return_arr = []

    for k in range(length):
        array_nums[k] = insertionsort(array_nums[k])
        return_arr = return_arr + array_nums[k]

    return return_arr

def heapify(array):    
    length = len(array)
    while length > 0:
        for i in range(length//2 - 1, -1, -1):
            if 2*i + 1 < length:
                l_child_i = 2*i + 1
                if array[i] < array[l_child_i]:
                    array[i], array[l_child_i] = array[l_child_i], array[i]
            if 2*i + 2 < length:
                r_child_i = 2*i + 2
                if array[i] < array[r_child_i]:
                    array[i], array[r_child_i] = array[r_child_i], array[i]
        array[0], array[length-1] = array[length-1], array[0]
        length = length - 1

    return array