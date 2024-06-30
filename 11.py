mapping = {1:7,2:8,3:9,4:4,5:5,6:6,7:1,8:2,9:3}
def solve(e):
    if "+" in e:
        a, _, b = e.partition("+")
        return solve(a) + solve(b)
    elif "-" in e:
        a, _, b = e.partition("-")
        return solve(a) - solve(b)
    elif "*" in e:
        a, _, b = e.partition("*")
        return solve(a) * solve(b)
    elif "/" in e:
        a, _, b = e.partition("/")
        return solve(a) / solve(b)
    else:
        return mapping[int(e)]
print(solve(input()))
