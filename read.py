import re
with open(r"c:\Users\administrator.MCA\Desktop\hemant.txt.txt",'r') as file:
    data=file.read()
    out=re.findall('a[a-z]* ',data)
    print(len(out))

