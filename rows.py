rows=int(input('enter number of rows:-'))
col =int(input('enter number of cols:-'))
for i in range(rows):
    for j in range(col):
        if i == 0 or i == rows-1:
            if j == 0 or j == col-1:
                print('@',end=' ')
            else:
                print('*',end=' ')    
        else:
            if j==i or rows-i-1==j:
                print('@',end=' ')
            else:
                print('*',end=' ')    
    print()    