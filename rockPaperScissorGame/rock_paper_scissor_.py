choice = "Y"
while choice == "Y" or choice =="y" :
    a = input("Enter first player name: ")
    b = input("Enter second player name: ")
    x = input( a + " what will you choose  press 'r' for  rock or press 'p' for paper or press 's' for scissor? ")
    y = input( b + " what will you  choose press 'r' for  rock or press 'p' for paper or press 's' for scissor? ")
    if x==y:
        print("Its a tie")
    
    elif x=="r" and  y=="s" :
        print(a,"won")
    elif x=="r" and  y=="p" :
        print(b,"won")
    
    
  
        
    
    elif x=="s" and  y=="p" :
        print(a,"won")
    elif x=="s" and  y=="r" :
        print(b,"won")
    
    
   
        
        
    elif x=="p" and  y=="r" :
        print(a,"won")
    elif x=="p" and  y=="s" :
        print(b,"won")
    
 
    else :
        print("Wrong Input try again")
        continue
    choice=input("Continue Y/N ")
    
    
    
    
    
    
    
    
   
    
    
   
