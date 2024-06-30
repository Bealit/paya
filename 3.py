def table(t):
    for row in t:
        print('+'+(("-"*17+'+')*len(row)))
        print("|",end = '')
        print(*[str(cell).center(17) for cell in row], sep = '|', end = '|\n')
    print('+'+(("-"*17+'+')*len(t[0])))
table([["Masir Zandegi",input()],["Arezoo Ghalbi",input()],["Adad Karmaei",input()]])
