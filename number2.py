#count digits
a=input('enter the string:-')
count=0
for i in a:
    if '0'<=i<='9':
        count+=1
print(count)
