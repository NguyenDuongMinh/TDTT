a=input("Nhập một kí tự từ bàn phím ")
if a.isalpha():
    print(f"{a} là chữ")
elif a.isdigit():
    print(f"{a} là số")
else:
    print("a không phải số và không phải chữ")