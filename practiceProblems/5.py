import os
file = os.path.join("Desktop","record.txt")
f =  open(file,"w")
choice = "Y"
while choice == "y" or choice =="Y":
    n = input("Name = ") 
    f.write("Name:"+n+"\n")
    m = float(input("Math marks "))
    if m>100:
        print("Ops something went  wrong  please re-enter the marks")
        m = float(input("Math marks "))
        m = str(m)
        f.write("Maths: "+m+"\n")
    else :
        m = str(m)
        f.write("Maths: "+m+"\n")
        
    p = float(input("Physics Marks "))
    if p>100:
        print("please re-enter the marks")
        m = float(input("Physics Marks "))
        m = str(m)
        f.write("physics: "+m+"\n")
    else:
        p = str(p)
        f.write("physics: "+p+"\n")
        c = float(input("Chemistry Marks "))
    if c>100:
        print("please re-enter the marks")
        m = float(input("Chemistry Marks: "))
        m = str(m)
        f.write("chemistry: "+m+"\n")
    else:
        c = str(c)
        f.write("chemistry: "+c+"\n")
    choice = input("Continue Y/N ")
    if not choice=="Y" or not choice == "y":
        f.close()
