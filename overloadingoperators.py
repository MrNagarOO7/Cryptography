class v:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self,o):
        return (self.a+o.a,self.b+o.b)

    def mod(self,o):
        return(self.a%o.a,self.b%o.b)
    
    def equals(self,other):
        if(self.a==other.a and self.b==other.b): return True
        else: return False

v1=v(11,2)
v2=v(10,2)
print(v1+v2)
print(v1.equals(v2))
print(v1.mod(v2))
