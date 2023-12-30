def vowel(a):
    out=[]
    i=0
    for i in range(0,len(a)):
        if a[i] in "aeiouAEIOU":
            out=out+[i]
        i=i+1
    print(out)                
vowel('happy new year')    
