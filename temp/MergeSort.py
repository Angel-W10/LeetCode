def MergeSort(arr):

    print("Unsorted: ")
    print(arr)

    # break condition
    if len(arr)>1:

        middle = len(arr)//2

        L = arr[:middle]
        R = arr[middle:]

        MergeSort(L)
        MergeSort(R)

        i=j=k=0

        while (i<len(L) and j < len(R)):
            if(L[i]<=R[j]):
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        
        while(i<len(L)):
            arr[k] = L[i]
            i+=1
            k+=1

        while(j<len(R)):
            arr[k] = R[j]
            j+=1
            k+=1

    print("Sorted: ")
    print(arr)




if __name__ == "__main__":
    arr = [7, 3, 2, 4, 6, 5, 1]
    MergeSort(arr)






