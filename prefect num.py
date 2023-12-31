a=int(input('enter the number:-'))
out=0
for i in range(1,a):
    if a%i==0:
        out=out+i
if out==a:
    print('perfect number')
else:
    print('not perfact number')
