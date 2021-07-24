a = input("Enter a string ")
c = 0
z = ""
for i in a:
    if i==" ":
        continue
    else:
        c+=1
print("The total number of characters in the string",c)
print("\nThe first character of the string is",a[0])
b = a
b = b.replace(" ","")
print("\nThe first three characters of the string are",b[0:3])
print("\nThe last three characters of the string are",a[-1:-4:-1])
print("\nThe string backwards are: ",a[::-1])
b = a
b.replace(" ","")
print("\nThe seventh charcter of the string is",b[6])
z = a.replace(a[0],"")
z = z.replace(a[-1],"")
print("After deleting first and last character the string is ",z)
print(a.replace("a","e"))

