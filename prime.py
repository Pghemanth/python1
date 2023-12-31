num=int(input('enter the number:-'))
i=1
count=0
while i<=num:
    if num%i==0:
        count+=1
    i+=1
if count==2:
    print('it is a prime number')
else:
    print('it is not a prime number')
             

