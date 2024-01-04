import re
st = 'the 52  78 92 38 654 7654 data 41 7 3 4 is 04/01/2024'

#data = re.findall('\d',st)
#data = re.findall('\d[24680]',st)
data = re.findall('\d+',st)
print(data)
