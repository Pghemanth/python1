import re
st ='+91-7815939981'

#data = re.findall('\d',st)
#data = re.findall('\d[24680]',st)
#data = re.findall('[A-Z]{5}\d{4}[A-Z]',st)
#data = re.findall('AP[0-3]\d[A-Z]{2}\d{4}',st)
data =re.findall('\+91-[6789]{1}[0-9]{9}',st)
print(data)
