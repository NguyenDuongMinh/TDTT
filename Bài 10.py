a,b,r=map(float,input().split())
x,y=map(float,input().split())
if (x-a)**2+(y-b)**2==r**2:
    print("điểm thuộc đường tròn")
else:
    print("điểm không thuộc đường tròn")