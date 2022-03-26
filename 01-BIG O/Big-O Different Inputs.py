def items(a, b):
    for i in range(a):
        print(a)

    for j in range(b):
        print(b)


# Big-O = O(a) + O(b)
#       = O(a + b)
items(10, 11)


def items2(a, b):
    for i in range(a):
        for j in range(b):
            print(a, b)


# Big-O = O(a) * O(b)
#       = O(a * b)
items2(10, 11)
