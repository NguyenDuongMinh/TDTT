a=input("Ten chu ho la:")
b=int(input("Chỉ số tháng trước là:"))
c=int(input("Chỉ số tháng này là:"))
d=c-b
print("Ten chu ho la:",a)
if d<0:
    print("Dữ liệu đầu vào không hợp lệ")
elif 0<d<=50:
    e=d*1984
    print("Tiền phải trả là:",int(e*1.08))
elif 50<d<=100:
    f=50*1.984+(d-50)*2050
    print("Tiền phải trả là:",int(f*1.08))
elif 100<d<=200: 
    g=50*1984+50*2050+(d-100)*2380
    print("Tiền phải trả là:",int(g*1.08))
elif 200<d<=300:
    h=50*1984+50*2050+100*2380+(d-200)*2998
    print("Tiền phải trả là:",int(h*1.08))
elif 300<d<=400:
    i=50*1984+50*2050+100*2380+100*2998+(d-300)*3350
    print("Tiền phải trả là:",int(i*1.08))
else:
    j=50*1984+50*2050+100*2380+100*2998+100*3350+(d-400)*3460
    print("Tiền phải trả là:",int(j*1.08))

