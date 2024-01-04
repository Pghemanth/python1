import re
st = 'hemanthPg2003@gmail.com'
data =re.findall('[a-zA-Z]+\w*@gmail.com',st)
print(data)
