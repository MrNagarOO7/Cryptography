class p:
    def show(self):
        print("parent")

class q(p):
    def show(self):
        print("child")

q1=q()
q1.show()   #object of child so child's show method
p1=p()
p1.show()
