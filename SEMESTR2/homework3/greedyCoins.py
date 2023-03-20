def summator1(list_: list) -> int:
    summ = 0
    for l_ in list_:
        summ += l_[0] * l_[1]
    return summ    

def greedyCoins(change_start: int, Ms_and_Ss: list) -> list:
    change = change_start
    Ms_and_Ss.sort(key = lambda x: x[1], reverse = True)
    change_list = [[0, 0] for i in range(len(Ms_and_Ss))]

    for MS_ind in range(len(Ms_and_Ss)):
        if change > 0:
            this_S = True
        else:
            break
        while this_S:
            if Ms_and_Ss[MS_ind][1] > change or Ms_and_Ss[MS_ind][0] == 0:
                this_S = False
            else:                
                Ms_and_Ss[MS_ind][0] -= 1
                change -= Ms_and_Ss[MS_ind][1]
                change_list[MS_ind][0] += 1
                change_list[MS_ind][1] = Ms_and_Ss[MS_ind][1]
    
    if summator1(change_list) == change_start:
        return change_list
    else:
        return []