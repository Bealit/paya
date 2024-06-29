def jadval_tabiei(n):
    for i in range(1, n + 1):
        row = [max(i,j) * 2 - 1 for j in range(1, n + 1)]
        print(*row)

n = int(input())
jadval_tabiei(n)
