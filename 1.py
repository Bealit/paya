def carma(n, ch = None):
    if n in {1,2,3,4,5,6,7,8,9,11,22}:
        return n, ch
    if n in {19,16,14,13}:
        ch = n
    return carma(sum([int(x) for x in str(n)]), ch)

inp = int(input("Input your number: "))
print("the base number: {} \nthe carmaiac numbers: {}".format(*carma(inp)))
