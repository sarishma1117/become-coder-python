n=int(input())
temp=0
s=c=0
while n:
    b=n//10
    c=c+1
c=k=c-1
n=temp
p=n//(10**c)
q=n%10
while n:
    r=n//(10**c)
    n=n%(10**C)
    if c==k:
        r=q
    elif c==0:
        r=p
    s=s*10+r
    c-=1
print(s)

