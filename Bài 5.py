a,b,c=map(float,input().split())
d=b**2-4*a*c
if d<0:
    print("Vo nghiem")
elif d==0:
    print(-b/(2*a))
else:
    print(f"{(-b-d**0.5)/2*a}, {(-b+d**0.5)/2*a}")