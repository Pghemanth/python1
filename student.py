percentage=float(input('enter your percentag:'))
if 90 <= percentage <= 100:
    print('A+')
elif 80 < percentage <= 89:
    print('A') 
elif 70 <= percentage <= 79:
    print('B')       
elif 60 <= percentage <= 69:
    print('c')
elif 35 <= percentage <= 59:
    print('pass')        
elif 0 < percentage <=34:
    print('file')
else:
    print('invaid marks')       
    