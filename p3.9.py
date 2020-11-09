def count(x):
    c=0
    for i in range(1,x+1):
        for j in range(2,i):
            if(i%j==0):
                break
            else:
                c+=1
    return c
n=int(input("Enter a number"))
print(count(n))
