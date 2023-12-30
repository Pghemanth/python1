a=10
def outer():
    b=20
    print(a)
    print(b)
    def inner():
        c=30
        print(c) 
    inner()    
outer()


