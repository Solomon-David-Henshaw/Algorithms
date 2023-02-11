def Selection_Sort(array): 
    
    '''Create Pointers for two values to caompare'''
    First_Value = 0
    Second_Value = 1
    print(array, "initization")

    '''Loop through compare and reassign values'''
    for first in range(len(array)-1):
        for second in range(first+1, len(array)):
            print(array[first], array[second],array, "Before Sorting")

            if array[first] > array[second]:
                array[first],array[second] = array[second],array[first]
                print(array[first], array[second],array, "After Comparing and sorting")

            else:
                continue
    print(array)
Selection_Sort([2,4,9,5,3,6])