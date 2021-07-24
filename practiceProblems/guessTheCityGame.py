import random
CITIES = ["peshawar", "islamabad", "lahore", "multan", "quetta", "karachi"]
word = random.choice(CITIES)
chances = 10
while chances>0 :
    a = input("Enter a city name to guess ")
    if a == word:
        print("Yayyy... correct word")
        break
    else:
        chances -=1
        print("Wrong choice\nYou have ",chances,"number of chances left ")
        
        
    
