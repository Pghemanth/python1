import csv
with open('mca.csv','w',newline='') as csvfile:
    data=csv.writer(csvfile)
    data.writerow(['id','name','mobil','email','location'])
    data2=[
        [1,'hemanth',7815939981,'hemnrhy@mail.com','rayalapet'],
        [2,'ram',8795461235,'ram2gmail.com','palamaner'],
        [3,'hari',987456123,'haruhh@gmail.com','marapalli']
    ]
    data.writerows(data2)