X = list(map(int,input().split(',' )))
i = int(input())
#Y = list(map(int,input().split(', ')))
class var:
    def __init__(self, c, e):
        self.c = c
        self.e = e
    def __str__(self):
        if self.e == 0:
            return str(self.c)
        return  str(self.c)+'x^'+str(self.e)


def multiply(a,b):
    r = []
    for i in a:
        for j in b:
            r.append(var(i.c*j.c, i.e+j.e))
    return r
def add(a,b):
    for i in range(len(a)):
        if a[i].e == b.e:
            a[i].c += b.c
            return None
    a.append(b)

#finding dinominator
d = 1
for j in range(len(X)):
    if j == i:
        continue    
    d *= X[i]-X[j]

#finding numerator
f = [var(1,1),var(-X[0],0)]
for j in range(1,len(X)):
    f = multiply(f,[var(1,1),var(-X[j],0)])
#simplify
simp = [f[0]]
for j in range(1,len(f)):
    add(simp,f[j])
#apply denominator
for x in range(len(simp)):
    simp[x].c /= d

#print
print(*simp)

