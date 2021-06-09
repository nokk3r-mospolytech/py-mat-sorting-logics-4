import errno
import os
import sys
import time

size = "1000000"

file = open("arr_"+size+".txt", "r")
length = int(file.readline())
file.readline()
arr = [int(x) for x in file.readline().split(" ")]
file.close()


def merge_sort(array, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(array, start, mid)
        merge_sort(array, mid, end)
        merge_list(array, start, mid, end)


def merge_list(array, start, mid, end):
    left = array[start:mid]
    right = array[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            array[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            array[k] = right[j]
            j = j + 1
            k = k + 1


start = time.time()
merge_sort(arr)
finish = time.time()

filename = "./results/msort_{}.txt".format(size)
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