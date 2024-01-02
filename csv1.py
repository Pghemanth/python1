import csv
#with open('mca.csv','w',newline='') as csvfile:
#    data.writerow(['id','name','mobil','email','location'])
#   data2=[
#        [1,'hemanth',7815939981,'hemnrhy@mail.com','rayalapet'],
#        [2,'ram',8795461235,'ram2gmail.com','palamaner'],
#        [3,'hari',987456123,'haruhh@gmail.com','marapalli']
#    ]
#    data.writerows(data2)


#with open('mca.csv','r') as csvfile:
#   for i in data:
#        print(i)


#with open('mca.csv','w',newline='') as csvfile:
#    fieldname=['id','name','mobile','email']
#    data=csv.DictWriter(csvfile,fieldname)
#    data.writeheader()
#    rows=[
#       {'id':1,'name':'hemanth','mobile':7815939981,'email':'hemanr@gmail.com'},
#      {'id':2,'name':'hari','email':'hari@gmail.com','mobile':7846595645},
#    ]
#    data.writerows(rows)

with open('mca.csv','r') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        print(row['name'])