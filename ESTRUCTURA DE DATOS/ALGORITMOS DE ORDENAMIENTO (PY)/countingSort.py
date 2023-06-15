def countingSort(arr):
    maxElement=max(arr)
    count = [0]*(maxElement+1)
    print(str(count)+"prueba 0")

    for i in arr:
        count[i]+=1
        print(str(count)+" prueba 1")

    for i in range(1, len(count)):
        count[i] += count[i-1]
        print(str(count)+" prueba 2")

    result =  [0] * len(arr)
    print(str(result)+" prueba 3")

    for i in arr:
        result[count[i]-1]  = i
        count[i] -= 1
        print(str(count)+" prueba 4")
    return result

arr = [8,5,2,6,9,3,1,4,0,7]
print(arr)
print(countingSort(arr))

