class over:
    l=10
    h=10
    w=9
    def area(self,l,h):
        self.h=h
        self.l=l
        return(self.l*self.h)

    def area(self,l,h,w):
        self.h=h
        self.l=l
        self.w=w
        return(self.l*self.h*self.w)

o1=over()
print(o1.area(2,3,4))
print(o1.area(2,3))

    
