def recursion(n):
    if n == 1:
        return 1
    return n * recursion(n-1)

print(recursion(60))