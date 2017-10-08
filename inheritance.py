class p:
    leng,hei=10,10
    def set(self,l,h):
        self.leng=l
        self.hei=h

class q(p):
    def area(self):
        return self.leng*self.hei

q1=q()
q1.set(15,20)
q2=q()
print("area:",q2.area())# q2's leng and hei=10 
print("area:",q1.area())
print(issubclass(q,p))# true if q is child of p
print(isinstance(q1,q))#true if q1 is intance object of q
    
