try:
    a=dict('34')
    print(a)
except TypeError:
    print('error handled') 
except ValueError:
    print('can not type cast sringe to dict')    
finally:
    print('exception handling')