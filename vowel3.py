a=input('enter the character:-')
i=0
count=0
while i<len(a):
    if a[i] in "aeiouAEIOU":
        count+=1
    else:
            
    i+=1
print(count)