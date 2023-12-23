password=input('enter the password:')
validate={
    'upper':False,
    'lower':False,
    'char':False,
    'number':False,
    'space':False
    }
if len(password)>=8:
    for char in password:
        if 'A'<= char <='Z':
            validate['upper']=True
        elif 'a'<= char <='z':
            validate['lower']=True
        elif '0'<= char <='9':
            validate['number']=True
        elif char !=' ':
            validate['char']=True 
        elif char ==' ':
            validate['space']=True 
            break              
    if (
        validate['upper'] and 
        validate['lower'] and 
        validate['char']and 
        validata['number'] and
        not validate['space']):
        print('password validate')
    else:
        print('password is invalidate')
else:
    print('password is invalidate')        
