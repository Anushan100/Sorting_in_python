num=[9,8,7,6,5,4,3,2,1] #creating a list
def bubblesort(num):
    for i in range(len(num)-1,0,-1): 
        for j in range(i):  
            if num[j]>num[j+1]:
                temp=num[j]  #swaping an element
                num[j]=num[j+1]
                num[j+1]=temp
    print(num)
        
bubblesort(num)