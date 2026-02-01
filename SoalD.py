import bisect
n,t=map(int,input().split())
a=list(map(int,input().split()))
i=bisect.bisect_left(a,t)
r=[]
if i>0:r.append(a[i-1])
if i<n:r.append(a[i])
print(min(r,key=lambda x:(abs(x-t),x)))