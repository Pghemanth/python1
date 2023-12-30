def add(var,i=0):
    if len(var)-1==i:
        if var[i]%2==0:
            return var[i]
        else:
            return 0
    if var[i]%2==0:
        return var[i]+add(var,i+1)
    else:
        return add(var,i+1) 
a=[6,7,9,12,13]
out=add(a)
print(out)
