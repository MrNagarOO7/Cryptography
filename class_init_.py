class emp:
    sal=10
    name="anonymous"

    def __init__(self,name,sal): #create constuctor
        self.name=name
        self.sal=sal
        
    def disp(self):
        print(self.name," salary:",self.sal)

emp1=emp("yopp",123)
emp1.name="yoss"
emp1.disp()
emp2=emp("kaka",34)
emp2.disp()
print(hasattr(emp1,"sal")) #check the attribute
print("doc:",emp.__doc__)
print(emp.__name__)#class name
print(emp.__module__)#module name
del emp1 #delete the object
emp1.disp()
