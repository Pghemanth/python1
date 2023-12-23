a=[1,9,11,23,78,4]
i=1
if len(a)%2==0:
    out=0
    for i in a:
        out+=i 
    else:
        for i in a:
            out*=i 
print(out)
