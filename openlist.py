m=[]
def all(l):
    for x in l:
        if(type(x)==list or type(x)==tuple):
            all(x)
        else:
            m.append(x)
l=[[1,2],[3],["k",[9,[14,[12,[11],"l"]]]],[(0.4,0.5),0.6],0.7]
all(l)
print(m)
