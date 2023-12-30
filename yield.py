def add(a,b):
    yield a+b
    yield a-b
    yield a*b
    yield a/b
out=add(10,4)
print(type(out))
for i in out:
    print(i)

    
