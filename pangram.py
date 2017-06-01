l=set(input("enter pangram").lower())
print(l)
b={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","v","w","x","y","z"}
print("yes")if(len(b-l)==0) else print("no")
