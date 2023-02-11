def maximum_pairwise(array):
    max_num_1 = 0 
    max_num_2 = 0
    first_max_index = 0 
    
    for x in range(len(array)):
        if array[x] > max_num_1:
            max_num_1 = array[x] 
            first_max_index = array.index(array[x])
    
    for y in range(len(array)):
        if y == first_max_index:
            continue
        elif array[y] > max_num_2:
            max_num_2 = array[y 
                              ]
    return (max_num_1*max_num_2)
              

