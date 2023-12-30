a=10
b=20
def sample():
    global a
    a=30
    print(a)
    print(b)
    
    print(a)

print(a)       
sample()
print(a)

