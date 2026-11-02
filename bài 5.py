ch = input("Nhập vào một chữ cái: ")
if ch=="A":
    print("Trường hợp đặc biêt")
else:
    prev_ch = chr(ord(ch) - 1) 
    print(f"Ký tự xếp trước '{ch}' là: '{prev_ch.lower()}'")