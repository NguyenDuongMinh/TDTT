a,b,c,d=map(int,input().split())
if a==0 and b==0 and c==0 and d==0:
    print("Yes")
elif b/a!=0 and c==0 and d==0:
    print("No")
elif a!=0 and b*(b/a)==c and c*(b/a)==d:
    print("Yes")
else:
    print("No")