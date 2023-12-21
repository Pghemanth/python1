num1=eval(input('enter a number:'))
num2=eval(input('enter a number:'))
num3=eval(input('enter a number:'))
if num1>num2 and num1>num3:
    if num2>num3:
        print(num2,'is second greatest')
    else:
        print(num3,'is second greatest')
elif num2>num3:
    if num1>num3:
        print(num1,'is scecond greatest') 
    else:print(num3,'is second greatest') 
else:
    if num1>num2:
        print(num1, 'is second greatest')
    else:
        print(num2,'is second greatest')                  
                                