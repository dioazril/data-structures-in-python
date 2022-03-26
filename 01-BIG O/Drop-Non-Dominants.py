def items2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)


# Big O = O(n2) + O(n)
#      = O(n2 +n)
# Kita akan menghapus(drop-dominants) n hasilnya = O(n2)

items2(10)
