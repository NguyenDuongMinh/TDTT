a=int(input("Nhập vào đây một năm cụ thể:"))
if a%4==0 and a%100!=0 or a%400==0:
    print("đây là năm nhuận")
else:
    print("đây không là năm nhuận")