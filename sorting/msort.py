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


def mergesort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        mergesort(left)
        mergesort(right)

        n = 0
        m = 0
        k = 0

        while n < len(left) and m < len(right):
            if left[n] < right[m]:
                array[k] = left[n]
                n += 1
            else:
                array[k] = right[m]
                m += 1
            k += 1

        while n < len(left):
            array[k] = left[n]
            n += 1
            k += 1

        while m < len(right):
            array[k] = right[m]
            m += 1
            k += 1


start = time.time()
mergesort(arr)
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