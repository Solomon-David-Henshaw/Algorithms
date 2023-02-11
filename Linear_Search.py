def Linear_Search(array,target):
    for value in array:
        if value == target:
            return "Value is present in Array"
        return "Value Not Present in Array"


print(Linear_Search([value for value in range(20)], 24))