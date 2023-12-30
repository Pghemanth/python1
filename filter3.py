def main(a):
    if a%2!=0:
        return True
    else:
        return False
def square(b):
    return b**2
a=map(square,filter(main,range(1,100)))                        
print(list(a))       