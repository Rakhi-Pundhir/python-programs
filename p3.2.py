def check():
    n1=int(input("Enter a number"))
    n2=int(input("Enter a number"))
    if(n1%2==0 and n2%2==0):
        return n2 if (n1>n2) else n1
    else:
        return n1 if (n1>n2) else n2
print(check())
