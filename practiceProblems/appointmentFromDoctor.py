q = input("press 'm' for make appointment \n press 'g' to record bp \npress 'g' to record gulucose \npress 't' to record temperature \n press 'a' to check upcoming appointments \n press 'h' to print the appointment history  ")
time = " "
if q==m:
    print("Doctors availibility time on 'a' 7 april is  8 am to 2 pm \n'b' 8 april is  8 am to 2 pm\n'c' 9 april is  8 am to 2 pm\n'd' 10 april is  8 am to 2 pm")
    p == input("Please select the appointment timings ")
    if p == a:
        time = "7 april is  8 am to 2 pm"
    elif p == b:
        time = " 8 april is  8 am to 2 pm"
    elif p==c:
        time = " 9 april is  8 am to 2 pm"
    elif p == d:
        time = " 10 april is  8 am to 2 pm"
    
elif q==g:
    print("Record bp or Record Gulucose")
elif q==t:
    print("Record temperature ")
elif q==a:
    print("Upcoming appointments\n 4pm to 6pm \n 8pm to 10pm")
elif q==h:
    print("Appointment history\n",time)
x = "Desktop"
y = "summary.txt"
import os
filename = os.path.join(x,y)
with open(filename,"w") as f:
    f.write(time)
