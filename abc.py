a='ABCDEFGIJKABC'
i=1
out=[]
temp=a[0]
while i<len(a):
    if ord(a[i])==ord(a[i-1])+1:
        temp+=a[i]
    else:
        out+=[temp]
        temp=a[i]
    i+=1   
print(out)         