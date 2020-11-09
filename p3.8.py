def order(n):
    for i in range(0,len(n)-2):
        if (n[i]==0 and n[i+1]==0 and n[i+2]==7):
            return True
        else:
            return False
print(order([1,2,4,0,0,7,8,9]))        
