a=float(input("Nhập một số thực:"))
b=float(input("Nhập một số thực:"))
c=float(input("Nhập một số thực:"))
if a<b+c and b<a+c and c<a+b:
    p=(a+b+c)/2
    d=(p*(p-a)*(p-b)*(p-c))**0.5
    e=f"{d:.1f}"
    print("Diện tích tam giác là",e)
else:
    print("Khong phai 3 canh cua tam giac")