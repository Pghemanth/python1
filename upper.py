def upper(a):
    if  'A'<= a <='Z':
        return True
    else:
        return False
out=filter(upper,'ASfgrtWE')
print(list(out))            