bill = 0
t_bill = 0
t = ""
menu  = """ 
      BURGERS
      
1: Zinger burger: 230
2: Zinger cheese burger: 260
3: Thames special burger: 320
4: Beef Burger 250
5: Tower Burger: 320
6: Fish Burger: 260
7: Fish Cheese burger: 290
8: Fire Stone Burger: 290
9: Crispy Byurger: 170
10: Chicken Burger: 180
11: Tikka Burger 170
12: Shami Burger 170 \n
      STREAKS
      
1: Azona Streak: 650
2: Mushroom Streak: 650
3: Perrer Streak: 650
4: Polo Trscany 650\n
What category you prefer
press '1' for burger category
press '2' for streaks category  """
burgers_menu = """      BURGERS\n
press '1' for  Zinger burger: 230
press '2' for Zinger cheese burger: 260
press '3' for Thames special burger: 320
press '4' for Beef Burger 250
press '5' for Tower Burger: 320
press '6' for Fish Burger: 260
press '7' for Fish Cheese burger: 290
press '8' for Fire Stone Burger: 290
press '9' for Crispy Byurger: 170
press '10' for Chicken Burger: 180
press '11' for Tikka Burger 170
press '12' for Shami Burger 170 """ 

streaks_menu = """       STREAKS\n
press '1' for Azona Streak: 650
press '2' for Mushroom Streak: 650
press '3' for Perrer Streak: 650
press '4' for Polo Trscany 650\n"""
while True:
    a = input(menu) # The menu will be printed here and also to choose burger menu or streak menu
    if a == "1": #  user will select burger menu or  streak menu
        b = input(burgers_menu)
        if  b=="1":   # user will select the burgers
            p = 230
            c = int(input("Enter the no of quantity of zinger burger you want "))
                            # user will select the quantity of burger
            bill = p*c     # here we are multiplying the price and quantity c that user will be entered by user
            t_bill +=bill  # here we are making the total bill which can be written as ( t_bill = t_bill + bill)
            y = str(c)
            z = str(bill)      
# here we are changing the type of no of quantity int into str because python
#can not concatenate the string and int that we will do further and there is one 
#question  arising  why we are not taking no of quantity directly as string from 
#user no that will be wrong approach because we have to multiply that number by 
#price forcreating the total bill so if we will take string then string cant be 
#multiplied  with int """  
           
                                
              
            t+= y + " zinger buregers = "+z+"\n"    
#here in y there is string of no of quantity
#and in  the bill we have stored the  price multiply
#by quantity and and in z there is its string of bill
#we have just did it because we are wanting to
#concatenate quantity,burger name and its price just like
#this ..... 2 zinger burgers = 460 """
            d  = input("Continue (y/n) ") # here user will select the again he will choose or not
            if d=="n":
                break
        elif b=="2":
            p = 260
            c = int(input("Enter the no of quantity of Zinger cheese burger you want "))
            bill = p*c
            t_bill +=bill
            y = str(c)
            z = str(bill)
            t+= y + " zinger cheese  buregers = "+z+"\n"
            d  = input("Continue (y/n) ")
            if d=="n":
                break
        elif b=="3":
            p = 320
            c = int(input("Enter the no of quantity of Thames special burger you want "))
            bill = p*c
            t_bill +=bill
            y = str(c)
            z = str(bill)
            t+= y + " thames special buregers = "+z+"\n"
            d  = input("Continue (y/n) ")
            if d=="n":
                break
            
        elif b=="4":
            p = 250
            c = int(input("Enter the no of quantity of Beef Burger you want "))
            bill = p*c
            t_bill +=bill
            y = str(c)
            z = str(bill)
            t+= y + " Beef buregers = "+z+"\n"
            d  = input("Continue (y/n) ")
            if d=="n":
                break
        elif b=="5":
            p = 320
            c = int(input("Enter the no of quantity of Tower Burger you want "))
            bill = p*c
            t_bill +=bill
            y = str(c)
            z = str(bill)
            t+= y + " Tower buregers = "+z+"\n"
            d  = input("Continue (y/n) ")
            if d=="n":
                break
        elif b=="6":
            p = 260
            c = int(input("Enter the no of quantity of Fish Burger you want "))
            bill = p*c
            t_bill +=bill
            y = str(c)
            z = str(bill)
            t+= y + " Fish buregers = "+z+"\n"
            d  = input("Continue (y/n) ")
            if d=="n":
                break
        elif b=="7":
            p = 290
            c = int(input("Enter the no of quantity of Fish Cheese burger you want "))
            bill = p*c
            t_bill +=bill
            y = str(c)
            z = str(bill)
            t+= y + " Fish Cheese burger buregers = "+z+"\n"
            d  = input("Continue (y/n) ")
            if d=="n":
                break
        elif b=="8":
            p = 290
            c = int(input("Enter the no of quantity of Fire Stone Burger you want "))
            bill = p*c
            t_bill +=bill
            y = str(c)
            z = str(bill)
            t+= y + " Fire stone buregers = "+z+"\n"
            d  = input("Continue (y/n) ")
            if d=="n":
                break
        elif b=="9":
            p = 170
            c = int(input("Enter the no of quantity of Crispy Byurger  you want "))
            bill = p*c
            t_bill +=bill
            y = str(c)
            z = str(bill)
            t+= y + " Crispy buregers = "+z+"\n"
            d  = input("Continue (y/n) ")
            if d=="n":
                break
        elif b=="10":
            p = 180
            c = int(input("Enter the no of quantity of Chicken Burger you want "))
            bill = p*c
            t_bill +=bill
            y = str(c)
            z = str(bill)
            t+= y + " Chicken buregers = "+z+"\n"
            d  = input("Continue (y/n) ")
            if d=="n":
                break
        elif b=="11":
            p = 170
            c = int(input("Enter the no of quantity of Tikaa Burger  you want "))
            bill = p*c
            t_bill +=bill
            y = str(c)
            z = str(bill)
            t+= y + " Tikka buregers = "+z+"\n"
            d  = input("Continue (y/n) ")
            if d=="n":
                break
        elif b=="12":
            p = 170
            c = int(input("Enter the no of quantity of Shami Burger you want "))
            bill = p*c
            t_bill +=bill
            y = str(c)
            z = str(bill)
            t+= y + " Shami buregers = "+z+"\n"
            d  = input("Continue (y/n) ")
            if d=="n":
                break
        
        
    elif a == "2":
        b = input(streaks_menu)
        if b=="1":
            p = 650
            c = int(input("Enter the no of quantity of Azona streak you want "))
            bill = p*c
            t_bill +=bill
            y = str(c)
            z = str(bill)
            t+= y + " Azona streak = "+z+"\n"
            d  = input("Continue (y/n) ")
            if d=="n":
                break
        elif b=="2":
            p = 650
            c = int(input("Enter the no of quantity of Mushroom streak you want "))
            bill = p*c
            t_bill +=bill
            y = str(c)
            z = str(bill)
            t+= y + " mushroo streak = "+z+"\n"
            d  = input("Continue (y/n) ")
            if d=="n":
                break
        elif b=="3":
            p = 650
            c = int(input("Enter the no of quantity of Perrer streak you want "))
            bill = p*c
            t_bill +=bill
            y = str(c)
            z = str(bill)
            t+= y + " Perrer streak = "+z+"\n"
            d  = input("Continue (y/n) ")
            if d=="n":
                break
        elif b=="4":
            p = 650
            c = int(input("Enter the no of quantity of Azona polo Trscany you want "))
            bill = p*c
            t_bill +=bill
            y = str(c)
            z = str(bill)
            t+= y + " Azona polo Trscany = "+z+"\n"
            d  = input("Continue (y/n) ")
            if d=="n":
                break
    else :
        print("Wrong input")
w = str(t_bill)
z = "Total bill :"+w

        
        
s = "Desktop"
f = "bill.txt"
j = str(bill)
import os
file = os.path.join(s,f)
with open(file,"w") as f:
    f.write(t)
    f.write(z)
        
    
    
