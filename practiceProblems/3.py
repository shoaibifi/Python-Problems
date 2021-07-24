a = int(input("Enter your matric total marks "))
b = int(input("Enter your matric obtained marks"))
c = int(input("Enter the fsc total marks "))
d = int(input("Enter the fsc obtained marks "))
e = input(" Are you Hafiz-e-quran y/n ")
if e=="y":
    e=20
else:
    e=0
f = int(input("Enter the obtained equate marks "))
total_equate_marks = 500
percentage = (b+d+e+f)*100/(a+c+total_equate_marks)
print("Your aggeregate is ",percentage)
if percentage>90:
    g = input("Congratulation you got an admission in Electrical Will u study in it or you will Choose any other department \npress '1' for this studying in this department \npress '2' for any other department ")
    if g=="2":
        h = input("You are eligible for these departments \npress '1' computer engineering \npress'2' computer science \npress'3' for Mechanical \npress '4 Architecture' ")
        if h=="1":
                 print("Congratulation you got Admission in Computer engineering")
        elif h=="2":
                print("Congratulation you got Admission in Computer Science ")
        elif h=="3":
            print("Congratulation you got Admission in Mechanical ")
        elif h=="4":
            print("Congratulation you got Admission in Architecture ")
        else :
            print("Wrong input press the right button ")
        
            
elif percentage>85 and percentage<90:
    g = input("Congratulation you got an admission in Computer engineering Will u study in it or you will Choose any other department \npress '1' for this studying in this department \npress '2' for any other department")
    if g=="2":
        h = input("You are eligible for these departments \n'1' computer science \npress'2' for Mechanical \n press '3' Architecture ")
        if h=="1":
            print("Congratulation you got Admission in Computer Science ")
        elif h=="2":
            print("Congratulation you got Admission in Mechanical ")    
        elif h=="3":
            print("Congratulation you got Admission in Architecture ")
        else :
            print("Wrong input press the right button ")
        
elif percentage>83 and percentage< 85:
    g = input("Congratulation you got an admission in Computer science  Will u study in it or you will Choose any other department \npress '1' for this studying in this department \npress '2' for any other department ")

    if g=="2":
        h = input("You are eligible for these departments \npress '1' for Mechanical \npress '2' Architecture' ")
        if h=="1":
            print("Congratulation you got Admission in Mechanical ")    
        elif h=="2":
            print("Congratulation you got Admission in Architecture ")
        else :
            print("Wrong input press the right button ")
elif percentage>80 and percentage < 83:
    g = input("Congratulation you got an admission in Mechanical Will u study in it or you will Choose any other department \npress '1' for this studying in this department \npress '2' for any other department ")
    if g=="2":
        h = input("You are eligible for this departments \npress '1' Architecture' ")
        if h=="1":
            print("Congratulation you got an Admission in Architecture ")
        else :
            print("Wrong input press the right button ")
        
elif percentage>75 and percentage < 80:
    print("Congratulation you got Admission in Architecture and you are only eligible for it...")
else:
    print("Your aggregate is less then our requirements you didn't got an admission better luck next time ")
