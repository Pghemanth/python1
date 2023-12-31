class Employee:
    compeny = "Tcs"
    ceo     = 'Elon musk'
    
    def insert(self,name,age,sal,eid):
        self.name = name
        self.age  = age
        self.sal  = sal
        self.eid  = eid


hemanth = Employee()
bhanu = Employee()  
dhoni= Employee()

Employee.insert(hemanth,'p g hemanth',21,50000,6453)
Employee.insert(bhanu,'bhanu',21,54000,6450)
dhoni.insert('dhoni',40,54999,4656)
