def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        mergeSort(left_half)
        mergeSort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i]<right_half[j]:
                arr[k] = left_half[i]
                i +=1
            else:
                arr[k] = right_half
                j+=1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i+=1
            k+=1
        while j< len(right_half):
            arr[k] = right_half[j]
            j+=1
            k+=1
    return arr 

arr1 = [8,5,2,6,9,3,1,4,0,7]
print (mergeSort(arr1))