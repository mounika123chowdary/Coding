#You are given two numbers L and R. You are required to find the total number of lucky numbers present in between L and R(inclusive).
def soe(r):
    m=r+1
    a=[1]*m
    l=[]
    l.append(1)
    for i in range(2,m):
        if(a[i]):
            l.append(i)
            for j in range(i*i,m,i*i):
                a[j]=0
    return l
lo=[]
up=[]
t=int(input())
for _ in range(t):
    l,r=map(int,input().split())
    lo.append(l)
    up.append(r)
f=max(up)
b=soe(f)
n=len(b)
def countu(u):
    f=0
    h=n-1
    while(f<=h):
        mid=(f+h)//2
        if(b[mid]<=u):
            f=mid+1
        else:
            h=mid-1
    return h
def countl(l):
    f=0
    h=n-1
    while(f<=h):
        mid=(f+h)//2
        if(b[mid]>=l):
            h=mid-1
        else:
            f=mid+1
    return f
for i in range(t):
    c=countu(up[i])-countl(lo[i])+1
    print(c)
