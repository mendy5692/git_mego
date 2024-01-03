def sum_of_pisg(list):
    pisg = 0
    for i in range(len(list) + 1):
        if (i != 0) and (i != len(list)):
            if list[i-1] < list[i] > list[i+1]:
                pisg += 1
    return pisg

def is_pisg(list, index):
    if (index != 0) and (index != len(list)):
        if list[index - 1] < list[index] > list[index + 1]:
            return True
        else:
            return False
    else:
        return False


print(sum_of_pisg([5,10,7,8,9,3]))
print(is_pisg([5,10,7,8,9,3], 0))
print(is_pisg([5,10,7,8,9,3], 0))