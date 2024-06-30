
X = list(map(int,input().split(',' )))
Y = list(map(int,input().split(',')))
ans = []
for i in range(len(Y)):
    d = 1
    n = ""
    for j in range(len(X)):
        if j == i:
            continue    
        d *= X[i]-X[j]
        n += f"(x - {X[j]})"
    ans.append(str(Y[i])+ str(n) + "/" + str(d))
print("+".join(ans))