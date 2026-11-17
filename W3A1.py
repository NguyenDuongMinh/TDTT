n=int(input())
if 100<=n<=999: 
    b=n%10
    x=n%100
    c=(x-b)//10
    d=n//100
    a=b*100+c*10+d
    print(a)
else:
    print("Khong xu li")


