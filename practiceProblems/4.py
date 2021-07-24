a = [43,56,3,4,2,6,7,6,0]
a = []
b = 1
while b<11:
    if b==1:
        z = "st"
    elif b==2:
        z = "nd"
    elif b==3:
        z = "rd"
    else :
        z  = "th"
    e = str(b)
    c = int(input("Enter the "+e+z+" integer:"))
    a.append(c)
    b+=1
d = int(input("\nEnter the number to check "))
for i in a:
    n = i
    if d==i:
        break
if n == d:
    print("Its present")
else :
    print("Not present")
    

