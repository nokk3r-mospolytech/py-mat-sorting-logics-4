import errno
import os
import sys
import time


size = "10000"

file = open("arr_"+size+".txt", "r")
length = int(file.readline())
file.readline()
arr = [int(x) for x in file.readline().split(" ")]
file.close()

start = time.time()

for i in range(len(arr)):
    min_i = i
    for j in range(i + 1, len(arr)):
        if arr[min_i] > arr[j]:
            min_i = j
    arr[i], arr[min_i] = arr[min_i], arr[i]

finish = time.time()

filename = "./results/selection_{}.txt".format(size)
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
