n=int(input())
e=[]
for _ in range(n):a,b=map(int,input().split());e+=[(a,1),(b,-1)]
e.sort()
c=m=0
for _,d in e:c+=d;m=max(m,c)
print(m)
