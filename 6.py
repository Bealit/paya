a,b,c = map(int, input().split())
discriminant = b*b - 4*a*c;
if discriminant < 0:
    print("always positive")
    quit()
x1 = (-b + discriminant ** 0.5) / (2*a);
x2 = (-b - discriminant ** 0.5) / (2*a);
if x1 > x2:
    x1, x2 = x2,x1
x = x1-1
if a*x**2+b*x+c > 0:
    print(f"from -infinity to {x1} is positive")
else:
    print(f"from -infinity to {x1} is negetive")
x = (x1+x2)/2
if a*x**2+b*x+c > 0:
    print(f"from {x1} to {x2} is positive")
else:
    print(f"from {x1} to {x2} is negetive")
x = x2+1
if a*x**2+b*x+c > 0:
    print(f"from {x1} to infinity is positive")
else:
    print(f"from {x1} to infinity is negetive")
