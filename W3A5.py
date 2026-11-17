m=float(input())
n=float(input())
x=int(m/n)
if n!=0:
    if m/n>x:
        print(int(m//n)+1)
    else:
        print(int(m//n))