a,b,c,d,m,n=map(int,input().split())
if a/c==b/d!=m/n:
    print("Phương trình vô nghiệm")
elif a/c==b/d==m/n:
    print("Phương trình vô số nghiệm")
else:
    y=((n*a/c)-m)/((a*d/c)-b)
    x=(m-b*y)/a
    print(x,y)