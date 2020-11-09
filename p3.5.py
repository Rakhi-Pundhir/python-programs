def check(x):
    for i in range(len(x)-1):
        if x[i:i+2]==[3,3]:
            return True
    return False    
print(check([1,3,3]))
print(check([1,3,1,3]))
print(check([3,1,3]))
