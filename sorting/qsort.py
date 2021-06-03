import errno
import os
import time

size = "10"

file = open("arr_" + size + ".txt", "r")
length = int(file.readline())
file.readline()
arr = [int(x) for x in file.readline().split(" ")]
file.close()


def quicksort(arr, begin, end):
    if end - begin <= 1:
        return

    pivot = partition(arr, begin, end)
    quicksort(arr, begin, pivot), quicksort(arr, pivot + 1, end)


def partition(arr, begin, end):
    arr[end - 1], arr[(begin + end - 1) // 2], pindex = \
        arr[(begin + end - 1) // 2], arr[end - 1], begin

    for j in range(begin, end):
        if arr[j] < arr[end - 1]:
            arr[pindex], arr[j], pindex = \
                arr[j], arr[pindex], pindex + 1

    arr[end - 1], arr[pindex] = \
        arr[pindex], arr[end - 1]
    return pindex


start = time.time()
quicksort(arr, 0, len(arr))
finish = time.time()

# creating result file
filename = "./results/qsort_{}.txt".format(size)
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise

result = open(filename, "w+")
result.write("{}\n\n{}\n\n".format(len(arr), finish - start))

for i in range(len(arr)):
    result.write("{} ".format(arr[i]))
result.close()
