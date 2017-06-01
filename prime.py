for x in range(2,int(input("ramge:"))):
    for y in range(2,x):
        if(x%y==0):
            break
    else:
        print(x)
