import random


def generation():
    file = open("arr_{}.txt".format(size), "w+")
    file.write("{}\n\n".format(size))
    first = True

    for i in range(int(size)):
        if first:
            file.write("{}".format(random.randint(0, int(size))))
            first = False
        else:
            file.write(" {}".format(random.randint(0, int(size))))

    file.close()


size = 10000000
generation()
