def table(t):
    for row in t:
        print('+'+(("-"*3+'+')*len(row)))
        print("|",end = '')
        print(*[str(cell).center(3) for cell in row], sep = '|', end = '|\n')
    print('+'+(("-"*3+'+')*len(t[-1])))
def jadval_tabiei(n):
    t = []
    for i in range(1, n + 1):
        row = [max(i,j) * 2 - 1 for j in range(1, n + 1)]
        t.append(row)
    return t

table(jadval_tabiei(int(input())))
