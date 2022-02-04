


def quicksort(num):
    length=len(num)
    if len(num)<=1:
        return num
    else:
        pivot=num.pop()   #taking last element in a list

    num_lower=[]     #creating list to add an element which is lower
    num_greater=[]   #creating list to add an element which is  greater

    for i in num:
        if i>pivot:
            num_greater.append(i) # will add element to num_greater
        else:
            num_lower.append(i) # will add element to num_lower

    return quicksort(num_lower) + [pivot] + quicksort(num_greater) #recursion
print(quicksort([9,8,7,6,5,4,3,2,1]))































