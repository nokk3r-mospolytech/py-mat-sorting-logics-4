def nextPermutation(arr):
    minInd = 0
    maxInd = len(arr)-1
    array = []
    for i in range(len(arr)-1, 0, -1):
        if arr[i] > arr[i - 1]:
            minInd = i - 1
            break
    print(arr[minInd], minInd)
    for i in range(minInd + 1, len(arr), +1):
        if arr[i] < arr[minInd]:
            maxInd = i
            break
    if maxInd == 0:
        maxInd = len(arr)-1
    print(arr[maxInd], maxInd)

    arr[minInd], arr[maxInd] = arr[maxInd], arr[minInd]

    for i in range(minInd+1, maxInd+1):
        array.append(arr[i])
    print(array)
    array.reverse()
    print(array)
    j = 0
    for i in range(minInd + 1, maxInd + 1):
        print(array[j])
        arr[i] = array[j]
        j = j + 1


arr = [3, 2, 1]
nextPermutation(arr)
print(arr)
