a=[1,2,3,4,55,66]
def main(a):
    for i in a:
        if type(a) in [int,float,complex,complex]:
            return True
        else:
            return False
out=filter(main(a))
print(list(out))            