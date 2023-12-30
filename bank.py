class Sbi:
    branch ='palamaner'
    ifsc   ='sbi00023'
    manager='charan'
    location='mtca'

    def __init__(self,name,mob,acc,pan,bal):
        self.name=name
        self.mobile=mob
        self.account=acc
        self.pan=panc 
        self.balnce=bal

    def credit(self,amt):
        self.blance+=amt

    def debit(self,amt):
        self.blance-=amt
                

hemanth = Sbi('pg hemanth',7815939981,47589687,'BSE34563HRY',500)
