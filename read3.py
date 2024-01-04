import re

with open(r"c:\Users\administrator.MCA\Desktop\hemant.txt.txt",'r+') as file:
    data= file.read()
    data1=re.sub('a','@',data)
    file.write(data1)