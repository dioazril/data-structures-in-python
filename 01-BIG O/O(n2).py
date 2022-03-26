def items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


items(10)  # Big O = n * n = O(n2)


def items2(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)


items2(10)  # Big O = n * n * n = O(n3) akan tetapi disederhanakan menjadi O(n2)
