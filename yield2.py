a=[(1,2),[4,5,6],(11,12,13),[9,8,7,6]]
def main(a):
    for i in a:
        if len(i)%2==0:
            yield (i[0]+i[-1])/2
        else:
            yield i[len(i)//2] 
out=main(a)
print(list(out))               