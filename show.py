setes=int(input('select your seats:-'))
option=int(input('plsace select 1-->daimond class \n 2-->gold class \n 3-->silver class:-'))
match option:
    case 1:
        print("daimond class")
        amt=setes*200
    case 2:
        print("gold class")
        amt=setes*150
    case 3:
        print("silver class")
        amt=setes*100
    case _:
        print('invaild option')
        amt = None  
print(amt)    