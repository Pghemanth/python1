def vowel(a):
    for i in range(len(a)):
        if a[i] in 'aeiouAEIOU':
            yield a[i] 
            yield i
out=vowel('god father')
res=''
for i in out:
    res+=str(i)
print(res)           
