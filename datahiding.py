class count:
    __c=0

    def plusone(self):
         self.__c+=1
         print(self.__c)

c1=count()
c1.plusone()
print(c1._count__c)# object __c name is c1._classname__objectname
print(c1._c) #not working its use count class private variable not object var
