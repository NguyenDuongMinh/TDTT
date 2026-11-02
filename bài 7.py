a=input("Nhập một chuỗi kí tự :")
b=a.split()
c=len(a)
if c<=20:
    print("Số kí tự chưa đủ.")
else:
    print("Kí tự số 5 của chuỗi là:",b[4])
    print("Kí tự số 9 của chuôi là:",b[9])