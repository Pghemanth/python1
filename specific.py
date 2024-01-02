try:
    a=2+'2'
    print(a)
except TypeError:
    print('error handled') 
finally:
    print('exception handling')

def sum(a,b):
    return a+b
print(sum(2,5))               