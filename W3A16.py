n=float(input())
a=int(n)
if n==a:
    print(int(n),end=" ")
    print(int(n),end=" ")
    print(int(n))
else:
    b=0    
    if n-int(n)>=0.5:
        b=int(n)+1
        print(b)
    else:
        b=int(n)
        print(int(n))
    print(int(n)+1,int(n),b)