def carma(n, ch = None):
    if n in {0,1,2,3,4,5,6,7,8,9,11,22}:
        assert n != 0 , "please enter non 0"
        return n, ch
    if n in {19,16,14,13}:
        ch = n
    return carma(sum([int(x) for x in str(n)]), ch)
name = input("Input your name: ").split()
year, month, day = map(int, input("input your birthday: ").split("/"))
lifePath = carma(carma(year)[0] + carma(month)[0] + carma(day)[0])
soulUrge = 0
trans = {'A': 1, 'U':3, 'E':5, 'O':6, 'I':9}
for part in name:
    soulUrge += carma(sum([trans[l] for l in part.upper() if l in trans.keys()]))[0]

print("the soulUrge number: {0} | the life path number: {2} \nthe carmas:{1},{3}".format(*carma(soulUrge), *lifePath))
#<ToDo> extinquish the soul urge number and the life path carmas