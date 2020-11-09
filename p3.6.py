n4=int(input("Enter a number"))
n2=int(input("Enter a number"))
n3=int(input("Enter a number"))
sum=n4+n2+n3
if(sum<=21):
    print(sum)
else:
    if(n4==11 or n2==11 or n3==11):
        sum=sum-10
    if(sum>21):
        print(sum)
