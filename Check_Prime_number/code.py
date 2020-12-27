def check_prime(x):
    if x>1: # its a check for greater than one  
        n=0
        for i in range(2,x): # here we are starting loop from 2 because 0 and 1 are not prime numbers 
            if x%i==0: 
                n=1
        if n==1:
            print("its not a prime number")
        else:
            print("its a prime number")
    else:
        print("its not a prime number")
