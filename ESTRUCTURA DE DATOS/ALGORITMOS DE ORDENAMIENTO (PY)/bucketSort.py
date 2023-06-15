def bucketSort(arr):
    bucket = []
    for i in range(len(arr)):
        bucket.append(i)
    for j in arr:
        index = int(10*j)
        bucket[index].append(j)
    for k in range(len(arr)):
        bucket[k] = sorted(bucket[k])

    a = 0
    for b in range(len(arr)):
        for c in range(len(bucket[b])):
            arr[a] = bucket[b][c]
            a += 1

    return arr

arr1 = [0.42,0.32,0.23,0.52,0.25,0.47,0.51]
resu = bucketSort(arr1)
print (resu)
