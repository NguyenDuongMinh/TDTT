a,b,c=map(int,input().split())
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("Tam giác đều")
    elif a==b or a==c or b==c:
        print("Tam giác cân")   
    else:
        print("Tam giác thường")
    p=(a+b+c)/2
    print(2*p)
    print((p*(p-a)*(p-b)*(p-c))**0.5)
else:
    print("Khong la ba canh cua mot tam giac")