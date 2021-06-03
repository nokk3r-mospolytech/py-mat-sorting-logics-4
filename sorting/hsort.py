import errno
import os
import time

size = "1000000"


file = open("arr_"+size+".txt", "r")
length = int(file.readline())
file.readline()
arr = [int(x) for x in file.readline().split(" ")]
file.close()


def heapify(array, heap_length, root):
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    if left < heap_length and array[left] > array[largest]:
        largest = left

    if right < heap_length and array[right] > array[largest]:
        largest = right

    if largest != root:
        array[root], array[largest] = array[largest], array[root]

        heapify(array, heap_length, largest)


def heapsort(array):
    arr_length = len(array)

    for j in range(arr_length // 2, -1, -1):
        heapify(array, arr_length, j)

    for j in range(arr_length - 1, 0, -1):
        array[0], array[j] = array[j], array[0]

        heapify(array, j, 0)


start = time.time()
heapsort(arr)
finish = time.time()


filename = "./results/hsort_{}.txt".format(size)
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
