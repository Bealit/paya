def chose(n,k):
    if k == 0 or k == n:
        return 1
    return chose(n-1,k)+chose(n-1,k-1)
print(chose(int(input()),int(input())))
