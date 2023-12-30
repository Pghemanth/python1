class father:
    def dd(self,param):
        self.01 = param

class child(father):
    def dd(self,param):
        self.02=param

obj=child(22)
print"%d%d"%(obj.01,obj.02)                