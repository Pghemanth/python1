import re

with open(r"c:\Users\administrator.MCA\Desktop\hemant.txt.txt",'r') as file:
    data=file.read()
    data1=re.split(' ',data)
    count=0
    words=[]
    for i in data1:
        out=re.match('^a',i)

        if out:
            words+=[i]
            count+=1
    print(count)
    print(words)
