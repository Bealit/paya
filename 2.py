def carma(n, ch = []):
    if n in {1,2,3,4,5,6,7,8,9,11,22}:
        return n, ch
    if n in {19,16,14,13}:
        ch.append(n)
    return carma(sum([int(x) for x in str(n)]), ch)
name = input("Input your name: ").split()
year, month, day = map(int, input("input your birthday: ").split("/"))
Sum = carma(year)[0] + carma(month)[0] + carma(day)[0]
hartwish = 0
trans = {'A': 1, 'U':3, 'E':5, 'O':6, 'I':9}
for part in name:
    hartwish += carma(sum([trans[l] for l in part.upper() if l in trans.keys()]))[0]
print("the hartwish number: {} the life way number: {} \nthe carmas:{}".format(carma(hartwish)[0], *carma(Sum)))
