def selectionsort(arr,size):
    for i in range(size):
        min_ind=i
        for j in range(size):
            if(arr[j]<arr[min_ind]):
                min_ind=j
                temp=arr[i]
                arr[i]=arr[min_ind]
                arr[min_ind]=temp

array = [5,4,1,8,3,10,12,0,25,-1,45,18]
l=len(array)
selectionsort(array,l)
print(array)