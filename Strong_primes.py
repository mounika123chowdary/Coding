#You are given Q queries and in each query, there are two numbers L and R. You have to calculate the number of strong primes present in the range L and R inclusive.

def soe():
    n=1000001
    a=[1]*(n+1)
    pr=[]
    u=2
    v=3
    for i in range(9,n+1,3):
            a[i]=0
    for p in range(5,n+1,2):
        if(a[p]):
            if 2*v>u+p:
                pr.append(v)
            u=v
            v=p
            for i in range(p*p,n+1,p):
                a[i]=0
    return pr 
d=soe()
n=len(d)
def ls(lo):
    l=0
    h=n-1
    while(l<=h):
        mid=(l+h)//2
        if(d[mid]>=lo):
            h=mid-1
        else:
            l=mid+1
    return l
def us(up):
    l=0
    h=n-1
    while(l<=h):
        mid=(l+h)//2
        if(d[mid]<=up):
            l=mid+1
        else:
            h=mid-1
    return h
for _ in range(int(input())):
    l,r=map(int,input().split())
    count=0
    count=us(r)-ls(l)+1
    print(count)
