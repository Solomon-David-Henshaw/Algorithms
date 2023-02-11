import random


# Define Function
def BinarySearch(array,target):
    
    ''' Create Pointers for the first element in 
    the array and the last elent of the array'''

    low = 0
    high = len(array)-1
    '''Implement a Loop That runs until the 
    pointer from the left of the array is 
    greater than ther right pointer'''
    while high >= low:        
        '''Divide the two pointyers to get 
        the middle value in the array '''
        mid = (low+high)//2

        '''Compare if the element in the middle of the
        array is the value were searching for ?'''
        if array[mid] == target:
            return "Found"
        elif array[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return "Not Found"



random_array = [ x for x in range(random.randint(1,100))]
random_arguments =  [ ] 

for x in range(random.randint(1,100)):
    b = random.randint(1,100)
    random_arguments.append(b)


for x in random_arguments:

    print(BinarySearch(random_array,x), x)

