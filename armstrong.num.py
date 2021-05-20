def arm(num):
    n=num
    s=0
    while n>0:
        r=n%10
        s+=(r*r*r)
        n=n//10
    if n==s:
        print("armstrong")
    else:
        print("armstrong")

num=int(input("enter a number"))
arm(num)
    
