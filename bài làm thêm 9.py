n=int(input("Nhập một số bất kì từ 1 đến 9 vào bàn phím:"))
def day(n):
    match n:
        case 0: return "Không"
        case 1: return "Một"
        case 2: return "Hai"
        case 3: return "Ba"
        case 4: return "Bốn"
        case 5: return "Năm"
        case 6: return "Sáu"
        case 7: return "Bảy"
        case 8: return "Tám"
        case 9: return "Chín"
print(day(n))