def per(num):
    n=num
    s=0
    i=1
    while i<n:
        if n%i==0:
            s=s+i
        i=i+1
    if n==s:
        print("perfect number")
    else:
        print("not a perfect number")

num=int(input("enter a number"))
per(num)
