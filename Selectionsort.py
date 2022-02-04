num=[9,8,7,6,5,4,3,2,1]
def selectionsort(num):
    for i in range(len(num)):
        min_value=i  
        for j in range(i+1,len(num)):
            if num[j]<num[min_value]:
                min_value=j

        temp=num[i]             #swap an element
        num[i]=num[min_value]
        num[min_value]=temp
    print(num)
selectionsort(num)



















