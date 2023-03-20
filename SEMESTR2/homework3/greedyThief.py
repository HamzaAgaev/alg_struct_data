def greedyThief(exponates: list, N: int, M: int, K: int) -> list:
    exponates.sort(key = lambda x: x[0], reverse = True) # lambda x: x[0] / x[1]
    
    sneaked = []
    ex_ind = 0
    while M > 0:
        K_copy = K
        sneaked_now = []
        while ex_ind < len(exponates) and K_copy - exponates[ex_ind][1] > 0 and N > 0:
            sneaked_now.append(exponates[ex_ind])
            K_copy -= exponates[ex_ind][1]
            N -= 1
            ex_ind += 1
        sneaked.append(sneaked_now)
        M -= 1
    
    return sneaked