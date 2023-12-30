def add_int(var,i=0):
    if len(var)-1==i:
        return var[i]
    return var[i] + add_int(var,i+1)        
a=[1,2,3,4,5,6,7]
out=add_int(a)
print(out)