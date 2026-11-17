x=int(input())
a=x//3600
b=x%3600
c=b//60
d=b%60
if a>0:
    if c>0 and d==0:
        print(f"{a} giờ {c} phút")
    elif c==0 and d>0:
        print(f"{a} giờ {d} giây")
    elif c>0 and d>0:
        print(f"{a} giờ {c} phút {d} giây")
    else:
        print(f"{a} giờ")
else:
    if c>0 and d==0:
        print(f"{c} phút")
    elif c==0 and d>0:
        print(f"{d} giây")
    elif c>0 and d>0:
        print(f"{c} phút {d} giây")
    else:
        print("")

